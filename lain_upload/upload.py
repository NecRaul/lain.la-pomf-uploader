import requests
import os

GIGABYTE = 1000000000

API_ENDPOINT = "https://pomf.lain.la/upload.php"


def upload_file(file_path):
    with open(file_path, "rb") as file:
        try:
            file_size = os.path.getsize(file_path)
            if file_size >= GIGABYTE:
                return None
            else:
                files = {"files[]": (file_path, file)}

                response = requests.post(API_ENDPOINT, files=files)

                if response.status_code == 200:
                    return response.json()
                else:
                    return None
        except:
            return None
