import os

import requests

GIBIBYTE = 1073741824

API_ENDPOINT = "https://pomf.lain.la/upload.php"


def upload_file(file_path):
    with open(file_path, "rb") as file:
        try:
            file_size = os.path.getsize(file_path)
            if file_size >= GIBIBYTE:
                return None
            else:
                files = {"files[]": (file_path, file)}

                response = requests.post(API_ENDPOINT, files=files)

                if response.status_code == 200:
                    return response.json()
                else:
                    return None
        except Exception:
            return None
