class ImgNotFoundException(FileNotFoundError):
    def __init__(self, url=""):
        self.url = url

    def __str__(self):
        if not self.url == "":
            return "Image \"%s\" not found." % self.url
        else:
            return "Image not found."