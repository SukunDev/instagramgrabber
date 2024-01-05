from InstagramGrabber import Instagram
from dotenv import load_dotenv
import os


load_dotenv()

username = os.environ.get("IG_USERNAME", None) # ganti dengan instagram username kamu
password = os.environ.get("IG_PASSWORD", None) # ganti dengan instagram password kamu

ig = Instagram(username=username, password=password)

if not os.path.exists(f"./instagram_cookies/{username}_cookies"):
    print("cookies tidak ditemukan")
    try:
        print("mencoba login")
        user = ig.login()
        print(f"berhasil login [{user['username']}]")
    except Exception as e:
        print(str(e))
    print("\n=============\n")


    
user = ig.get_user("hololive.animation")
print(f"user id: {user.user_id}") # ambil user user id
print(f"username: {user.username}") # ambil user username
print(f"full name: {user.full_name}") # ambil user full name
print(f"category name: {user.category_name}") # ambil user category name
print(f"biography: {user.biography}") # ambil user biography
print(f"jumlah following: {user.following}") # ambil user jumlah following
print(f"jumlah followers: {user.followers}") # ambil user jumlah followers
print(f"jumlah posts: {user.posts_count}") # ambil user jumlah posts
print(f"profile picture: {user.profile_picture}") # ambil user profile picture