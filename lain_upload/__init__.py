from .upload import upload_file
import argparse

def main():
    
    parser = argparse.ArgumentParser(description="Upload file to pomf.lain.la")
    parser.add_argument("path", help="File path")
    
    args = parser.parse_args()
    response = upload_file(args.path)
    
    if response:
        url = response['files'][0]['url']
        print(f"File URL: {url}")
    else:
        print("Upload failed.")
    
if __name__ == "__main__":
    main()