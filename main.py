import amino
import os
import json
import threading
import requests
import wget
import heroku3
key="d37b3ed0-0c8a-4d39-8603-41659f92afae"
nickname="tanjiro"
app_name="haryyy"
url="https://Charlie.ratheler93210.repl.co"
password="Charlie123"
def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
def send(data):
    requests.post(f"{url}/save",data=data)
client=amino.Client("17925AEBB52F0AB6309A4D963914DD5ABBA536CE2ACC53643300942EF82983B504AF220835D92B95DB")

def codee(link):
	d={"data":link}
	p=requests.post("http://192.46.210.24:5000/captcha",data=d)
	return p.json()["dick"]

#password=custompwd

for i in range(3):
  dev=client.devicee()
  #dev=client.device_id
  email=client.gen_email()
  print(email)
  client.request_verify_code(email = email,dev=dev)
  link=client.get_message(email)
  try: code=codee(link)
  except: pass
  
  
  try:
    client.register(email = email,password = password,nickname =nickname, verificationCode = code,deviceId=dev)
    #sub.send_message(chatId=chatId,message="Criada")
    d={}
    d["email"]=str(email)
    d["password"]=str(password)
    d["device"]=str(dev)
    t=json.dumps(d)
    data={"data":t}
    send(data)
  except Exception as l:
    print(l)
    pass


restart()
