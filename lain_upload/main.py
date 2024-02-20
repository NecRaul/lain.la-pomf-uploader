from .upload import parse_file
import argparse
import pyperclip


def main():
    parser = argparse.ArgumentParser(description="Upload file to pomf.lain.la")
    parser.add_argument("path", help="File path")

    args = parser.parse_args()
    response = parse_file(args.path)

    if response:
        url = response["files"][0]["url"]
        pyperclip.copy(url)
        print(f"File URL: {url}\nCopied to clipboard.")
    else:
        print("Upload failed.")


if __name__ == "__main__":
    main()
