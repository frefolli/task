import task.bl as Bl

class Frame:
    @staticmethod
    def open(ticket: str, start: str):
        return Frame(ticket, start)

    @staticmethod
    def deserialize(data: dict):
        return Frame(
            data["ticket"],
            Bl.read_time(data.get("start")),
            Bl.read_time(data.get("end"))
        )

    def __init__(self, ticket: str, start: str = None, end: str = None):
        self._ticket = ticket
        self._start = start or Bl.get_current_time()
        self._end = end

    def close(self, end: str):
        assert self._end is None
        self._end = end

    def reopen(self):
        assert self._end is not None
        self._end = None

    def serialize(self) -> dict:
        return {
            "ticket": self._ticket,
            "start": str(self._start),
            "end": str(self._end)
        }
