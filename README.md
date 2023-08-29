# lain.la-pomf-uploader

pomf.lain.la uploader.

## Requirements

`requests` is used upload the file.

`pyperclip` is used to copy link to the clipboard.

`setuptools` is used to build the script.

If you want to build this on your own, you can install the requirements with

```Python
pip install -r requirements.txt
```

or install the package by running

```Python
pip install lain-upload
```

Python's native `os` and `argparse` packages are used to check for file size and parse return request along with set command argument respectively.

## How it works

Files below the file size 1GB can be uploaded to `pomf.lain.la` and `pomf2.lain.la` making necessary API calls to `https://pomf.lain.la/upload.php` endpoint.

I just wrapped it inside said API calls inside Python and added validation to check for size. Links are printed on the terminal and copied to clipboard for ease of use.

You can run the script with

```Python
lain-upload <file-path>
```

You can not upload files bigger than 1 gigabyte.
