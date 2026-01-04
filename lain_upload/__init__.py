import argparse

from .upload import upload_file

try:
    import pyperclip

    CLIP_OK = pyperclip.is_available()
except Exception:
    CLIP_OK = False


def main():
    parser = argparse.ArgumentParser(description="Upload file to pomf.lain.la")
    parser.add_argument("path", help="File path")

    args = parser.parse_args()
    response = upload_file(args.path)

    if response:
        url = response["files"][0]["url"]
        print(f"File URL: {url}")
        if CLIP_OK:
            pyperclip.copy(url)
            print("Copied to clipboard.")
    else:
        print("Upload failed.")


if __name__ == "__main__":
    main()
