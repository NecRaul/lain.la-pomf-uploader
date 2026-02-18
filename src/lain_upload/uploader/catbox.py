from .base import BaseUploader


class CatboxUploader(BaseUploader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_max_size = 200 * 1000 * 1000
        self.file_max_size_str = "200MB"
        self.api_endpoint = "https://catbox.moe/user/api.php"

    @staticmethod
    def _build_fields(file_name, file):
        return {
            "reqtype": "fileupload",
            "userhash": "",  # placeholder
            "fileToUpload": (file_name, file),
        }

    @staticmethod
    def _extract_url(response):
        return response.text
