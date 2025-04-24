import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected ✅")

@sio.event
def message(data):
    print(f"[RECV]: {data}")

@sio.event
def disconnect():
    print("Disconnected ❌")

def send_message(eventKey: str, message: str):
    sio.emit(eventKey, message)

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
