import os
import socketio
import time
from dotenv import load_dotenv

sio = socketio.Client()
connectFlag = False

load_dotenv()
url = os.getenv('SERVER_URL')
port = os.getenv('SERVER_PORT')
server_url = f"{url}:{port}"

@sio.event
def connect():
  global connectFlag
  connectFlag = True
  register()
  print("Connected ✅")

@sio.event
def ping(data):
  print(f"[RECV]: {data}")
  sio.emit('pong','pong')
  print('[SEND] pong')

@sio.event
def disconnect():
  global connectFlag
  connectFlag = False
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

def register():
  sio.emit('register', {'clientType': 'etc'})

def keep_reconnecting():
    global connectFlag, server_url
    while True:
      if not connectFlag:
        print("Reconnecting...")
        try:
          connectFlag = connect_to_server(server_url)
        except Exception as e:
            print(f"[❌ 재연결 실패]: {e}")
      time.sleep(2)
