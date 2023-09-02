from setuptools import setup, find_packages

VERSION = "1.4"
DESCRIPTION = "pomf.lain.la uploader."
with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
AUTHOR = "NecRaul"

setup(
    name="lain_upload",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    packages=find_packages(),
    install_requires=["requests", "pyperclip"],
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