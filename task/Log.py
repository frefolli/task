import task.Info as Info
import task.Frame as Frame

class Log:
    SKEL = {"info": {}, "frames": []}
    @staticmethod
    def deserialize(data: dict):
        return Log(
            Info.deserialize(data["info"]),
            list(map((lambda k: l.deserialize()), data["frames"]))
        )

    def __init__(self, info: Info = None, frames: list[Frame] = []):
        self._info = info or Info()
        self._frames = frames

    def serialize(self) -> dict:
        return {
        "info": self._info.serialize(),
        "frames": list(map((lambda k: l.serialize()), self._frames))
    }


