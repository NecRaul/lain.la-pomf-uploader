# lain.la-pomf-uploader

pomf.lain.la uploader.

## Requirements

`requests` is used to upload the file.

`pyperclip` is used to copy the link to the clipboard.

If you want to build this on your own, you can install the requirements with

```Python
pip install -r requirements.txt
```

or install the package by running

```Python
pip install lain-upload
```

Python's native `os` (used to check for file size), `argparse` (parse return request and set command argument) and `setuptools` (used to build the script) packages are also used.

## How it works

Files below the file size 1GB can be uploaded to `pomf.lain.la` and `pomf2.lain.la` making necessary API calls to `https://pomf.lain.la/upload.php` endpoint.

I just wrapped it inside said API calls inside Python and added validation to check for size. Links are printed on the terminal and copied to clipboard for ease of use.

You can run the script with

```Python
lain-upload <file-path>
```

You can not upload files bigger than 1 gigabyte.
