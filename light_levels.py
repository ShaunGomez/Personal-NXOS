"""
light_levels.py - Optical light levels for a specified interface on NX-OS

Executes 'show interface <intf> trans detail' filtered to Tx/Rx power levels
and prints the result to the console.

Prerequisites:
    - NX-OS device with Python 3.9 (on-box interpreter)
    - cisco module available (NX-OS SDK)
    - Interface must support optical transceiver (SFP/QSFP)

Usage:
    python bootflash:python_scripts/light_levels.py <interface>

CLI alias example:
    cli alias name light python
    bootflash:python_scripts/light_levels.py

Authors: Shaun Gomez & Predrag Zivkovic
Version: 3.0
"""

import sys
from cli import cli, clip


def validate_args():
    """Validate that an interface argument was provided."""
    if len(sys.argv) < 2:
        print ("Usage: python light_levels.py <interface>")
        print ("Example: python light_levels.py eth1/1")
        sys.exit(1)
    return str(sys.argv[1])


def show_light_levels(eth_int):
    """Display optical Tx/Rx power levels for the specified interface."""
    print ("Returning optical light levels for:  + eth_int")
    clip("show interface " + eth_int + " trans detail | inc Tx|Rx")


def main():
    """Main entry point."""
    eth_int = validate_args()
    show_light_levels(eth_int)


if __name__ == "__main__":
    main()
