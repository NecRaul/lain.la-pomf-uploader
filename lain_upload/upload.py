import requests

API_ENDPOINT = "https://pomf.lain.la/upload.php"

def upload_file(file_path):
    with open(file_path, 'rb') as file:
                files = {'files[]': (file_path, file)}
        
                response = requests.post(API_ENDPOINT, files=files)
                
                return response.json()