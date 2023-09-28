import os
import time
import random
from datetime import datetime

timetowait =  5

currenttime = datetime.now()

regions = ["us", "au", "hr", "bg", "ca", "dk"]

print("mullvad auto ip changer - powered by DH Network")
print("starting...")

while True:
    print("-----------------------------------------")
    print("rotating ip now")
    randregion = random.choice(regions)
    print(randregion)
    os.system("mullvad relay set location " + str(randregion))
    os.system("mullvad connect")
    print("connected at " + str(currenttime))
    print("waiting " + str(timetowait) + " minutes")
    print("-----------------------------------------")
    time.sleep(int(timetowait) * 60)