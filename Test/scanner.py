from smd.red import *
import time

MASTER_PORT =  "/dev/ttyUSB0" #depending on operating system, port, etc. may vary depending on the
master = Master(MASTER_PORT) #creating master object


print(master.scan()) #prints ID list of connected SMDs
