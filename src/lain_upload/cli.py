import argparse
import sys

import requests

from .progress import ProgressHandler
from .upload import upload_file
from .version import __version__


def main():
    parser = argparse.ArgumentParser(
        description="Upload file to pomf.lain.la",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Example: %(prog)s -p file1.txt file2.jpg file3.webm",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument(
        "-p", "--progress", action="store_true", help="show upload progress bar"
    )
    parser.add_argument("file_paths", nargs="+", help="File path(s)")

    args = parser.parse_args()

    uploaded_urls = []
    has_error = False

    for file_path_str in args.file_paths:
        progress_handler = ProgressHandler()
        progress_callback = progress_handler.update if args.progress else None
        try:
            response = upload_file(file_path_str, progress_callback)
            url = response["files"][0]["url"]
            print(f"File URL: {url}\n")
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
            print("\nURL(s) copied to clipboard")
        except Exception:
            pass

    if has_error:
        sys.exit(1)
