# Virtualization Deployment Report

**Platform:** AlmaLinux  
**Purpose:** Prepare host for Kubernetes lab  

---

## Deployment Summary

### 1️⃣ Hardware Verification

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo

Confirmed CPU virtualization support (VT-x / SVM enabled).

2️⃣ Stack Installation
sudo dnf install -y qemu-kvm libvirt virt-install virt-manager bridge-utils

Installed components:

KVM – Kernel-level hypervisor

QEMU – Virtual machine execution engine

libvirt – Management and orchestration layer

3️⃣ Service Activation
sudo systemctl enable --now libvirtd

Verified:

systemctl status libvirtd

libvirt daemon running successfully.

4️⃣ Hypervisor Verification
lsmod | grep kvm

Confirmed kvm_intel or kvm_amd module loaded.
Kernel operating as a Type-1 hypervisor.

5️⃣ Network Activation
sudo virsh net-define /usr/share/libvirt/networks/default.xml
sudo virsh net-start default
sudo virsh net-autostart default

Default NAT network activated via virbr0.

Underlying Architecture
virt-manager / virsh
        ↓
libvirt (orchestration layer)
        ↓
QEMU (VM process per instance)
        ↓
/dev/kvm interface
        ↓
KVM kernel module
        ↓
CPU virtualization extensions (VT-x / SVM)
Final State

Kernel-level hypervisor active

libvirtd operational

Default network configured

GUI management available

Environment ready for VM provisioning

Status: Virtualization stack successfully deployed and Kubernetes-ready.
