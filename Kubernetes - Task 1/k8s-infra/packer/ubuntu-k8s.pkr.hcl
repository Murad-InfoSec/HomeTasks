// --------------------------------------------------
// Packer Configuration
// Defines required builder plugins
// --------------------------------------------------

packer {
  required_plugins {
    qemu = {
      source  = "github.com/hashicorp/qemu"   // QEMU/KVM builder
      version = ">= 1.0.0"
    }
  }
}

// --------------------------------------------------
// QEMU Source Definition
// Builds Ubuntu cloud image into reusable QCOW2
// --------------------------------------------------

source "qemu" "ubuntu" {

  accelerator = "kvm"        // Hardware virtualization (must support KVM)
  disk_image  = true         // Treat ISO as disk image (cloud image mode)
  format      = "qcow2"      // Output disk format (snapshot-friendly)
  headless    = true         // No GUI (CI/CD compatible)

  iso_url      = "${path.root}/jammy-server-cloudimg-amd64.img"  // Base Ubuntu 22.04 cloud image
  iso_checksum = "none"       // Skipped (recommended to use SHA256 in production)

  output_directory = "${path.root}/output"   // Final image location
  vm_name          = "k8s-base"               // Artifact name

  memory = 2048   // VM RAM allocation (MB)
  cpus   = 2      // vCPU allocation

  ssh_username         = "ubuntu"             // Cloud-init default user
  ssh_private_key_file = "~/.ssh/k8s_key"     // Key-based authentication
  ssh_timeout          = "20m"                // Provisioning timeout window

  // Cloud-init seed files for automated initialization
  cd_files = [
    "${path.root}/user-data",
    "${path.root}/meta-data"
  ]

  cd_label = "cidata"   // Required label for NoCloud datasource

  shutdown_command = "sudo shutdown -P now"  // Graceful poweroff after provisioning
}

// --------------------------------------------------
// Build Phase
// Applies Kubernetes node baseline configuration
// --------------------------------------------------

build {
  sources = ["source.qemu.ubuntu"]

  provisioner "shell" {
    inline = [

      // System update
      "sudo apt update",

      // Install container runtime (K8s prerequisite)
      "sudo apt install -y containerd",

      // Ensure runtime starts on boot
      "sudo systemctl enable containerd",

      // Kubernetes requirement: disable swap
      "sudo swapoff -a",
      "sudo sed -i '/ swap / s/^/#/' /etc/fstab"
    ]
  }
}
