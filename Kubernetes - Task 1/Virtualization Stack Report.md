Virtualization Deployment Report

Platform: AlmaLinux
Purpose: Prepare host for Kubernetes multi-node lab

1️⃣ Hardware Verification

Confirmed CPU virtualization support (VT-x / SVM):

egrep -c '(vmx|svm)' /proc/cpuinfo

Output > 0 → Hardware acceleration enabled.

2️⃣ Virtualization Stack Installation

Installed core components:

sudo dnf install -y qemu-kvm libvirt virt-install virt-manager bridge-utils

Components deployed:

KVM → Kernel-level Type-1 hypervisor

QEMU → Virtual machine execution engine

libvirt → Orchestration & management layer

3️⃣ Service Activation
sudo systemctl enable --now libvirtd

Verified:

systemctl status libvirtd

Status: active (running)

4️⃣ Hypervisor Verification
lsmod | grep kvm

Confirmed kvm_intel or kvm_amd loaded.
Kernel now functioning as hypervisor.

5️⃣ Default Network Deployment
sudo virsh net-define /usr/share/libvirt/networks/default.xml
sudo virsh net-start default
sudo virsh net-autostart default

Verified:

sudo virsh net-list --all

Network default active via bridge virbr0 (NAT mode).

Underlying Architecture
virt-manager / virsh
        ↓
libvirt (management daemon)
        ↓
QEMU (one process per VM)
        ↓
/dev/kvm interface
        ↓
KVM kernel module
        ↓
CPU virtualization extensions
Final State

Kernel-integrated hypervisor active

Hardware acceleration enabled

Default NAT network operational

GUI management available

Environment ready for VM provisioning and Kubernetes deployment

Status: Virtualization stack successfully deployed and production-capable.
