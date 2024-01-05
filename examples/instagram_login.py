from InstagramGrabber import Instagram
from dotenv import load_dotenv
import os


load_dotenv()

username = os.environ.get("IG_USERNAME", None) # ganti dengan instagram username kamu
password = os.environ.get("IG_PASSWORD", None) # ganti dengan instagram password kamu

ig = Instagram(username=username, password=password)
account = ig.login()
print(account['username']) # ini akan mengambil username instagram kamu jika sudah selesai