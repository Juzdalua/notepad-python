from dotenv import load_dotenv
import os
import time

from utils.socket import connect_to_server, send_loop, send_message, disconnect_from_server

load_dotenv()
server_url = "http://localhost:6001"
connectFlag = False

try:
    while connectFlag == False:
      connectFlag = connect_to_server(server_url)
except:
    print("Can't connect server")

send_loop()