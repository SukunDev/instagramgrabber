from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="InstagramGrabber",
    packages=setuptools.find_packages(),
    version="1.0.0",
    license="MIT",
    description="Simple project to grab instagram info",
    author="SukunDev",
    author_email="sukundev32@gmail.com",
    url="https://github.com/sukundev/instagramgrabber",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["instagram", "instagram-grabber", "instagram grabber", "python3", "api", "instagram api"],
    install_requires=["requests"],
    python_requires=">=3.7",
)