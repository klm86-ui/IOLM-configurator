import requests
import time
import json

# CONFIGURATION
ip = "192.168.5.151"   # IP
DEVICE_PORT = 1                            #  IO-Link port
AUTHORIZATION=True                # Authorization enable ( Solution Block)
AUTH={"user":"YWRtaW4=","passwd":"cGFzc3dvcmQ="}    # User and password i ut8
BLOB_INDEX_CONTROL = 49
BLOB_INDEX_DATA = 50
SYSTEM_COMAND_INDEX=2
START_RECORD_RAW='D4'
BlobStartCommand= {"index": 50,"subindex": 0,"value": "F1F000"}
BlobReadIndex49={"index":BLOB_INDEX_CONTROL,"subindex": 0}
BlobConf1=  {"index":BLOB_INDEX_CONTROL,"subindex": 0}
BlobTrigerSource=  {"index":8017,"subindex":1,"value":"01"}
BlobReadCurentNumber=  {"index":BLOB_INDEX_CONTROL,"subindex": 0}
BlobSystemComand= {"index":2,"subindex":0,"value":START_RECORD_RAW}
BlobReadData= {"index":BLOB_INDEX_DATA,"subindex": 0}
ReadAcyclicCode= {"code": "request","cid": 1,"adr": "/iolinkmaster/port[8]/iolinkdevice/iolreadacyclic"}
WriteAcyclicCode= {"code":10,"cid":80,"adr": "/iolinkmaster/port[8]/iolinkdevice/iolwriteacyclic"}
ReadPdinPort1={"code": "request","cid":80,"adr": "/iolinkmaster/port[1]/iolinkdevice/pdin/getdata"}
VENDOR_NAME=16
MirrorReadAcyclic={"code": "request","cid":80,"adr": "/remote/IOLM_AL1422_1/iolinkmaster/port[1]/iolinkdevice/iolreadacyclic"}
MirrorPdinPort1={"code": "request","cid":80,"adr": "/remote/IOLM_AL1422_1/iolinkmaster/port[1]/iolinkdevice/pdin/getdata"}
MirrorIndexData={"index":VENDOR_NAME,"subindex": 0}
# Statystyki
packets_sent = 0
packets_received = 0
response_errors = 0
http_sent=0
http_recived=0
http_error=0
mirror_sent=0
mirror_recived=0
mirror_error=0

def httpPost(ip,req,data):
    url = f"http://{ip}"
    req['data']=data

    if AUTHORIZATION:
        req['auth'] = AUTH
    #print(req)
    r = requests.post(url, data=json.dumps(req), verify=False, timeout=100)
    status = r.status_code
    return r.json()
def BlobConf():
   # r = httpPost(ip, WriteAcyclicCode, BlobTrigerSource)
   # print(r)
    r=httpPost(ip, WriteAcyclicCode, BlobSystemComand)
    print(r)
    r=httpPost(ip,ReadAcyclicCode,BlobConf1)
    print(r)
    r = httpPost(ip, WriteAcyclicCode, BlobStartCommand)
    print(r)
    r = httpPost(ip, MirrorReadAcyclic, MirrorIndexData)
    print(r)
    r = httpPost(ip, MirrorPdinPort1, "")
    print(r)


def read_blob():
    global packets_sent, packets_received, response_errors
    # 2. Odczyt danych blob (indeks 50) przez POST

    start = time.time()
    packets_sent += 1
    try:
        response = httpPost(ip,ReadAcyclicCode,BlobReadData)
        elapsed = time.time() - start
        packets_received += 1

        if response['code'] == 200:
            blob_data = response['data']
            first_two = blob_data['value'][:2]

            if first_two == '20':
                print("New segment")
            if first_two == '30':
                print("Reading finished")

            print(f"[OK] Data uploaded in {elapsed:.3f}s, size: {len(blob_data.get('value'))} bytes:, 'data:{blob_data}")
            return blob_data
        else:
            print(f"[ERROR] Status code: {response['code']}, time: {elapsed:.3f}s, MSG: {response['data']}")
            response_errors += 1
            return None
    except Exception as e:
        print(f"[ERROR] Request error: {e},'data:{response}")
        return None
def blob_test():
    while True:
        blob = read_blob()
        time.sleep(0.5)
        try:
            first_two = blob['value'][:2]
            if first_two == '30':
                print("Data reading finished")
                break
            if first_two == '40':
                print("Data reading finished")
                break
        except:
            print("MSG")
        #time.sleep(1.6)
    print("\n--- Summary---")
    print(f"Packets send: {packets_sent}")
    print(f"Packets recived: {packets_received}")
    print(f"Status: {'OK' if blob else 'error'}")
    print(f"Resonse errors: {response_errors}")

def http_test():
    global http_sent, http_recived, http_error
    start = time.time()
    http_sent +=1
    r = httpPost(ip, ReadAcyclicCode, MirrorIndexData)
    elapsed = time.time() - start
    if r['code'] == 200:
       http_recived += 1
    else:
        http_error += 1
        print(f"ERROR: {r['code']},{r['data']}")
    print(f"HTTP test acyclic:{r['data'].get('value')}; packets sent {http_sent}, recived {http_recived}; time: {elapsed}")
    http_sent += 1
    start = time.time()
    r = httpPost(ip, ReadPdinPort1, "")
    elapsed = time.time() - start
    if r['code'] == 200:
       http_recived += 1
    else:
        http_error += 1
        print(f"ERROR: {r['code']},{r['data']}")
    print(f"HTTP test pdin:{r['data'].get('value')}; packets sent {http_sent}, recived {http_recived}; time: {elapsed}")
    return http_sent, http_recived, http_error
def mirror_test():
    global mirror_sent, mirror_recived, mirror_error
    mirror_sent += 1
    start = time.time()
    r = httpPost(ip, MirrorReadAcyclic, MirrorIndexData)
    elapsed = time.time() - start
    if r['code'] == 200:
       mirror_recived += 1
    else:
        mirror_error += 1
        print(f"ERROR: {r['code']},{r['data']}")
    print(f"Mirror test acyclic:{r['data'].get('value')}, packets sent {mirror_sent}, recived {mirror_recived}; time: {elapsed}")
    mirror_sent += 1
    start = time.time()
    r = httpPost(ip, MirrorPdinPort1, "")
    elapsed = time.time() - start
    print(f"Mirror test pdin:{r['data'].get('value')} packets sent {mirror_sent}, recived {mirror_recived}; time: {elapsed}")
    if r['code'] == 200:
        mirror_recived += 1
    else:
        mirror_error += 1
        print(f"ERROR: {r['code']},{r['data']}")
    return mirror_sent, mirror_recived, mirror_error
BlobConf()
time.sleep(1)
if __name__ == "__main__":
    blob_test()
    for x in range(30000):
        http_test()
        mirror_test()
        #time.sleep(1)

    print(f" Http test result : sent: {http_sent}, recived: {http_recived}, errors: {http_error}")
    print(f" Mirror test result : sent: {mirror_sent}, recived: {mirror_recived}, errors: {mirror_error}")





