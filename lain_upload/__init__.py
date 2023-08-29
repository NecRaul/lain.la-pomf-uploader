from .upload import upload_file
import argparse

def main():
    
    parser = argparse.ArgumentParser(description="Upload file to pomf.lain.la")
    parser.add_argument("path", help="File path")
    
    args = parser.parse_args()
    response = upload_file(args.path)
    
    url = response['files'][0]['url']
    print(f"File URL: {url}")
    
if __name__ == "__main__":
    main()