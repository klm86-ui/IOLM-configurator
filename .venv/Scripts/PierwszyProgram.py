from operator import truth
from enum import Enum
import requests
import numpy as np
from pythonping import ping
import time
import json
from datetime import datetime
import os
import winsound
from openpyxl import Workbook, load_workbook
import paho.mqtt.client as mqtt
#from KURS import STALA
STALA =33333





# GŁÓWNE USTAWIENIA PROGRAMU
ip=f"192.168.5.144" #Target IOLM device IP
ex_path = r"C:\Users\plsokopa\PycharmProjects\PythonProject"
logInterval = 5 # Main loop interval - for http data request and logging [s]
AUTHORIZATION=False     # In case of using Solution Block set TRUE
T1_INTERVAL=2000    # Timer 1 interval for notifications

# MQTT BROKER DATA - for example mosquitto
BROKER = "192.168.5.10"  # BROKER ip
PORT = 1883
PUB_TOPIC = "PythonMqttTopic"   # TEST TOPIC TO SEND
SUBS_TOPIC="MqttAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1" # Topic to subscribe with Python script

#-----------------------------------GetData-------------------------------------------------
GetProductData={"ProductCode":{"code":"request","cid":1,"adr":"/deviceinfo/productcode/getdata"},
                "FirmwareVersion":{"code":"request","cid":1,"adr":"/deviceinfo/swrevision/getdata"}}
GetMqttData={"MqttConnect":{"code":"request","cid":1,"adr":"/connections/mqttConnection/status/getdata"},
             "MqttCmd":{"code":"request","cid":1,"adr":"/connections/mqttConnection/mqttCmdChannel/status/getdata"}}
GetMqttDataSB={"MqttConnect":{"code":"request","cid":1,"adr":"/connections/mqttclient/status/getdata"},
             "MqttCmd":{"code":"request","cid":1,"adr":"/connections/mqttcommandchannel/status/getdata"}}
GetAdvancedData={"FreeMem":{"code":"request","cid":1,"adr":"/debug/freemem/getdata"},
                 "UpTime":{"code":"request","cid":1,"adr":"/debug/uptime/getdata"}}
GetPdin={"Pdin1":{"code":"request","cid":1,"adr":"/iolinkmaster/port[1]/iolinkdevice/pdin/getdata"},
         "Pdin2":{"code":"request","cid":1,"adr":"/iolinkmaster/port[2]/iolinkdevice/pdin/getdata"},
         "Pdin3":{"code":"request","cid":1,"adr":"/iolinkmaster/port[3]/iolinkdevice/pdin/getdata"},
         "Pdin4":{"code":"request","cid":1,"adr":"/iolinkmaster/port[4]/iolinkdevice/pdin/getdata"},
         "Pdin5":{"code":"request","cid":1,"adr":"/iolinkmaster/port[5]/iolinkdevice/pdin/getdata"},
         "Pdin6":{"code":"request","cid":1,"adr":"/iolinkmaster/port[6]/iolinkdevice/pdin/getdata"},
         "Pdin7":{"code":"request","cid":1,"adr":"/iolinkmaster/port[7]/iolinkdevice/pdin/getdata"},
         "Pdin8":{"code":"request","cid":1,"adr":"/iolinkmaster/port[8]/iolinkdevice/pdin/getdata"}}
GetIolinkEvent={"IolinkEventPort1":{"code":"request","cid":1,"adr":"/iolinkmaster/port[1]/iolinkdevice/iolinkevent/getdata"},
                "IolinkEventPort2":{"code":"request","cid":1,"adr":"/iolinkmaster/port[2]/iolinkdevice/iolinkevent/getdata"},
                "IolinkEventPort3":{"code":"request","cid":1,"adr":"/iolinkmaster/port[3]/iolinkdevice/iolinkevent/getdata"},
                "IolinkEventPort4":{"code":"request","cid":1,"adr":"/iolinkmaster/port[4]/iolinkdevice/iolinkevent/getdata"},
                "IolinkEventPort5":{"code":"request","cid":1,"adr":"/iolinkmaster/port[5]/iolinkdevice/iolinkevent/getdata"},
                "IolinkEventPort6":{"code":"request","cid":1,"adr":"/iolinkmaster/port[6]/iolinkdevice/iolinkevent/getdata"},
                "IolinkEventPort7":{"code":"request","cid":1,"adr":"/iolinkmaster/port[7]/iolinkdevice/iolinkevent/getdata"},
                "IolinkEventPort8":{"code":"request","cid":1,"adr":"/iolinkmaster/port[8]/iolinkdevice/iolinkevent/getdata"}
                }
GetTimerData={"Timer1Interval":{"code": "request","cid": 1,"adr": "/timer[1]/interval/getdata"},
              "Timer2Interval":{"code": "request","cid": 1,"adr": "/timer[1]/interval/getdata"}}
GetProcesParameters={"Voltage":{"code": "request","cid": 1,"adr": "/processdatamaster/voltage/getdata"},
                     "Temperature":{"code": "request","cid": 1,"adr": "/processdatamaster/temperature/getdata"},
                     "Current":{"code": "request","cid": 1,"adr": "/processdatamaster/current/getdata"},
                     "SupStatus":{"code": "request","cid": 1,"adr": "/processdatamaster/supervisionstatus/getdata"}}

# -----------------------------------GetData-Port event , device name and acyclic data------------------------------------------------
GetPortEvent={"Port1Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[1]/portevent/getdata"},
              "Port2Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[2]/portevent/getdata"},
              "Port3Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[3]/portevent/getdata"},
              "Port4Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[4]/portevent/getdata"},
              "Port5Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[5]/portevent/getdata"},
              "Port6Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[6]/portevent/getdata"},
              "Port7Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[7]/portevent/getdata"},
              "Port8Event":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[8]/portevent/getdata"}}

GetPortDeviceProductName={"Port1DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[1]/iolinkdevice/productname/getdata"},
                           "Port2DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[2]/iolinkdevice/productname/getdata"},
                           "Port3DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[3]/iolinkdevice/productname/getdata"},
                           "Port4DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[4]/iolinkdevice/productname/getdata"},
                           "Port5DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[5]/iolinkdevice/productname/getdata"},
                           "Port6DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[6]/iolinkdevice/productname/getdata"},
                           "Port7DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[7]/iolinkdevice/productname/getdata"},
                           "Port8DeviceProductName":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[8]/iolinkdevice/productname/getdata"}}

INDEX=16 # Vendor name ifm
SUBINDEX=0
GetPortReadAcyclic={"Port1ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[1]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}},
                    "Port2ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[2]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}},
                    "Port3ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[3]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}},
                    "Port4ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[4]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}},
                    "Port5ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[5]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}},
                    "Port6ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[6]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}},
                    "Port7ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[7]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}},
                    "Port8ReadAcyclic":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[8]/iolinkdevice/iolreadacyclic","data": {"index": INDEX,"subindex": SUBINDEX}}}

# -----------------------------------Command channel configuration---------------------------------------------------

BROKER_IP="192.168.5.10"
BROKER_PORT=1883
CMD_TOPIC="cmdTopic"
CMD_REPLY_TOPIC="reply"
AUTH={"user":"YWRtaW4=","passwd":"cGFzc3dvcmQ="}    # Authorization for Solution block
CmdConfig={ "Timer1Interval":{"code": "request","cid": 1,"adr": "/timer[1]/interval/setdata","data": {"newvalue": T1_INTERVAL}},
            "CmdStart":{"code": "request", "cid": 1, "adr": "/connections/mqttConnection/mqttCmdChannel/status/start"},
            "CmdReset":{"code": "request", "cid": 1, "adr": "/connections/mqttConnection/mqttCmdChannel/status/reset"},
            "CmdSetIp":{"code": "request", "cid": 2,"adr": "/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/brokerIP/setdata","data": {"newvalue": BROKER_IP}},
            "CmdSetPort":{"code": "request", "cid": 3,"adr": "/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/brokerPort/setdata","data": {"newvalue": BROKER_PORT}},
            "CmdSetTopic":{"code": "request", "cid": 4,"adr": "/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/cmdTopic/setdata","data": {"newvalue": CMD_TOPIC}},
            "CmdSetRepTopic":{"code": "request", "cid": 5,"adr": "/connections/mqttConnection/mqttCmdChannel/mqttCmdChannelSetup/defaultReplyTopic/setdata","data": {"newvalue": CMD_REPLY_TOPIC}},
            "MqttStart":{"code": "request", "cid": 1, "adr": "/connections/mqttConnection/status/start"}}
CmdConfigSB={ "Timer1Interval":{"code": "request","cid": 1,"adr": "/timer[1]/interval/setdata","data": {"newvalue": T1_INTERVAL}},
            "CmdStart":{"code": "request", "cid": 1, "adr": "/connections/mqttcommandchannel/status/start"},
            "CmdSetIp":{"code": "request", "cid": 2,"adr": "/connections/mqttcommandchannel/mqttcmdchannel/mqttcmdchannelsetup/brokerip/setdata","data": {"newvalue": BROKER_IP}},
            "CmdSetPort":{"code": "request", "cid": 3,"adr": "/connections/mqttcommandchannel/mqttcmdchannel/mqttcmdchannelsetup/brokerport/setdata","data": {"newvalue": BROKER_PORT}},
            "CmdSetTopic":{"code": "request", "cid": 4,"adr": "/connections/mqttcommandchannel/mqttcmdchannel/mqttcmdchannelsetup/cmdtopic/setdata","data": {"newvalue": CMD_TOPIC}},
            "CmdSetRepTopic":{"code": "request", "cid": 5,"adr": "/connections/mqttcommandchannel/mqttcmdchannel/mqttcmdchannelsetup/defaultreplytopic/setdata","data": {"newvalue": CMD_REPLY_TOPIC}},
            "MqttStart":{"code": "request", "cid": 1, "adr": "/connections/mqttclient/status/start"},
            "CmdStart":{"code": "request", "cid": 1, "adr": "/connections/mqttcommandchannel/status/start"}}

             #"CmdStop":{"code": "request", "cid": 1, "adr": "/connections/mqttcommandchannel/status/stop"},

# -----------------------------------Fielbus configuration-----------------------------------------------

FB_IP=f"192.168.5.130"
FB_HOST_NAME="IOLM"
FB_SUBNET_MASK="255.255.255.0"
FB_DEFAULT_GATEWAY="192.168.5.250"
FieldBusConfig={"fbSetIp":{"code":10,"cid":2,"adr":"/fieldbussetup/network/ipaddress/setdata","data":{"newvalue":FB_IP}},
                "fbSetHostName":{"code": 10,"cid": 1,"adr": "/fieldbussetup/hostname/setdata","data": {"newvalue": FB_HOST_NAME}},
                "fbSetSubnetMask":{"code": "request","cid": 1,"adr": "/fieldbussetup/network/subnetmask/setdata","data": {"newvalue": FB_SUBNET_MASK}},
                "fbSetDefaultGateway":{"code": "request","cid": 1,"adr": "/fieldbussetup/network/ipdefaultgateway/setdata","data": {"newvalue": FB_DEFAULT_GATEWAY}}}

# -----------------------------------IOT configuration-------------------------------------------------------

IOT_IP=f"192.168.5.131"
IOT_SUBNET_MASK="255.255.255.0"
IOT_DEFAULT_GATEWAY="192.168.5.250"
IotConfig={"iotSetIp":{"code":"request","cid":2,"adr":"/iotsetup/network/ipaddress/setdata","data":{"newvalue":IOT_IP}},
            "iotSetSubnetMask":{"code": "request","cid": 1,"adr": "/iotsetup/network/subnetmask/setdata","data": {"newvalue": IOT_SUBNET_MASK}},
            "iotSetDefaultGateway":{"code": "request","cid": 1,"adr": "/iotsetup/network/ipdefaultgateway/setdata","data": {"newvalue": IOT_DEFAULT_GATEWAY}}}

# ----------------------------Iolink master confiigurtatiom------------------------------------

class PortMode(Enum):
    DISABLE = 0
    DI = 1
    DO = 2
    IOLINK =3
portMode=PortMode
# Port mode setings :
PORT_1_MODE=portMode.IOLINK
PORT_2_MODE=portMode.IOLINK
PORT_3_MODE=portMode.IOLINK
PORT_4_MODE=portMode.IOLINK
PORT_5_MODE=portMode.IOLINK
PORT_6_MODE=portMode.DISABLE
PORT_7_MODE=portMode.DISABLE
PORT_8_MODE=portMode.DISABLE
PortModeConfig={"port1SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[1]/mode/setdata","data": {"newvalue": PORT_1_MODE.value}},
                "port2SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[2]/mode/setdata","data": {"newvalue": PORT_2_MODE.value}},
                "port3SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[3]/mode/setdata","data": {"newvalue": PORT_3_MODE.value}},
                "port4SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[4]/mode/setdata","data": {"newvalue": PORT_4_MODE.value}},
                "port5SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[5]/mode/setdata","data": {"newvalue": PORT_5_MODE.value}},
                "port6SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[6]/mode/setdata","data": {"newvalue": PORT_6_MODE.value}},
                "port7SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[7]/mode/setdata","data": {"newvalue": PORT_7_MODE.value}},
                "port8SetMode":{"code": "request","cid": 1,"adr": "/iolinkmaster/port[8]/mode/setdata","data": {"newvalue": PORT_8_MODE.value}}}
Subscribtions={
"subscribeData1":{
  "code":"request",
  "cid":4711,
  "adr":"/timer[1]/counter/datachanged/subscribe",
  "data":{"callback":"mqtt://192.168.5.10:1883/MqttAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1",
    "datatosend":["/iolinkmaster/port[1]/iolinkdevice/pdin","/processdatamaster/temperature"]
  }},
"subscribeData2":{
  "code":"request",
  "cid":4711,
  "adr":"/timer[1]/counter/datachanged/subscribe",
  "data":{"callback":"mqtt://192.168.5.10:1883/MqttAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA2",
    "datatosend":["/iolinkmaster/port[2]/iolinkdevice/pdin","/processdatamaster/temperature"]
  }},
"subscribeData3":{
  "code":"request",
  "cid":4711,
  "adr":"/timer[1]/counter/datachanged/subscribe",
  "data":{"callback":"mqtt://192.168.5.10:1883/MqttAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3",
    "datatosend":["/iolinkmaster/port[3]/iolinkdevice/pdin","/processdatamaster/temperature"]
  }},
"subscribeData4":{
  "code":"request",
  "cid":4711,
  "adr":"/timer[1]/counter/datachanged/subscribe",
  "data":{"callback":"mqtt://192.168.5.10:1883/MqttAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4",
    "datatosend":["/iolinkmaster/port[4]/iolinkdevice/pdin","/processdatamaster/temperature"]
  }}
}
# Subscription  check
SUBSCRIPTION_TOPIC="mqtt://192.168.5.10:1883/MqttAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4" # Existing subscription topic
SUBSCRIPTION_ADR="/timer[1]/counter/datachanged/getsubscriptioninfo"                                                       # Existing subscription adress
GetSubscribeExist={"subscribeCheck":{"code":"request","cid":4711,"adr":SUBSCRIPTION_ADR,"data":{"callback":SUBSCRIPTION_TOPIC}}}


# -------------Konfiguracja mqtt client ---------------------------
client = mqtt.Client()
# Funkcja wywoływana po połączeniu z brokerem
def on_connect(client, userdata, flags, rc):
    print("MQTT BROKER ONLINE, code:", rc)
    client.subscribe(SUBS_TOPIC)
    client.subscribe(CMD_REPLY_TOPIC)

# Funkcja wywoływana po odebraniu wiadomości
def on_message(client, userdata, msg):
    data=msg.payload.decode()
    #print(f"Odebrano wiadomość: {data} z tematu: {msg.topic}")
    daneJason = json.loads(data)        # parsowanie tekstu na JASON !!!!!:)
    try:
        print("Temperature from MQTT:",daneJason['data']['payload']["/processdatamaster/temperature"]['data'])
    except:
        print(daneJason)

def mqttClientConfig():
    try:
        client.connect(BROKER, PORT, 60)
    except:
        print("Broker offline")

client.on_connect = on_connect
client.on_message = on_message
# -------------Excell logging  ---------------------------
def createFile(keyList):

    excel_name = "log_bledow.xlsx"
    excel_file = os.path.join(ex_path, excel_name)

    if not os.path.exists(excel_file):
        wb = Workbook()
        ws = wb.active
        ws.title = "Mqtt test AL1302"
        ws.append(keyList)
        wb.save(excel_file)
        #print(f"[DEBUG] Utworzono plik")

    return excel_file

def log_error(keyList, list):
    now = datetime.now()
    try:

        wb = load_workbook(createFile(keyList))
        ws = wb.active
        listTimeStamp=[now.strftime("%Y-%m-%d") ,now.strftime("%H:%M:%S")]
        listX=listTimeStamp+list
        ws.append(listX)
        wb.save(createFile(keyList))
    except Exception as e:
        print("Błąd zapisu do Excela:", e)

def pingTest(ip):
    print(f"[DEBUG] Pinguje.")
    try:
        resp=ping(ip, count=1, timeout=1, interval=1)
        print("\nCzas odpowiedzi:",resp.rtt_avg_ms)
        return resp.success()
    except:
        print(f"[DEBUG] Ping nie udany.")
        return False

def httpPost(ip,data):
    url = f"http://{ip}"
    if AUTHORIZATION:
        data['auth'] = AUTH
    r = requests.post(url, data=json.dumps(data), verify=False)
    status = r.status_code
    return r.json()

def dictIteamCounter(data):
    counter = 0
    for cx in data.values():
        counter += 1
        if isinstance(cx, dict):
            counter += dictIteamCounter(cx)
    #print("DICT len ", counter)
    return counter


def post(data):
    i = 0
    logData = [0] * len(data)
    if dictIteamCounter(data)>6:        # Check if it is single reqest or multipule request
        for key, path in data.items():  # Multiplle request code:
            dataX=httpPost(ip,path)
            try:
                if 'value' in dataX['data']:                # search "value" key
                    logData[i]=dataX['data'].get('value')   # copy value from dict to loggig data list
                    i+=1
                    print(key,dataX['data'].get('value'))
                else:
                    print("JASON data: ",key, dataX)        # if there is no "value" key print all response
                    i += 1
            except:
                print("JASON data: ",key, dataX)            # Exceptation
                i += 1

    else:                                                   # Single request code part
        dataX = httpPost(ip, data)
        try:
            if 'value' in dataX['data']:
                logData[i] = dataX['data'].get('value')
                i += 1
                print(data, dataX['data'].get('value'))
            else:
                print("JASON data: ",data,"response",dataX)
                i += 1
        except:
            print("JASON data: ",data,"response",dataX)
            i += 1
    return logData

#'YWRtaW4=', 'cGFzc3dvcmQ='

postDone=True
# ---------------------------------------Declare get data HERE:-------------------------------------------------
# Initializing GetData also creates an array of column names of the appropriate size used to create Excell file
GetData = GetProductData | GetAdvancedData | GetPdin | GetPortDeviceProductName | GetPortEvent |GetIolinkEvent  # Add required "Get" dictrionary for HTTP REQUEST
#GetProductData | GetAdvancedData | GetMqttData | GetSubscribeExist | GetPdin | GetProcesParameters | GetPortDeviceProductName | GetPortEvent |GetIolinkEvent| GetPortReadAcyclic

#GetData=GetAdvancedData| GetMqttData | GetSubscribeExist | GetPdin
keyList = [0] * (len(GetData)+3)

start2 = 1
while True:


    if start2:  #pingTest(ip)
        i=0
        print(STALA)
        if postDone :                       # CONFIGURATION CODE PART
            #post(FieldBusConfig)           # Use this command type to set multi request type
            #post(IotConfig)                # Use this command type to set multi request type
            #post(PortModeConfig)            # Use this command type to set multi request type
            #(CmdConfig["CmdReset"])        # Use this command type to individual request type
            #post(CmdConfig)                # Use this command type to set multi request type
            #post(CmdConfigSB)               # use this command to set Solution block command channel
            #post(Subscribtions)
            postDone=False
            mqttClientConfig()
            ix=0
            for key in GetData:             # Key list for logging initializing
                keyList[ix+2] = str(key)
                ix += 1
        # HTTP GET DATA AND LOGGING CODE PART:
        getValue=post(GetData)              # GET DATA command - You can use total dict GetData, or individual GetProductData or GetMqttData with changing GetData declaration
        #print(keyList)
        #print(getValue)
        log_error(keyList,getValue)   #Excell file data logging
        time.sleep(logInterval)     # Main loop interval
        # MQTT CLIENT :
        client.publish(PUB_TOPIC, "Hello MQTT!")                         # MQTT publishing test
        client.publish(CMD_TOPIC, json.dumps(GetProcesParameters['Voltage']))    # MQTT Command channel request via MQTT
        client.loop_read()


    else:
        print(f"[DEBUG] Ping error.")

















