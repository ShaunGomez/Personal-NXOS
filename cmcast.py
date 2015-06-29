import sys
from cisco import cli
# v1.0
# Shaun Gomez
#
#clear multicast state for given group on NXOS
#
#
mcast_g = str(sys.argv[1])
cli("clear ip pim route "+mcast_g) 
cli("clear ip mroute data-created "+mcast_g)
cli("clear ip igmp route "+mcast_g)
print 'All Multicast State Cleared For:'
print mcast_g
print 'Thank You! Come again'