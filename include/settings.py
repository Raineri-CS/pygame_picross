import json

COLOR_BACKGROUND = (51, 153, 255)
COLOR_TEXT = (200,200,200)
COLOR_FOREGROUND = (0, 102, 204)

class GameSettings:
    def __init__(self) -> None:
        jsonfile = open("./resources/settiongs.json")
        x = json.loads(jsonfile.read())
        # Resolution
        for key in x["options"]["video"]["resolution"]:
            for value in key:
                if(key.get(value) == True):
                    self.resolution = (key.split("x"))
        # Audio stuff
        for key in x["options"]["audio"]["music"]:
            for value in key:
                if(key.get(value) == True):
                    self.audioLevel = (key[:-1])
        for key in x["options"]["audio"]["sfx"]:
            for value in key:
                if(key.get(value) == True):
                    self.sfxLevel = (key[:-1])
        jsonfile.close()

    def getResolution(self):
        return self.resolution

    def getMusicLevel(self):
        return self.audioLevel

    def getSfxLevel(self):
        return self.sfxLevel

    # TODO settings write
