def is_image(url: str):
    extension = url[-4:].lower()
    return extension in [".gif", ".jpg", ".png"]
