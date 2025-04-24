from dotenv import load_dotenv
import os

load_dotenv()

print("Hello ")
print(f"HI -> {os.getenv('HI')}")