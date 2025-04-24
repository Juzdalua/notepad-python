import socketio
import time

sio = socketio.Client()
connectFlag = False

@sio.event
def connect():
    global connectFlag
    connectFlag = True
    print("Connected ✅")

@sio.event
def ping(data):
    print(f"[RECV]: {data}")
    sio.emit('pong','pong')

@sio.event
def disconnect():
    global connectFlag
    connectFlag = False
    print("Disconnected ❌")

def send_message(eventKey: str, message: str):
    sio.emit(eventKey, message)

def send_loop():
    global connectFlag
    try:
      while connectFlag == True:
          send_message("message", "안녕하세요, 서버!")
          time.sleep(1)
    except KeyboardInterrupt:
        disconnect_from_server()
        connectFlag = False
        print("Close socket")

def connect_to_server(url: str):
    try:
        sio.connect(url)
        print(f"{url}에 연결되었습니다.")
        register()
        return True
    except Exception as e:
        print(f"연결 실패: {e}")
        return False

def register():
    sio.emit('register', {'clientType': 'etc'})

def disconnect_from_server():
    sio.disconnect()
    print("서버와 연결이 종료되었습니다.")

def keep_reconnecting(url: str):
    while not connectFlag:
        print("Reconnecting...")
        time.sleep(5)
        connectFlag = connect_to_server(url)
