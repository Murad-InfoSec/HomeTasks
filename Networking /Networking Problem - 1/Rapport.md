# Network Troubleshooting Report

---

## Case 1 – Access Port Configuration & Static IP Assignment (SW-1 / PC1)

### Issue

- Fa0/2 was not properly assigned to the required VLAN.
- PC1 required correct VLAN alignment and IP configuration.

---

### Initial VLAN Status

```console
SW-1#show vlan brief

VLAN Name                             Status    Ports
1    default                          active    Fa0/3–Fa0/24, Gig0/1, Gig0/2
10   VLAN0010                         active
20   VLAN0020                         active    Fa0/1
30   VLAN0030                         active
300  VLAN0300                         active
```

Fa0/2 was not assigned to VLAN 20.

---

### Corrective Action

```console
SW-1#configure terminal
SW-1(config)#interface fa0/2
SW-1(config-if)#switchport mode access
SW-1(config-if)#switchport access vlan 20
SW-1(config-if)#end
SW-1#copy running-config startup-config
```

System notifications observed:

```console
%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan10, changed state to down
%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan30, changed state to down
```

---

### Host Configuration (PC1)

IP configuration updated from DHCP to Static:

```
IP Address: 192.168.20.101
Subnet Mask: 255.255.255.0
```

---

### Result

- Fa0/2 successfully assigned to VLAN 20
- PC1 correctly placed in VLAN 20 broadcast domain
- Static IP aligned with subnet 192.168.20.0/24
- Configuration saved to NVRAM

**Network Status: Access layer configuration successfully completed.**
