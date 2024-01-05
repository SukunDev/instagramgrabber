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

username = "username instagram kalian"
password = "password instgaram kalian"

ig = Instagram(username=username, password=password)
account = ig.login()
print(account['username'])
```

### Get Post

Ambil link post instagram yang kalian inginkan, Kalian bisa menggunakan url **Post** atau **Reel**

```python
from InstagramGrabber import Instagram

username = "username instagram kalian"
password = "password instgaram kalian"

ig = Instagram(username=username, password=password)

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

print(post.media) # ambil post info
```

### Get User

Ambil username instagram target dan jalankan program ini

```python
from InstagramGrabber import Instagram

username = "username instagram kalian"
password = "password instgaram kalian"

ig = Instagram(username=username, password=password)
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

username = "username instagram kalian"
password = "password instgaram kalian"

ig = Instagram(username=username, password=password)
user = ig.get_user("hololive.animation")

max_id = None
more_available = True
while more_available:
    posts = user.get_post(max_id=max_id)
    max_id = posts.max_id
    more_available = posts.more_available
    print(f"Next max_id: {max_id}")
    print(f"More Available: {more_available}")
    print(posts.media.prettify(indent=2))
```

### Get All User Reels

Ambil username instagram target dan jalankan program ini

```python
from InstagramGrabber import Instagram

username = "username instagram kalian"
password = "password instgaram kalian"

ig = Instagram(username=username, password=password)
user = ig.get_user("hololive.animation")

max_id = None
more_available = True
while more_available:
    reels = user.get_reel(max_id=max_id)
    max_id = reels.max_id
    more_available = reels.more_available
    print(f"Next max_id: {max_id}")
    print(f"More Available: {more_available}")
    print(reels.media.prettify(indent=2))
```

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, kami sangat menghargai setiap bentuk dukungan. Silakan buka [Panduan Kontribusi](CONTRIBUTING.md) untuk informasi lebih lanjut.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

Dikembangkan oleh [SukunDev](https://github.com/SukunDev)
