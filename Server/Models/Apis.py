import json

class Point(object):
    def __init__(self, *, x, y):
        self.x = x
        self.y = y
    
    def toJson(self):
        return {
            "x": self.x,
            "y": self.y
        }

class Frame(object):

    def __init__(self, *, points: [Point], score: float, ocr: str):
        self.points = points
        self.score = score
        self.ocr = ocr

    def toJson(self):
        return {
            "points": [pnt.toJson() for pnt in self.points],
            "score": self.score,
            "ocr": self.ocr
        }

class Regions(object):

    def __init__(self, *, size: Point, cnt: int, frames: [Frame]):
        self.size = size
        self.cnt = cnt
        self.frames = frames

    def toJson(self):
        return {
            "size": self.size.toJson(),
            "cnt": self.cnt,
            "frames": [frm.toJson() for frm in self.frames]
        }