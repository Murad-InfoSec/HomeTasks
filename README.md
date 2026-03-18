<h1 align="center">GitLab CE Infrastructure as Code</h1>

<p align="center">
  <img src="https://img.shields.io/badge/GitLab%20CE-18.9.2-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab CE 18.9.2"/>
  <img src="https://img.shields.io/badge/GitLab%20Runner-18.9.0-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab Runner 18.9.0"/>
  <img src="https://img.shields.io/badge/AlmaLinux-10.1-00B1A9?style=for-the-badge&logo=almalinux&logoColor=white" alt="AlmaLinux 10.1"/>
  <br/>
  <img src="https://img.shields.io/badge/Packer-QEMU-02A8EF?style=for-the-badge&logo=hashicorp&logoColor=white" alt="Packer"/>
  <img src="https://img.shields.io/badge/Terraform-libvirt-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform"/>
  <img src="https://img.shields.io/badge/Ansible-Playbooks-EE0000?style=for-the-badge&logo=ansible&logoColor=white" alt="Ansible"/>
  <img src="https://img.shields.io/badge/KVM-QEMU-009900?style=for-the-badge&logo=linux&logoColor=white" alt="KVM"/>
</p>

<p align="center">
  Fully automated GitLab CE deployment on KVM/libvirt.<br/>
  One script — Packer builds images, Terraform provisions VMs, Ansible configures everything.
</p>

---

## Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         deploy.sh                                   │
│                                                                     │
│  [1] SSH Keys  →  [2] Packer Build  →  [3] Terraform  →  [4] Ansible│
└─────────────────────────────────────────────────────────────────────┘
```

| Stage | Tool | Output |
|-------|------|--------|
| SSH Key Generation | `ssh-keygen` | Build-time + deployment ED25519 keys |
| Image Build | Packer + QEMU | `gitlab-main.qcow2` · `gitlab-runner.qcow2` |
| Infrastructure | Terraform + libvirt | 2 VMs · NAT network · storage pool |
| Configuration | Ansible | Runner registered · health check · HTML report |

---

## Network Architecture

```
Host (KVM hypervisor)
│
└─ libvirt NAT network: 172.16.30.0/24  (gitlab-net)
   │
   ├─ 172.16.30.128   gitlab-main    MAC 52:54:00:CE:B7:F0
   │  └─ GitLab CE 18.9.2 (omnibus)
   │
   └─ 172.16.30.129   gitlab-runner  MAC 52:54:00:CE:B7:F1
      └─ GitLab Runner 18.9.0 (shell executor)
```

> **Isolated network** — no external internet exposure. All traffic stays on the host.

---

## Prerequisites

<table>
<tr>
  <th>Tool</th>
  <th>Min. Version</th>
  <th>Notes</th>
</tr>
<tr><td>KVM / QEMU</td><td>—</td><td><code>qemu:///system</code> socket must be accessible</td></tr>
<tr><td>libvirt</td><td>—</td><td><code>libvirtd</code> running, user in <code>libvirt</code> group</td></tr>
<tr><td>virt-customize</td><td>—</td><td>Part of <code>guestfs-tools</code> / <code>libguestfs-tools</code></td></tr>
<tr><td>Packer</td><td>1.0+</td><td>With <code>hashicorp/qemu</code> plugin</td></tr>
<tr><td>Terraform</td><td>1.6+</td><td>libvirt provider downloaded automatically</td></tr>
<tr><td>Ansible</td><td>core</td><td><code>ansible-playbook</code> in PATH</td></tr>
<tr><td>ssh-keygen</td><td>—</td><td>ED25519 support required</td></tr>
</table>

`deploy.sh` will detect your distro and offer to install missing tools automatically.

---

## Quick Start

```bash
git clone <repo-url> gitlab-infra
cd gitlab-infra
chmod +x deploy.sh
./deploy.sh
```

After completion:

```
GitLab CE  :  http://172.16.30.128
Runner     :  172.16.30.129
SSH alias  :  ssh gitlab-main
```

Retrieve the initial root password:

```bash
ssh gitlab-main cat /home/gitlab-main/gitlab_initial_root_password.txt
```

> The file is auto-deleted by GitLab after 24 hours.

---

## deploy.sh Flags

| Flag | Description |
|------|-------------|
| `--skip-deps` | Skip dependency checking / installation |
| `--skip-keys` | Skip SSH key generation |
| `--skip-packer` | Skip Packer builds (reuse existing artifacts) |
| `--skip-terraform` | Skip Terraform provisioning |
| `--skip-ansible` | Skip Ansible post-deployment steps |
| `--force-keys` | Regenerate SSH keys even if they already exist |

Example — rebuild infrastructure without rebuilding images:

```bash
./deploy.sh --skip-packer
```

---

## Repository Structure

```
gitlab-infra/
├── packer/
│   ├── gitlab-main.pkr.hcl          # GitLab CE image (30 GB, 4 vCPU, 4 GB RAM)
│   ├── gitlab-runner.pkr.hcl        # Runner image   (20 GB, 2 vCPU, 2 GB RAM)
│   ├── http/
│   │   ├── gitlab-main/ks.cfg       # Kickstart — automated OS install
│   │   └── gitlab-runner/ks.cfg
│   └── artifacts/                   # Built QCOW2 images (git-ignored)
│
├── terraform/
│   ├── main.tf                      # Storage pool, network, volumes, VMs
│   ├── variables.tf                 # Input variable declarations
│   ├── terraform.tfvars             # Default values
│   └── ansible_postprocessor.tf    # null_resources: wait → register → check
│
├── ansible/
│   ├── ansible.cfg
│   ├── inventory/
│   │   ├── hosts.ini                # Static inventory (gitlab-main, gitlab-runner)
│   │   └── group_vars/all.yml       # Shared vars (URLs, runner config)
│   ├── playbooks/
│   │   ├── runner_register.yml      # Fetch token + register runner
│   │   ├── gitlab_check.yml         # Health checks → HTML report
│   │   └── gitlab_troubleshoot.yml  # Diagnostics + optional auto-fix
│   └── templates/
│       ├── gitlab_check_report.html.j2
│       └── gitlab_troubleshoot_report.html.j2
│
├── services/
│   ├── gitlab-main.service          # systemd unit — start VM with host
│   └── gitlab-runner.service        # Depends on gitlab-main.service
│
├── reports/                         # Generated HTML reports (git-ignored)
├── deploy.sh                        # Master orchestration script
└── generate_ssh_keys.sh             # Standalone key setup (legacy)
```

---

## Component Details

<details>
<summary><strong>Packer — Image Builds</strong></summary>

Both images boot from the AlmaLinux 10.1 minimal ISO via Kickstart (HTTP-served `ks.cfg`), then Packer shell provisioners run:

**gitlab-main** (`52:54:00:CE:B7:F0` → `172.16.30.128`)
1. Full system update
2. SELinux → permissive (required by GitLab omnibus)
3. Install GitLab CE 18.9.2 from official repo
4. Open HTTP firewall port (runner ↔ main communication)
5. Set static NetworkManager config keyed to MAC address
6. Save initial root password to `/home/gitlab-main/gitlab_initial_root_password.txt`
7. Clean build-time SSH key

**gitlab-runner** (`52:54:00:CE:B7:F1` → `172.16.30.129`)
1. Full system update
2. SELinux → permissive
3. Install `git` + GitLab Runner 18.9.0
4. Set static NetworkManager config
5. Clean build-time SSH key

> Runner registration is deferred to Ansible — the registration token is fetched from the live GitLab instance.

</details>

<details>
<summary><strong>Terraform — Infrastructure Provisioning</strong></summary>

Resources created in order:

1. **Storage pool** `gitlab` → `/var/lib/libvirt/images/gitlab`
2. **NAT network** `gitlab-net` → `172.16.30.0/24`, DNS enabled
3. **Volumes** — two QCOW2 disks cloned from Packer artifacts
4. **SSH key injection** — `virt-customize` injects deployment public keys before first boot
5. **VMs** — `gitlab-main` (4 GB / 2 vCPU) and `gitlab-runner` (2 GB / 2 vCPU)

After `terraform apply` the `ansible_postprocessor.tf` null_resources execute in sequence:

```
wait_for_gitlab_main  →  wait_for_gitlab_runner
    └─ ansible_runner_register  →  ansible_check  →  ansible_troubleshoot
```

**Key variables** (`terraform.tfvars`):

| Variable | Default |
|----------|---------|
| `libvirt_uri` | `qemu:///system` |
| `pool_path` | `/var/lib/libvirt/images/gitlab` |
| `gitlab_main_image` | `packer/artifacts/gitlab-main/gitlab-main` |
| `gitlab_runner_image` | `packer/artifacts/gitlab-runner/gitlab-runner` |
| `gitlab_main_ssh_private_key` | `~/.ssh/gitlab-infra/main_key` |
| `gitlab_runner_ssh_private_key` | `~/.ssh/gitlab-infra/runner_key` |

</details>

<details>
<summary><strong>Ansible — Configuration &amp; Health</strong></summary>

**Inventory** (`ansible/inventory/hosts.ini`)

```ini
[gitlab_main]
172.16.30.128 ansible_user=gitlab-main ansible_ssh_private_key_file=~/.ssh/gitlab-infra/main_key

[gitlab_runner]
172.16.30.129 ansible_user=gitlab-runner ansible_ssh_private_key_file=~/.ssh/gitlab-infra/runner_key
```

**runner_register.yml**
- Retrieves registration token via `gitlab-rails runner`
- Registers runner on `gitlab-runner` host with shell executor
- Restarts and verifies connectivity

**gitlab_check.yml**
- `gitlab-ctl status` — all services up
- Readiness / liveness HTTP probes
- `gitlab-rake gitlab:check`
- Firewall + SELinux verification
- Runner service active + `gitlab-runner verify`
- Outputs: `reports/gitlab_check_<timestamp>.html`

**gitlab_troubleshoot.yml**
- Identifies down services (puma, sidekiq, …)
- Optional auto-remediation: `ansible-playbook … -e autofix=true`
- Log tail collection for failed services
- Machine-ID collision detection
- Locale and SELinux denial checks
- Outputs: `reports/gitlab_troubleshoot_<timestamp>.html`

</details>

<details>
<summary><strong>systemd — VM Auto-start</strong></summary>

Install the units to start VMs automatically with the host:

```bash
sudo cp services/gitlab-main.service   /etc/systemd/system/
sudo cp services/gitlab-runner.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now gitlab-main gitlab-runner
```

`gitlab-runner.service` declares `Requires=gitlab-main.service`, ensuring correct boot order.

</details>

---

## SSH Access

After deployment, SSH aliases are configured in `~/.ssh/config`:

```bash
ssh gitlab-main    # → gitlab-main@172.16.30.128
ssh gitlab-runner  # → gitlab-runner@172.16.30.129
```

Keys are stored in `~/.ssh/gitlab-infra/`:

| Key | Purpose |
|-----|---------|
| `packer_key` | Build-time access (cleared from images post-build) |
| `main_key` | Deployment access to `gitlab-main` |
| `runner_key` | Deployment access to `gitlab-runner` |

---

## Manual Ansible Runs

Run health check:

```bash
cd ansible
ansible-playbook -i inventory/hosts.ini playbooks/gitlab_check.yml
```

Run diagnostics with auto-fix:

```bash
ansible-playbook -i inventory/hosts.ini playbooks/gitlab_troubleshoot.yml -e autofix=true
```

Re-register runner (e.g. after reset):

```bash
ansible-playbook -i inventory/hosts.ini playbooks/runner_register.yml
```

---

## Security Notes

- SELinux is set to **permissive** — required by GitLab omnibus installer.
- The root account is **locked** in both kickstart files; a dedicated wheel user is created per VM.
- The Packer build key is wiped from VM images before Terraform runs.
- Deployment keys are injected at provision time via `virt-customize`, never baked into images.
- The network is **isolated** (NAT only); no ports are exposed on the host.
- The initial GitLab root password file is auto-deleted by GitLab after 24 hours.
