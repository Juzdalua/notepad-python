from dotenv import load_dotenv
import os
import time

from utils.socket import connect_to_server, ping, send_loop, send_message, disconnect_from_server

load_dotenv()
server_url = "http://localhost:6001"
connectFlag = False

try:
    while True:
      if connectFlag == False:
        connectFlag = connect_to_server(server_url)
      else:
         pass
except Exception as e:
    print(f"연결 실패: {e}")

# send_loop()
