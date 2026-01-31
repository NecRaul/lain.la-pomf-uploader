# lain.la-pomf-uploader

`pomf.lain.la` uploader.

## Installation

### Via PyPI (Recommended)

You have the option to choose between the standard version (lain-upload) or the desktop version (lain-upload[clipboard]), which adds clipboard support for auto-copying links.

> [!NOTE]
> For brevity, the examples below use the desktop version.

#### With pip (Basic)

```sh
pip install "lain-upload[clipboard]"
```

#### With pipx (Isolated)

```sh
pipx install "lain-upload[clipboard]"
```

#### With uv (Best)

The most efficient way to install or run the uploader.

```sh
# Permanent isolated installation
uv tool install "lain-upload[clipboard]"

# Run once without installing
uvx --with "lain-upload[clipboard]" lain-upload <file1> <file2> <file3>

# Run in scripts or ad-hoc environments
uv run --with "lain-upload[clipboard]" lain-upload <file1> <file2> <file3>
```

### From Source (Development)

```sh
# Clone the repository and navigate to it
git clone git@github.com:NecRaul/lain.la-pomf-uploader.git
cd lain.la-pomf-uploader

# Install environment and all development dependencies (mandatory and optional)
uv sync --dev

# Install pre-commit hook
uv run pre-commit install

# Optional: Run all linters and type checkers manually
uv run pre-commit run --all-files

# Run the local version
uv run lain-upload <file1> <file2> <file3>
```

## Usage

Simply provide the path to the file or files you wish to upload.

```sh
# Upload a file
lain-upload kuroneko.png

# Upload files from different directories
lain-upload /path/to/kuroneko.png /path/to/another/directory/shirone.png yamineko.png ../kamineko.png

# Upload files with the -p/--progress flag
lain-upload -p big-file

# Display help with the -h/--help flag
lain-upload -h

# Display version with the -v/--version flag
lain-upload -v
```

## Dependencies

* [requests](https://github.com/psf/requests): send the API request for uploading.
* [requests-toolbelt](https://github.com/requests/toolbelt): enable memory-efficient streaming and progress tracking for large uploads.

### Optional

* [pyperclip](https://github.com/asweigart/pyperclip): copy the uploaded files' URLs to the clipboard.

## How it works

The `pomf.lain.la` service allows uploading files via a multipart `POST` request.

This tool automates the process and adds safety checks.

### The Manual Way

```sh
curl -F "files[]=@kuroneko.png" https://pomf.lain.la/upload.php
```

### The lain-upload way

* Batch Processing: Upload multiple files in a single command execution, saving time over individual manual requests.
* Validation: Checks the file size before uploading to ensure it is below the `1GiB` limit.
* API Request: Sends the multipart `POST` request via `requests` and `requests-toolbelt`, provides progress bar with the `-p/--progress` flag.
* Normalization: Parses the server response to provide clean links from `pomf.lain.la` or `pomf2.lain.la`.
* Clipboard (Optional): If `pyperclip` is installed, the result is instantly copied to your clipboard.
