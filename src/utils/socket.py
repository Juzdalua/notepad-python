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
def message(data):
    print(f"[RECV]: {data}")

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

def echo_on_event(event_key: str):
    @sio.on(event_key)
    def handle_message(data):
        print(f"📥 받은 메시지 [{event_key}]: {data}")
        sio.emit(event_key, data)
        print(f"📤 에코 응답 전송 [{event_key}]: {data}")

def connect_to_server(url: str):
    try:
        sio.connect(url)
        print(f"{url}에 연결되었습니다.")
        return True
    except Exception as e:
        print(f"연결 실패: {e}")
        return False

def disconnect_from_server():
    sio.disconnect()
    print("서버와 연결이 종료되었습니다.")
