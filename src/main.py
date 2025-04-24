import threading
from dotenv import load_dotenv
from utils.socket import keep_reconnecting

load_dotenv()

t = threading.Thread(target=keep_reconnecting)
t.daemon = True
t.start()



t.join()
