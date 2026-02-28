
packer {
  required_plugins {
    qemu = {
      source  = "github.com/hashicorp/qemu"
      version = ">= 1.0.0"
    }
  }
}

source "qemu" "ubuntu" {
  accelerator = "kvm"
  disk_image  = true
  format      = "qcow2"
  headless         = true

  # Use absolute-safe root path
  iso_url      = "${path.root}/jammy-server-cloudimg-amd64.img"
  iso_checksum = "none"

  output_directory = "${path.root}/output"
  vm_name          = "k8s-base"

  memory = 2048
  cpus   = 2

  ssh_username         = "ubuntu"
  ssh_private_key_file = "~/.ssh/k8s_key"
  ssh_timeout          = "20m"

  cd_files = [
    "${path.root}/user-data",
    "${path.root}/meta-data"
  ]

  cd_label = "cidata"

  shutdown_command = "sudo shutdown -P now"
}

build {
  sources = ["source.qemu.ubuntu"]

  provisioner "shell" {
    inline = [
      "sudo apt update",
      "sudo apt install -y containerd",
      "sudo systemctl enable containerd",
      "sudo swapoff -a",
      "sudo sed -i '/ swap / s/^/#/' /etc/fstab"
    ]
  }
}
