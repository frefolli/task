import task.Log as Log
import task.YamlFile as YamlFile
import task.bl as Bl

class Workspace:
    def __init__(self, options: dict = None):
        if options is None:
            options = {"path": "%s/.task" % Bl.get_home_path()}
        self._path = options["path"]
        Bl.ensure_dir(self._path)
        self._load_log()
        self._save_log()

    def _master_log(self) -> YamlFile:
        return YamlFile.relative(self._path, "master.log")

    def _load_log(self):
        self._log = Log.deserialize(self._master_log().skel(Log).read())

    def _save_log(self):
        self._master_log().write(self._log.serialize())
