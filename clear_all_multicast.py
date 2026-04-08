"""
clear_all_multicast.py - Clear all multicast state for a given group on NX-OS.

Clears IGMP, PIM, mroute, and netstack state for a specified multicast group,
then runs verification show commands to confirm the clear completed.

Prerequisites:
    - NX-OS 9.3(5) or later (Python 3 support)
    - cisco module available (NX-OS SDK)
    - Multicast routing enabled on the device

Usage:
    python3 bootflash:python_scripts/clear_all_multicast.py <multicast-group>

CLI alias example:
    cli alias name clr_mcast python3
    bootflash:python_scripts/clear_all_multicast.py

Authors: Shaun Gomez & John Senkow
Version: 4.0
"""

import sys
import time
from cli import cli, clip

VERIFY_COUNTDOWN = 3


def validate_args():
    """Validate that a multicast group argument was provided."""
    if len(sys.argv) < 2:
        print("Usage: python3 clear_all_multicast.py <multicast-group>")
        print("Example: python3 clear_all_multicast.py 239.1.1.1")
        sys.exit(1)
    return sys.argv[1]


def clear_multicast_state(mcast_g):
    """Clear all multicast state for the specified group."""
    print(f"Clearing all multicast state for: {mcast_g}")
    cli("clear ip igmp groups " + mcast_g)
    cli("clear ip pim route " + mcast_g)
    cli("clear ip mroute data-created " + mcast_g)
    print(f"All multicast state cleared for: {mcast_g}")


def verify_multicast_state(mcast_g):
    """Run verification show commands after clearing multicast state."""
    print("Verifying state clear, please wait...")
    for countdown in range(VERIFY_COUNTDOWN, 0, -1):
        time.sleep(1)
        print(countdown)
    clip("show ip igmp groups " + mcast_g)
    clip("show ip igmp route " + mcast_g)
    clip("show ip mroute " + mcast_g)
    clip("show ip pim route " + mcast_g)
    print("Verification complete.")


def main():
    """Main entry point."""
    mcast_g = validate_args()
    clear_multicast_state(mcast_g)
    verify_multicast_state(mcast_g)


if __name__ == "__main__":
    main()
