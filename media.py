from pathlib import Path

class MediaFile:
    def __init__(self, path: Path):
        self.path = path
        self.name = path.name
        self.stem = path.stem
        self.suffix = path.suffix.lower()
        
    def is_image(self) -> bool:
        return self.suffix in (".heic", ".jpg", ".jpeg", ".png")
        
    def is_video(self) -> bool:
        return self.suffix == ".mov"
