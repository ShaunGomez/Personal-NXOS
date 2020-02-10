import sys
from cisco import clip 
# Author: Shaun Gomez
# Display both CDP & LLDP neighbors for @penultimateadam
# Python 2.7
clip ('show cdp nei ; show lldp nei')
print 'show neighbors (LLDP & CDP) completed'
