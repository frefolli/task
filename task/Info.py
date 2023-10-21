import task.bl as Bl

class Info:
    @staticmethod
    def deserialize(data: dict):
        return Info(
            data.get("author"),
            Bl.read_datetime(data.get("created_at")),
            Bl.read_datetime(data.get("updated_at"))
        )

    def __init__(self, author: str = None, created_at: str = None, updated_at: str = None):
        self._author = author or Bl.get_current_user()
        current_datetime = Bl.get_current_datetime()
        self._created_at = created_at or current_datetime
        self._updated_at = updated_at or current_datetime

    def serialize(self) -> dict:
        return {
        "author": self._author,
        "created_at": str(self._created_at),
        "updated_at": str(self._updated_at)
    }


