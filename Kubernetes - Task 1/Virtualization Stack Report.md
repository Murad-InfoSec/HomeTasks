<div style="font-family: Arial, Helvetica, sans-serif; line-height: 1.7; max-width: 1100px; margin: auto;">

<h1 style="text-align:center; border-bottom: 3px solid #c3002f; padding-bottom: 10px;">
Virtualization Deployment Report
</h1>

<p style="text-align:center; font-size:16px;">
<strong>Platform:</strong> AlmaLinux <br>
<strong>Purpose:</strong> Prepare host for Kubernetes Multi-Node Lab Environment
</p>

<hr style="border: 1px solid #ddd;">

<h2 style="color:#c3002f;">1️⃣ Hardware Verification</h2>

<p><strong>Objective:</strong> Confirm CPU virtualization extensions (VT-x / AMD-V).</p>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
egrep -c '(vmx|svm)' /proc/cpuinfo
</pre>

<p><strong>Validation Criteria:</strong></p>
<ul>
<li>Output &gt; 0 → Hardware acceleration enabled</li>
<li>Output = 0 → Virtualization not supported or disabled in BIOS</li>
</ul>

<p><strong>Status:</strong> Hardware acceleration confirmed.</p>

<hr>

<h2 style="color:#c3002f;">2️⃣ Virtualization Stack Installation</h2>

<p><strong>Installed Core Components:</strong></p>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
sudo dnf install -y qemu-kvm libvirt virt-install virt-manager bridge-utils
</pre>

<table style="width:100%; border-collapse: collapse; margin-top:10px;">
<tr style="background:#efefef;">
<th style="border:1px solid #ddd; padding:8px;">Component</th>
<th style="border:1px solid #ddd; padding:8px;">Role</th>
</tr>
<tr>
<td style="border:1px solid #ddd; padding:8px;">KVM</td>
<td style="border:1px solid #ddd; padding:8px;">Kernel-level Type-1 Hypervisor</td>
</tr>
<tr>
<td style="border:1px solid #ddd; padding:8px;">QEMU</td>
<td style="border:1px solid #ddd; padding:8px;">Virtual Machine Execution Engine</td>
</tr>
<tr>
<td style="border:1px solid #ddd; padding:8px;">libvirt</td>
<td style="border:1px solid #ddd; padding:8px;">Virtualization Orchestration & Management Layer</td>
</tr>
<tr>
<td style="border:1px solid #ddd; padding:8px;">virt-manager</td>
<td style="border:1px solid #ddd; padding:8px;">GUI-Based VM Management</td>
</tr>
</table>

<p><strong>Status:</strong> Virtualization stack successfully installed.</p>

<hr>

<h2 style="color:#c3002f;">3️⃣ Service Activation</h2>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
sudo systemctl enable --now libvirtd
</pre>

<p><strong>Verification:</strong></p>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
systemctl status libvirtd
</pre>

<p><strong>Expected Result:</strong> <code>active (running)</code></p>

<p><strong>Status:</strong> libvirt daemon operational.</p>

<hr>

<h2 style="color:#c3002f;">4️⃣ Hypervisor Verification</h2>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
lsmod | grep kvm
</pre>

<p><strong>Expected Modules:</strong></p>
<ul>
<li><code>kvm_intel</code> (Intel CPUs)</li>
<li><code>kvm_amd</code> (AMD CPUs)</li>
</ul>

<p><strong>Conclusion:</strong> Kernel is functioning as a hardware-accelerated hypervisor.</p>

<hr>

<h2 style="color:#c3002f;">5️⃣ Default Network Deployment</h2>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
sudo virsh net-define /usr/share/libvirt/networks/default.xml
sudo virsh net-start default
sudo virsh net-autostart default
</pre>

<p><strong>Verification:</strong></p>

<pre style="background:#f4f4f4; padding:15px; border-radius:8px;">
sudo virsh net-list --all
</pre>

<p><strong>Network Mode:</strong> NAT via <code>virbr0</code> bridge interface</p>

<p><strong>Status:</strong> Default virtual network active and persistent.</p>

<hr>

<h2 style="color:#c3002f;">Underlying Virtualization Architecture</h2>

<pre style="background:#111; color:#00ff88; padding:20px; border-radius:8px;">
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
</pre>

<hr>

<h2 style="color:#c3002f;">Final Deployment State</h2>

<ul>
<li>Kernel-integrated hypervisor active</li>
<li>Hardware acceleration enabled</li>
<li>Default NAT network operational</li>
<li>GUI-based VM management available</li>
<li>Environment ready for VM provisioning</li>
<li>Infrastructure prepared for Kubernetes multi-node lab</li>
</ul>

<hr>

<h2 style="text-align:center; color:green;">
Status: Virtualization stack successfully deployed and production-capable
</h2>

</div>
