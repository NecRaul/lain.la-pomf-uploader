from pathlib import Path

import requests
from requests_toolbelt import MultipartEncoderMonitor
from requests_toolbelt.multipart.encoder import MultipartEncoder

GIBIBYTE = 1024 * 1024 * 1024

API_ENDPOINT = "https://pomf.lain.la/upload.php"


def upload_file(file_path_str, progress_callback=None):
    file_path = Path(file_path_str)
    print(f"Uploading {file_path.name}")
    if not file_path.is_file():
        raise FileNotFoundError(file_path)
    file_size = file_path.stat().st_size
    if file_size > GIBIBYTE:
        raise ValueError(f"{file_path.name} bigger than 1GiB")
    with file_path.open("rb") as file:
        encoder = MultipartEncoder(fields={"files[]": (file_path.name, file)})
        data = (
            MultipartEncoderMonitor(
                encoder, lambda m: progress_callback(m.bytes_read, encoder.len)
            )
            if progress_callback
            else encoder
        )
        response = requests.post(
            url=API_ENDPOINT,
            data=data,
            headers={"Content-Type": data.content_type},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
