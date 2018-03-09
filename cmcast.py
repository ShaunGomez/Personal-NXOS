import sys
from cisco import cli
# v1.2
# Shaun Gomez
#
#clear all multicast state for given group on NXOS
#
#
mcast_g = str(sys.argv[1])
cli("clear ip pim route "+mcast_g) 
cli("clear ip mroute data-created "+mcast_g)
cli("clear ip igmp route "+mcast_g)
cli("clear ip igmp groups "+mcast_g)
print 'All Multicast State Cleared For:'
print mcast_g