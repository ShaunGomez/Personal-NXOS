# Personal-NXOS

On-box Python scripts for Cisco NX-OS platforms (Nexus 3000, 3500, 5600, and likely 9000/7000/5500).

> **Note:** These scripts use Python 3.9, which is the on-box interpreter for Cisco NX-OS.

---

## Scripts

| Script | Description |
|---|---|
| `clear_all_multicast.py` | Clear all multicast state for a specified group |
| `light_levels.py` | Display optical Tx/Rx light levels for a specified interface |
| `cdp_lldp_neighbors.py` | Display both CDP and LLDP neighbors in a single command |

---

## Installation

1. Create a scripts directory on bootflash:

```
mkdir bootflash:python_scripts
```

2. Copy the script to the device via SCP, TFTP, or USB:

```
copy scp: bootflash:python_scripts/
```

3. Optionally, create a CLI alias for each script (see per-script examples below).

---

## clear_all_multicast.py

Clears IGMP, PIM, mroute, and netstack state for a specified multicast group,
then runs verification show commands to confirm the clear completed.

### Usage

```
python bootflash:python_scripts/clear_all_multicast.py <multicast-group>
```

### CLI Alias

```
cli alias name clr_mcast python bootflash:python_scripts/clear_all_multicast.py
```

### Execution

```
clr_mcast 239.1.1.1
```

---

## light_levels.py

Returns optical Tx/Rx power levels for a specified interface using
`show interface <intf> trans detail`.

### Usage

```
python bootflash:python_scripts/light_levels.py <interface>
```

### CLI Alias

```
cli alias name light python bootflash:python_scripts/light_levels.py
```

### Execution & Output

```
cybertron-1# light eth1/1
Returning optical light levels for: eth1/1

  Tx Power   -5.03 dBm    0.00 dBm   -13.56 dBm   -3.00 dBm    -9.50 dBm
  Rx Power  -30.00 dBm    2.99 dBm   -21.54 dBm    0.00 dBm   -16.98 dBm
```

---

## cdp_lldp_neighbors.py

Displays both CDP and LLDP neighbor tables in a single command. Useful in
mixed-vendor environments where both protocols are active simultaneously.

### Usage

```
python bootflash:python_scripts/cdp_lldp_neighbors.py
```

### CLI Alias

```
cli alias name sh_nei python bootflash:python_scripts/cdp_lldp_neighbors.py
```

### Execution

```
sh_nei
```

---

## Contributing

If you find these scripts helpful or want to suggest something specific,
feel free to reach out: shaun@4g1vn.com
