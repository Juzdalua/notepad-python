from dotenv import load_dotenv
import os
import time

from utils.socket import connect_to_server, send_message, disconnect_from_server

load_dotenv()
server_url = "http://localhost:6001"
connectFlag = False

try:
    while connectFlag == False:
      connectFlag = connect_to_server(server_url)
except:
    print("Can't connect server")

try:
    while connectFlag == True:
        send_message("message", "안녕하세요, 서버!")
        time.sleep(1)
except KeyboardInterrupt:
    disconnect_from_server()
    connectFlag = False
    print("Close socket")