from distutils.core import setup
import os.path
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("./InstagramGrabber/version.py") as fp:
    exec(fp.read())

setuptools.setup(
    name="InstagramGrabber",
    packages=["InstagramGrabber", "InstagramGrabber.post", "InstagramGrabber.user"],
    package_data={"": ["LICENSE"],},
    version=__version__,
    license="The Unlicense (Unlicense)",
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
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    include_package_data=True,
    python_requires=">=3.7",
)