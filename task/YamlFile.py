from __future__ import annotations
import yaml
import os

class YamlFile:
    @staticmethod
    def relative(base: str, path: str) -> YamlFile:
        return YamlFile(os.path.join(base, path))

    def __init__(self, path: str):
        self._path = path
        self._skel = None

    def skel(self, klass) -> YamlFile:
        self._skel = klass.SKEL
        return self

    def read(self) -> dict:
        if os.path.exists(self._path):
            with open(self._path, mode="r", encoding="utf-8") as file:
                return yaml.load(file.read(), Loader=yaml.Loader)
        elif self._skel is not None:
            self.write(self._skel)
            return self._skel
        else:
            raise Exception("no '%s' file exists nor skel has been defined" % self._path)

    def write(self, obj):
        with open(self._path, mode="w", encoding="utf-8") as file:
            file.write(yaml.dump(obj, Dumper=yaml.Dumper))
