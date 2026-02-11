# Network Troubleshooting Report  
*(Structured by Individual Cases)*

---

## Case 1 – VTY Remote Access Configuration (SW-2)

### Issue
VTY lines required authentication method for secure Telnet access.

### Initial Configuration
```console
line vty 0 4
 login
line vty 5 15
 login
```

### Corrective Action
```console
username netadmin secret <password>
line vty 0 4
 login local
```

Configuration saved:
```console
copy running-config startup-config
```

### Verification Output
```console
C:\>telnet 192.168.10.99
Trying 192.168.10.99 ...Open

User Access Verification
Username: netadmin
Password:
SW-2>
```

### Result
Remote access secured and operational.

---

## Case 2 – VLAN 10 Missing & Trunk Restriction (SW-1)

### Issue
- VLAN 10 absent on SW-1  
- Fa0/2 in default VLAN 1  
- Trunk did not allow VLAN 10  

### Corrective Action
```console
interface fa0/2
 switchport mode access
 switchport access vlan 10

interface gig0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

### Verification

VLAN table:
```console
VLAN 10 active    Fa0/2
```

Trunk status:
```console
Vlans allowed on trunk
Gig0/1  10,20,30
```

Ping test:
```console
C:\>ping 192.168.10.100
Reply from 192.168.10.100: bytes=32 time<1ms TTL=128
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

### Result
Intra-VLAN connectivity restored.

---

## Case 3 – SW-0 Fa0/1 Unconfigured

### Issue
Fa0/1 not assigned to required VLAN 20.

### Corrective Action
```console
interface fa0/1
 switchport mode access
 switchport access vlan 20
```

### Verification
```console
VLAN 20 active    Fa0/1, Fa0/2
```

### Result
Host successfully integrated into VLAN 20 broadcast domain.

---

## Case 4 – Unused Ports Hardening (SW-0 & SW-1)

### Issue
Unused ports active in default VLAN 1.

### Corrective Action

SW-0:
```console
interface range fa0/4 - 24
 shutdown
```

SW-1:
```console
interface range fa0/2 - 24
 shutdown
```

### Result Output
```console
%LINK-5-CHANGED: Interface FastEthernet0/4, changed state to administratively down
```

### Result
Unused ports disabled to improve security posture.

---

## Case 5 – VLAN 99 for Unused Ports (SW-2)

### Issue
Unused ports remained in default VLAN 1.

### Corrective Action
```console
interface range fa0/2 - 24
 switchport mode access
 switchport access vlan 99
```

System response:
```console
% Access VLAN does not exist. Creating vlan 99
```

### Result
Unused interfaces moved to isolated VLAN 99.

---

## Case 6 – Incorrect VLAN Assignment (SW-1 Fa0/1)

### Issue
Fa0/1 incorrectly assigned to VLAN 20.

### Corrective Action
```console
interface fa0/1
 switchport mode access
 switchport access vlan 30
```

### Verification
```console
VLAN 30 active    Fa0/1
```

Connectivity test:
```console
C:\>ping 192.168.30.102
Reply from 192.168.30.102: bytes=32 time<1ms TTL=128
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

### Result
Correct VLAN segmentation restored. End-to-end communication successful.

---

# Final Status

All issues were Layer 2 configuration errors:
- Missing VLANs  
- Incorrect access port assignments  
- Trunk VLAN filtering  
- Default VLAN exposure  
- Unsecured unused ports  

**Network Status: Fully Operational and Properly Segmented.**
