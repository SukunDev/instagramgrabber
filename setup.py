from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("./InstagramGrabber/version.py") as fp:
    exec(fp.read())

setuptools.setup(
    name="InstagramGrabber",
    packages=setuptools.find_packages(),
    version=__version__,
    license="MIT",
    description="Simple project to grab instagram info",
    author="SukunDev",
    author_email="sukundev32@gmail.com",
    url="https://github.com/sukundev/instagramgrabber",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["instagram", "instagram-grabber", "instagram grabber", "python3", "api", "instagram api"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
)