Virtualization Setup Report

Platform: AlmaLinux
Goal: Prepare host for Kubernetes lab using KVM

1️⃣ Verified Hardware Virtualization

Checked CPU support:

egrep -c '(vmx|svm)' /proc/cpuinfo

Result > 0 confirms VT-x / SVM enabled.

2️⃣ Installed Virtualization Stack

Installed required components:

KVM

QEMU

libvirt

virt-install

virt-manager

bridge-utils

sudo dnf install -y qemu-kvm libvirt virt-install bridge-utils virt-manager
3️⃣ Enabled libvirt Service
sudo systemctl enable --now libvirtd

Verified:

systemctl status libvirtd

Service running successfully.

4️⃣ Verified KVM Modules
lsmod | grep kvm

Confirmed kvm_intel or kvm_amd loaded.

5️⃣ Configured Default Network

Defined and started default network:

sudo virsh net-define /usr/share/libvirt/networks/default.xml
sudo virsh net-start default
sudo virsh net-autostart default

Verified:

sudo virsh net-list --all

Network default is active and persistent.

6️⃣ Resolved System vs Session Context

System scope:

virsh -c qemu:///system net-list --all

To avoid sudo:

sudo usermod -aG libvirt eduard

(Re-login required)

7️⃣ Launched GUI

Started graphical manager:

virt-manager

Connected to:

qemu:///system
Current State

✔ KVM hypervisor active
✔ libvirt operational
✔ Default network configured
✔ GUI available
✔ Ready to create VMs for Kubernetes
