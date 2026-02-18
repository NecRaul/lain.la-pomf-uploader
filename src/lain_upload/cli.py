import argparse
import sys
from pathlib import Path

import requests

from . import uploader
from .version import __version__


def main():
    allowed_hosts = {
        "catbox": {"class": "Catbox", "options": {}},
        "litterbox": {"class": "Litterbox", "options": {}},
        "pomf": {"class": "Pomf", "options": {}},
        "uguu": {"class": None, "options": {}},
    }
    deprecated_hosts = {
        "pomf": "pomf is no longer supported.\nSee: https://infrablog.lain.la/pomf-announcement",
    }
    parser = argparse.ArgumentParser(
        description="Upload file to pomf.lain.la",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Example: %(prog)s -p file1.txt file2.jpg file3.webm",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "--host",
        nargs="?",
        default="catbox",
        choices=allowed_hosts.keys(),
        help="host to use for uploading",
    )
    parser.add_argument("file_paths", nargs="+", help="File path(s)")

    args = parser.parse_args()

    if args.host in deprecated_hosts:
        parser.error(deprecated_hosts[args.host])

    host_info = allowed_hosts[args.host]

    if not host_info or host_info["class"] is None:
        parser.error(f"Host {args.host} is not supported.")

    host_class_name = f"{host_info['class']}Uploader"
    if isinstance(host_class_name, str):
        host_class = getattr(uploader, host_class_name)
    else:
        parser.error(f"Uploader class for host {args.host} is invalid.")

    uploaded_urls = []
    has_error = False

    for file_path_str in args.file_paths:
        try:
            file_path = Path(file_path_str)
            uploader_instance = host_class(file_path)
            url = uploader_instance.upload()
            print(f"{file_path.name}: {url}")
            uploaded_urls.append(url)
        except FileNotFoundError as e:
            print(f"File not found: {e}", file=sys.stderr)
            has_error = True
            continue
        except ValueError as e:
            print(f"Value Error: {e}", file=sys.stderr)
            has_error = True
            continue
        except requests.RequestException as e:
            print(f"Network error: {e}", file=sys.stderr)
            has_error = True
            continue
        except (KeyError, IndexError, TypeError) as e:
            print(f"Unexpected server response: {e}", file=sys.stderr)
            has_error = True
            continue

    if uploaded_urls:
        all_urls = "\n".join(uploaded_urls)
        try:
            import pyperclip

            pyperclip.copy(all_urls)
            print("\nURL(s) copied to clipboard", file=sys.stderr)
        except Exception:
            pass

    if has_error:
        sys.exit(1)
