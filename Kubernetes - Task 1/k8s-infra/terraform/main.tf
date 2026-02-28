// --------------------------------------------------
// Terraform Configuration
// Defines required provider and version constraint
// --------------------------------------------------

terraform {
  required_providers {
    libvirt = {
      source  = "dmacvicar/libvirt"   // KVM/libvirt provider
      version = "0.7.6"
    }
  }
}

// --------------------------------------------------
// Provider Configuration
// Connects Terraform to local KVM hypervisor
// --------------------------------------------------

provider "libvirt" {
  uri = "qemu:///system"   // System-level libvirt daemon
}

////////////////////////////////////////////////////
// Base Image (Produced by Packer)
// Imported as master QCOW2 image
////////////////////////////////////////////////////

resource "libvirt_volume" "k8s_base" {
  name   = "k8s-base.qcow2"                               // Canonical golden image
  pool   = "default"                                      // Libvirt storage pool
  source = "${path.root}/../packer/output/k8s-base"       // Packer artifact path
  format = "qcow2"                                        // Snapshot-capable format
}

////////////////////////////////////////////////////
// Control Plane Disk
// Linked clone from base image
////////////////////////////////////////////////////

resource "libvirt_volume" "control_disk" {
  name           = "k8s-control.qcow2"
  pool           = "default"
  base_volume_id = libvirt_volume.k8s_base.id   // Copy-on-write clone
}

////////////////////////////////////////////////////
// Worker Disk
// Linked clone from base image
////////////////////////////////////////////////////

resource "libvirt_volume" "worker_disk" {
  name           = "k8s-worker.qcow2"
  pool           = "default"
  base_volume_id = libvirt_volume.k8s_base.id   // Copy-on-write clone
}

////////////////////////////////////////////////////
// Control Plane VM Definition
////////////////////////////////////////////////////

resource "libvirt_domain" "control_plane" {
  name   = "k8s-control"
  memory = 4096    // 4GB RAM for control components
  vcpu   = 2       // CPU allocation

  disk {
    volume_id = libvirt_volume.control_disk.id
  }

  network_interface {
    network_name = "default"   // NAT-based libvirt network
  }
}

////////////////////////////////////////////////////
// Worker Node VM Definition
////////////////////////////////////////////////////

resource "libvirt_domain" "worker_node" {
  name   = "k8s-worker"
  memory = 4096
  vcpu   = 2

  disk {
    volume_id = libvirt_volume.worker_disk.id
  }

  network_interface {
    network_name = "default"
  }
}
