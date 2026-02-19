from .base import BaseUploader


class NullUploader(BaseUploader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_max_size = 512 * 1024 * 1024
        self.file_max_size_str = "512MiB"
        self.api_endpoint = "https://0x0.st"

    def _build_fields(self, file_name, file):
        return {"file": (file_name, file)}

    @staticmethod
    def _extract_url(response):
        return response.text
