# lain.la-pomf-uploader

`pomf.lain.la` uploader.

## Installation

### Via PyPI (Recommended)

```sh
# Basic installation
pip install lain-upload

# With clipboard support (recommended for desktop)
pip install lain-upload[clipboard]
```

### From Source (Development)

```sh
git clone git@github.com:NecRaul/lain.la-pomf-uploader.git
cd lain.la-pomf-uploader
# You can skip the next two commands
# for installing it globally
python -m venv .venv
source .venv/bin/activate
pip install -e .[clipboard,dev,build]
```

## Usage

Simply provide the path to the file you wish to upload.

```sh
# Upload a file
lain-upload kuroneko.png

# Upload a file from a different directory
lain-upload /path/to/kuroneko.png
```

## Dependencies

* [requests](https://github.com/psf/requests): send the API request for uploading.

### Optional

* [pyperclip](https://github.com/asweigart/pyperclip): copy the uploaded file URL to the clipboard.

## How it works

The `pomf.lain.la` service allows uploading files via a multipart `POST` request.

This tool automates the process and adds safety checks.

### The Manual Way

```sh
curl -F "files[]=@kuroneko.png" https://pomf.lain.la/upload.php
```

### The lain-upload way

* Validation: Checks the file size before uploading to ensure it is below the `1GiB` limit.
* API Request: Sends the multipart `POST` request via `requests`.
* Normalization: Parses the server response to provide clean links from `pomf.lain.la` or `pomf2.lain.la`.
* Clipboard (Optional): If `pyperclip` is installed, the result is instantly copied to your clipboard.
