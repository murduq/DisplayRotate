import network
import utime
import urequests

### Station Mode
#wifi = network.WLAN(network.STA_IF)
#wifi.active(True)
#while not wifi.isconnected():
#    print('connecting...')
#    wifi.connect('Verizon_773VVX','cub7-put-argo')
#    utime.sleep(1)
#print('connected')
#print(wifi.ifconfig())

def find_server(ip, port):
    waiting = True
    while waiting:
        try:
            response = urequests.request('POST', f"http://{ip}:{port}", data="land")
            waiting = False
        except OSError:
            print('waiting for server...')
            continue
    
def do_a_barrell_roll(times):   
    for i in range(times):
        response = urequests.request('POST', "http://192.168.1.168:8000", data="port")
        utime.sleep(1.5)
        response = urequests.request('POST', "http://192.168.1.168:8000", data="land flip")
        utime.sleep(1.5)
        response = urequests.request('POST', "http://192.168.1.168:8000", data="port flip")
        utime.sleep(1.5)
        response = urequests.request('POST', "http://192.168.1.168:8000", data="land")
        
def set_orient(ip, port, orient:str):
    response = urequests.request('POST', f"http://{str(ip)}:{str(port)}", data=f"{orient}")
    utime.sleep(2)
        