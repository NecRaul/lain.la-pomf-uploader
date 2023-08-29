import requests

API_ENDPOINT = "https://pomf.lain.la/upload.php"

def upload_file(file_path):
    with open(file_path, 'rb') as file:
                files = {'files[]': (file_path, file)}
        
                response = requests.post(API_ENDPOINT, files=files)
                
                if response.status_code == 200:
                    return response.json()
                else:
                    return None