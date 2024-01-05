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

post = ig.get_post(url="https://www.instagram.com/p/C0oC-bchkjw")
print(f"user id: {post.user.user_id}") # ambil user user id
print(f"username: {post.user.username}") # ambil user username
print(f"full name: {post.user.full_name}") # ambil user full name
print(f"category name: {post.user.category_name}") # ambil user category name
print(f"biography: {post.user.biography}") # ambil user biography
print(f"jumlah following: {post.user.following}") # ambil user jumlah following
print(f"jumlah followers: {post.user.followers}") # ambil user jumlah followers
print(f"jumlah posts: {post.user.posts_count}") # ambil user jumlah posts
print(f"profile picture: {post.user.profile_picture}") # ambil user profile picture

if post.media: # check media ada atau tidak
    print(post.media.prettify(indent=2)) # ambil post info