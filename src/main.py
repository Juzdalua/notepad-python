from dotenv import load_dotenv
import os
from utils.socket import connect_to_server, send_message, disconnect_from_server

load_dotenv()
server_url = "http://localhost:5000"

print("Hello ")
print(f"HI -> {os.getenv('HI')}")

connect_to_server(server_url)

# 서버에 메시지 보내기
send_message("안녕하세요, 서버!")

# 서버와 연결 종료
disconnect_from_server()