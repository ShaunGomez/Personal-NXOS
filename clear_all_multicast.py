import sys
import time
from cisco import cli
from cisco import clip
# v2.1
# Authors: Shaun Gomez & John Senkow
# Clear all multicast state for given group on NXOS
# Python 2.7
mcast_g = str(sys.argv[1])
cli("clear ip igmp groups "+mcast_g)
cli("clear ip pim route "+mcast_g) 
cli("clear ip mroute data-created "+mcast_g)
cli("clear ip netstack mroute "+mcast_g)
print 'All Multicast State Cleared For:'
print mcast_g
print 'Verification of State Clear, Please Wait 3 Seconds to Complete'
for verify_print in xrange(3,0,-1):
	time.sleep(1)
	print verify_print
clip("show ip igmp groups "+mcast_g)
clip("show ip igmp route "+mcast_g)
clip("show ip mroute "+mcast_g)
clip("show ip pim route "+mcast_g)
print "Verification Complete"
