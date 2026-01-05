import argparse

from .upload import upload_file


def main():
    parser = argparse.ArgumentParser(description="Upload file to pomf.lain.la")
    parser.add_argument("path", help="File path")

    args = parser.parse_args()
    response = upload_file(args.path)

    if response:
        url = response["files"][0]["url"]
        print(f"File URL: {url}")

        try:
            import pyperclip

            pyperclip.copy(url)
            print("Copied to clipboard.")
        except Exception:
            pass
    else:
        print("Upload failed.")


if __name__ == "__main__":
    main()
