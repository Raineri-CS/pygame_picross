import json
import os

COLOR_BACKGROUND = (51, 153, 255)
COLOR_TEXT = (200, 200, 200)
COLOR_FOREGROUND = (0, 102, 204)
# TODO change this
COLOR_SELECTED = (0, 0, 0)


class GameSettings:
    def __init__(self) -> None:
        dirname = os.path.dirname(__file__)
        filename = dirname[:-8] + '/resources/settings.json'
        jsonfile = open(filename)
        x = json.loads(jsonfile.read())
        # Resolution
        for key in x["options"]["video"]["resolution"]:
            for value in key:
                if(key.get(value) == True):
                    self.resolution = (value.split("x"))
        # Audio stuff
        for key in x["options"]["audio"]["music"]:
            for value in key:
                if(key.get(value) == True):
                    self.audioLevel = (value[:-1])
        for key in x["options"]["audio"]["sfx"]:
            for value in key:
                if(key.get(value) == True):
                    self.sfxLevel = (value[:-1])
        jsonfile.close()

    def getResolution(self):
        return self.resolution

    def getMusicLevel(self):
        return self.audioLevel

    def getSfxLevel(self):
        return self.sfxLevel

    # TODO settings write
