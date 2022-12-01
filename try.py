import config as conf
from boltiot import Bolt
mybolt = Bolt(conf.API_KEY,conf.DEVICE_ID)
while True :
    print("Select Option :")
    led = int(input("1) LED on Press 1\t 2) LED off Press 0 \n"))
    if led == 1:
        response = mybolt.digitalWrite('1',"HIGH")
        print (response)
    elif led == 0:
        response = mybolt.digitalWrite('1',"LOW")
        print (response)
    else :
        print("Select Valid Option")
        continue
    br = input("Do you want to continue (y/n) : ")
    if (br == "N") or (br == "n") :
        break
print("Thank You")
