# VLAN Segmentation & Switch Security Configuration Report

---

# 1. Objective

Configure VLAN segmentation as follows:

- VLAN 10 → PC4, PC5  
- VLAN 20 → PC0, PC1  
- VLAN 30 → PC2, PC3  

Additional requirements:

- PCs must communicate only within their own VLAN.
- SW-1 → Configure User EXEC password.
- SW-2 → Configure Privileged EXEC password (encrypted).
- SW-0 & SW-1 → Shutdown unused ports.
- SW-2 → Move unused ports from VLAN 1 to VLAN 99.

---

# 2. VLAN Configuration

---

## SW-0 Configuration (VLAN 20 – PC0, PC1)

### Create VLAN
```console
vlan 20
 name VLAN0020
```

### Assign Access Ports
```console
interface fa0/1
 switchport mode access
 switchport access vlan 20

interface fa0/2
 switchport mode access
 switchport access vlan 20
```

### Trunk to SW-2
```console
interface gig0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

---

## SW-1 Configuration (VLAN 30 – PC2, PC3)

### Create VLAN
```console
vlan 30
 name VLAN0030
```

### Assign Access Ports
```console
interface fa0/1
 switchport mode access
 switchport access vlan 30

interface fa0/2
 switchport mode access
 switchport access vlan 30
```

### Trunk to SW-2
```console
interface gig0/2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

---

## SW-2 Configuration (VLAN 10 – PC4, PC5)

### Create VLAN
```console
vlan 10
 name VLAN0010
```

### Assign Access Ports
```console
interface fa0/1
 switchport mode access
 switchport access vlan 10

interface fa0/2
 switchport mode access
 switchport access vlan 10
```

### Trunk Links
```console
interface gig0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30

interface gig0/2
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

---

# 3. Switch Security Configuration

---

## SW-1 – User Mode Password (Console Access)

```console
line console 0
 password cisco123
 login
service password-encryption
```

Result: Console access secured with encrypted password.

---

## SW-2 – Privileged Mode Password (Encrypted)

```console
enable secret securepass
```

Result: Privileged EXEC access protected with encrypted secret.

---

# 4. Port Security & Hardening

---

## SW-0 – Shutdown Unused Ports

```console
interface range fa0/3 - 24
 shutdown
```

---

## SW-1 – Shutdown Unused Ports

```console
interface range fa0/3 - 24
 shutdown
```

Result:
```
%LINK-5-CHANGED: Interface FastEthernet0/x, changed state to administratively down
```

Unused ports disabled.

---

## SW-2 – Move Unused Ports to VLAN 99

### Create VLAN 99
```console
vlan 99
 name UNUSED
```

### Assign Unused Ports
```console
interface range fa0/3 - 24
 switchport mode access
 switchport access vlan 99
```

Result:
```
% Access VLAN does not exist. Creating vlan 99
```

Unused ports removed from default VLAN 1.

---

# 5. IP Addressing Scheme

| VLAN | Subnet              | Hosts            |
|------|--------------------|-----------------|
| 10   | 192.168.10.0/24    | PC4, PC5        |
| 20   | 192.168.20.0/24    | PC0, PC1        |
| 30   | 192.168.30.0/24    | PC2, PC3        |

Static IP addressing configured on all PCs.

---

# 6. Connectivity Verification

## VLAN 20 Test
```console
C:\>ping 192.168.20.101
Reply from 192.168.20.101: bytes=32 time<1ms TTL=128
```

## VLAN 30 Test
```console
C:\>ping 192.168.30.102
Reply from 192.168.30.102: bytes=32 time<1ms TTL=128
```

## VLAN 10 Test
```console
C:\>ping 192.168.10.102
Reply from 192.168.10.102: bytes=32 time<1ms TTL=128
```

Inter-VLAN ping attempts fail (expected behavior).

---

# 7. Final Validation

✔ VLAN segmentation correctly implemented  
✔ Trunk links properly configured  
✔ PCs isolated within respective broadcast domains  
✔ SW-1 user access secured  
✔ SW-2 privileged access encrypted  
✔ Unused ports disabled (SW-0, SW-1)  
✔ Unused ports isolated in VLAN 99 (SW-2)  

---

# Network Status: Fully Operational, Segmented, and Hardened
