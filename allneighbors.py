import sys
from cisco import clip 
#
#show cdp & lldp neighbors for @penultimateadam
#
clip ('show cdp nei ; show lldp nei')
print 'show neighbors (LLDP & CDP) completed'