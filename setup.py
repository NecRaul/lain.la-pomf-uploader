from setuptools import find_packages, setup

VERSION = "1.15"
DESCRIPTION = "pomf.lain.la uploader."
with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
AUTHOR = "NecRaul"
AUTHOR_EMAIL = "necraul@kuroneko.dev"

setup(
    name="lain_upload",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    keywords=[
        "python",
        "uploader",
        "pomf",
        "lain",
        "lain.la",
        "pomf.lain.la",
        "kuroneko",
    ],
    url="https://github.com/NecRaul/lain.la-pomf-uploader",
    project_urls={
        "Documentation": "https://github.com/NecRaul/lain.la-pomf-uploader#readme",
        "Source": "https://github.com/NecRaul/lain.la-pomf-uploader",
        "Issues": "https://github.com/NecRaul/lain.la-pomf-uploader/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
    py_modules=["upload"],
    entry_points={
        "console_scripts": [
            "lain-upload = lain_upload:main",
        ],
    },
)
