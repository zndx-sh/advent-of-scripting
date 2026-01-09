import psutil as ps
import socket as sk
import time
from time import strftime, localtime
import platform as pt

print("="*10+" System Health "+"="*10)
print("Hostname: "+sk.gethostname()[:-6])
print("OS: "+pt.system())
print("Uptime: "+str(round(time.monotonic()/60.0, 2))+" min")
print("CPU Usage: "+str(ps.cpu_percent(interval=None)))
print("Memory Usage: "+str(ps.virtual_memory().percent))
print("Disk Usage: "+str(ps.disk_usage('/').percent))
print(strftime("%d-%m-%Y_%H:%M", localtime()))


