from setuptools import setup, find_packages

VERSION = "1.0"
DESCRIPTION = "pomf.lain.la uploader."
LONG_DESCRIPTION = "Uploading files to pomf.lain.la using a python interface."
AUTHOR = "NecRaul"

setup(
    name="lain_upload",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=["requests", "pyperclip", "setuptools"],
    keywords=["python", "uploader", "pomf", "lain", "lain.la", "pomf.lain.la"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP"
    ],
    py_modules=["upload"],
    entry_points={
        "console_scripts": [
            "lain-upload = lain_upload.__init__:main",
        ],
    },
)