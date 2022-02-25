def is_image(url: str):
    extension = url[-3:].lower()
    return "jpg" in extension or "png" in extension
