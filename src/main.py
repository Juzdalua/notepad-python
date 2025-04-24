import threading
from utils.socket import keep_reconnecting

t = threading.Thread(target=keep_reconnecting)
t.daemon = True
t.start()



t.join()
