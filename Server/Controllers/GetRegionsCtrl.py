from Server.Models.Apis import Point, Frame, Regions

def getRegions():
    frames = [
        Frame(
            points=[
                Point(x=342, y=150),
                Point(x=664, y=115),
                Point(x=679, y=270),
                Point(x=358, y=305)
            ],
            score=0.9998086,
            ocr="Half"
        ),
        Frame(
            points=[
                Point(x=878, y=653),
                Point(x=1021, y=653),
                Point(x=1021, y=672),
                Point(x=879, y=672)
            ],
            score=0.99980634,
            ocr="pm0336-1683hy"
        ),
        Frame(
            points=[
                Point(x=0, y=651),
                Point(x=251, y=652),
                Point(x=251, y=672),
                Point(x=0, y=671)
            ],
            score=0.999803,
            ocr="全景网www.quanjing.com"
        )
    ]
    return Regions(
        size=Point(x=682, y=1024),
        cnt=len(frames),
        frames=frames
    )