**Examples of onbox python scripts for Cisco NXOS Platforms**

**What are these files?**

clear_all_multicast.py |
Clear all multicast state for specific group (mcast_g)

light_levels.py |
Optical Light Levels for specific interface (eth_int)

cdp_lldp_neighbors.py | 
Discover both CDP and LLDP neighbors with a single command


**Usage**

These python scripts have been tested on the Nexus 3000, 5600, and 3500. They
probably will work on any NXOS device (9500/9300/5500/7000/7700), but I have
not tested on those platforms. 

**Keep in mind that Python 2.7 is what's installed on the Cisco NXOS Linux guestshell, so print commands will be in the older syntax.**

Create a scripts directory on bootflash: (example:**_mkdir
bootflash:python_scripts_**) and copy the script you want to use to this
directory (USB/SCP/TFTP).

I find it user friendly to use a cli alias that executes the script. 

**Example:**
cybertron-1(config)# **_cli alias name light
python bootflash:python_scripts/light_levels.py_**

**Execution:**
cybertron-1(config)# **_light eth1/1_**

**Result:**
Returning optical light levels for ...

Ethernet 1/1

  Tx Power       -5.03 dBm       0.00 dBm  -13.56 dBm   -3.00 dBm     -9.50 dBm
** **   
  Rx Power      -30.00 dBm --    2.99 dBm  -21.54 dBm    0.00 dBm    -16.98 dBm

** **

If you find these scripts
helpful and want to contribute or recommend something specific please contact
me shaun@4g1vn.com
