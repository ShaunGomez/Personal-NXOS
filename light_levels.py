import sys
from cisco import cli
from cisco import clip
# v1.1
# Authors: Shaun Gomez & Predrag Zivkovic
# Return optical light levels for a specfied interface (passed through CLI argument)
# Python 2.7
eth_int = str(sys.argv[1])
    print "Returning optical light levels for " + eth_int
cli_cmd = clip("show interface " + eth_int + " trans detail | inc Tx|Rx")
    print cli_cmd
