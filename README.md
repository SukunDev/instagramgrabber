# InstagramGrabber

InstagramGrabber adalah modul Python yang memungkinkan pengembang mengakses dan mengambil data dari Instagram. Dengan fungsionalitas seperti mengunduh gambar, video, dan informasi profil pengguna, modul ini menyediakan solusi efektif untuk integrasi Instagram dalam proyek tanpa perlu mengakses API resmi. Memudahkan ekstraksi data, InstagramGrabber cocok untuk berbagai aplikasi dan skenario pengembangan perangkat lunak.

---

## Fiture

- **Instagram Post Grabber**: mengambil semua informasi tentang postingan
- **Instagram User Grabber**: mengambil semua informasi tentang user
- **Instagram User Posts Grabber**: mengambil semua informasi tentang posts user
- **Instagram User Reels Grabber**: mengambil semua informasi tentang reels user
- **Instagram User Stories Grabber**: mengambil semua informasi tentang stories user

## Installation

### Using Git

```bash
git clone https://github.com/SukunDev/instagramgrabber.git
cd instagramgrabber
python -m setup.py install
```

### Using PIP

```bash
pip install InstagramGrabber
```

## Usage

### Login

Login dulu sebelum pakai modul ini. Ambil cookies untuk aktivitas lebih lanjut.

```python
from InstagramGrabber import Instagram
from dotenv import load_dotenv
import os


load_dotenv()

username = os.environ.get("IG_USERNAME", None) # ganti dengan instagram username kamu
password = os.environ.get("IG_PASSWORD", None) # ganti dengan instagram password kamu

ig = Instagram(username=username, password=password)
account = ig.login()
print(account['username']) # ini akan mengambil username instagram kamu jika sudah selesai
```

### Get Post

Ambil link post instagram yang kalian inginkan, Kalian bisa menggunakan url **Post** atau **Reel**

```python
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
```

### Get User

Ambil username instagram target dan jalankan program ini

```python
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
```

### Get All User Posts

Ambil username instagram target dan jalankan program ini

```python
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

max_id = None
more_available = True
while more_available:
    posts = user.get_post(max_id=max_id)
    max_id = posts.max_id
    more_available = posts.more_available
    print(f"Next max_id: {max_id}")
    print(f"More Available: {more_available}")
    if posts.media: # check media ada atau tidak
        print(posts.media.prettify(indent=2))

```

### Get All User Reels

Ambil username instagram target dan jalankan program ini

```python
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

max_id = None
more_available = True
while more_available:
    reels = user.get_reel(max_id=max_id)
    max_id = reels.max_id
    more_available = reels.more_available
    print(f"Next max_id: {max_id}")
    print(f"More Available: {more_available}")
    if reels.media: # check media ada atau tidak
        print(reels.media.prettify(indent=2))
```

### Get All User Stories

Ambil username instagram target dan jalankan program ini

```python
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

stories = user.get_stories()
if stories.media: # check media ada atau tidak
    print(stories.media.prettify(indent=2))
```

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, kami sangat menghargai setiap bentuk dukungan. Silakan buka [Panduan Kontribusi](CONTRIBUTING.md) untuk informasi lebih lanjut.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

Dikembangkan oleh [SukunDev](https://github.com/SukunDev)
