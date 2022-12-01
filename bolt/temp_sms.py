import config as conf
from boltiot import Sms, Bolt
import json, time

minimum_limit = 500
maximum_limit = 600  


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms0 =  Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
sms1 =  Sms(conf.SID, conf.AUTH_TOKEN, '+917990687847', conf.FROM_NUMBER)
sms2 =  Sms(conf.SID, conf.AUTH_TOKEN, '+917219602306', conf.FROM_NUMBER)
sms3 =  Sms(conf.SID, conf.AUTH_TOKEN, '+917767984929', conf.FROM_NUMBER)

response = mybolt.analogRead('A0')
data = json.loads(response) 
print("Sensor value is: " + str(data['value']))
sensor_value = int(data['value'])

if sensor_value in range(400,600):
	output = mybolt.digitalWrite('1', "LOW")
	print(output)
elif sensor_value in range(100,399):
	output = mybolt.digitalWrite('1', "HIGH")
	print(output)
elif sensor_value in range(601,750):
	output = mybolt.digitalWrite('1', "HIGH")
	print(output)
else:
	print("ALL OK!")

while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        Temperature=(100*sensor_value)/1024 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms0.send_sms("The Current temperature sensor value is " +str(Temperature))
            response = sms1.send_sms("The Current temperature sensor value is " +str(Temperature))
            response = sms2.send_sms("The Current temperature sensor value is " +str(Temperature))
            response = sms3.send_sms("The Current temperature sensor value is " +str(Temperature))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
            print("Response1 received from Twilio is: " + str(response))
            print("1:Status of SMS at Twilio is :" + str(response.status))
            print("Response2 received from Twilio is: " + str(response))
            print("2:Status of SMS at Twilio is :" + str(response.status))
            print("Response3 received from Twilio is: " + str(response))
            print("3:Status of SMS at Twilio is :" + str(response.status))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(100)