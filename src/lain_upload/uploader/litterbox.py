from .base import BaseUploader


class LitterboxUploader(BaseUploader):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_max_size = 1000 * 1000 * 1000
        self.file_max_size_str = "1GB"
        self.api_endpoint = "https://litterbox.catbox.moe/resources/internals/api.php"

    @staticmethod
    def _build_fields(file_name, file):
        return {
            "reqtype": "fileupload",
            "time": "12h",  # placeholder
            "fileToUpload": (file_name, file),
        }

    @staticmethod
    def _extract_url(response):
        return response.text
