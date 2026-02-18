from .base import BaseUploader


class UguuUploader(BaseUploader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_max_size = 128 * 1024 * 1024
        self.file_max_size_str = "128MiB"
        self.api_endpoint = "https://uguu.se/upload?output=text"

    @staticmethod
    def _build_fields(file_name, file):
        return {"files[]": (file_name, file)}

    @staticmethod
    def _extract_url(response):
        return response.text
