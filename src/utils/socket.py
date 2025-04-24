import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("서버와 연결되었습니다.")

@sio.event
def message(data):
    print(f"서버로부터 받은 메시지: {data}")

@sio.event
def disconnect():
    print("서버와 연결이 끊어졌습니다.")

def send_message(message: str):
    sio.emit("message", message)

def connect_to_server(url: str):
    sio.connect(url)
    print(f"{url}에 연결되었습니다.")

def disconnect_from_server():
    sio.disconnect()
    print("서버와 연결이 종료되었습니다.")
