import sys
from cisco import cli
from cisco import clip
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
print 'Verification of State Clear'
clip("show ip mroute "+mcast_g)
clip("show ip pim route "+mcast_g)
clip("show ip igmp groups "+mcast_g)
clip("show ip igmp route "+mcast_g)
print "Verification Complete"