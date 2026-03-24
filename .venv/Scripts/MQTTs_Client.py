import paho.mqtt.client as mqtt
import time
import sys
import json
BROKER_HOST = "192.168.5.10"
BROKER_PORT = 8883  # typowy port TLS

CA_CERT = "certs/CA.crt"
CLIENT_CERT = "certs/MqttExplorer.crt"
CLIENT_KEY = "certs/MqttExplorerKey.pem"

TOPIC1 = "pdin12"
TOPIC2 = "pdin34"
TOPIC3 = "pdin56"
TOPIC4 = "pdin78"
TOPIC5 = "balluff/iolink/devices/master1port1/databytes/fromdevice"
TOPIC6 = "balluff/iolink/devices/master1port2/databytes/fromdevice"
TOPIC7 = "balluff/iolink/devices/master1port3/databytes/fromdevice"
TOPIC8 = "balluff/iolink/devices/master1port4/databytes/fromdevice"
TOPIC9 = "balluff/iolink/devices/master1port5/databytes/fromdevice"
TOPIC10 = "balluff/iolink/devices/master1port6/databytes/fromdevice"
TOPIC11 = "balluff/iolink/devices/master1port7/databytes/fromdevice"
TOPIC12 = "balluff/iolink/devices/master1port8/databytes/fromdevice"
TOPIC13 = "MirrorTlsPort"
TOPIC14 = "NodeRed_Counter_1"
TOPIC15 = "Node_Red_Bridge"

start_time=0
elapsed_time=0
subscriptionCounter=0
notification_interval=0
notification_time=0
def on_connect(client, userdata, flags, rc):
    print("Połączono z kodem:", rc)
    client.subscribe(TOPIC1)
    client.subscribe(TOPIC2)
    client.subscribe(TOPIC3)
    client.subscribe(TOPIC4)
    client.subscribe(TOPIC5)
    client.subscribe(TOPIC6)
    client.subscribe(TOPIC7)
    client.subscribe(TOPIC8)
    client.subscribe(TOPIC9)
    client.subscribe(TOPIC10)
    client.subscribe(TOPIC11)
    client.subscribe(TOPIC12)
    client.subscribe(TOPIC13)
    client.subscribe(TOPIC14)
    client.subscribe(TOPIC15)

def on_message(client, userdata, msg):

    global start_time,elapsed_time,subscriptionCounter,notification_time,notification_interval
    notification_interval=time.time()-notification_time
    notification_time=time.time()

    if start_time==0:
        start_time = time.time()
    elapsed_time = time.time() - start_time
    if elapsed_time>600.0:
        print("   Odebrano subs:",subscriptionCounter)
        start_time=0
        sys.exit("Zakończono program")

    subscriptionCounter=subscriptionCounter+1
    data = json.loads(msg.payload.decode())
    counterNumber=0
    try:
        for itm,value in data['data']['payload'].items():
            try:
               # print(f"Counter {counterNumber} value:",value['data'],"|  Time stamp:", value['timestamp'])
                counterNumber = counterNumber + 1
            except:
                print(data['data']['payload'])

    except:
        # print(data['data']['payload'])
        print(data)

    #print(f"  Odebrano: {msg.topic} -> {msg.payload.decode()}")
    try:
        print("Elapsed time1:",elapsed_time,"Notification timer:",notification_interval,f"  DATA: {data['data']}")
        print("---")
    except:
        print("Elapsed time2:", elapsed_time, "Notification timer:", notification_interval, f"  DATA: {data}")
    msgx=msg.payload.decode()

client = mqtt.Client()

# Uwierzytelnianie certyfikatem klienta
client.tls_set(
    ca_certs=CA_CERT,
   certfile=CLIENT_CERT,
    keyfile=CLIENT_KEY
)

# Opcjonalnie wymuszenie weryfikacji certyfikatu brokera
client.tls_insecure_set(False)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_HOST, BROKER_PORT)
client.loop_forever()