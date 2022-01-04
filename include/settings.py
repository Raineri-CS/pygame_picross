import json
import os

COLOR_BACKGROUND = (51, 153, 255)
COLOR_TEXT = (200, 200, 200)
COLOR_FOREGROUND = (0, 102, 204)
COLOR_SELECTED = (0, 58, 116)
FONT_SIZE_TEXT = 40
FONT_SIZE_HINTS = 30
SONG_OVER = 666

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
        # NOTE maybe this shouldnt be on this class?
        dirname = os.path.dirname(__file__)
        levelsDir = os.listdir(dirname[:-8] + '/resources/levels/')
        # NOTE we have 2 options, cache every puzzle here as a Puzzle class, OR store the filenames for the levels, loading them on selection
        self.levelList = []
        for file in levelsDir:
            self.levelList.append(file)
            pass
        self.completedLevelList = []
        filename = dirname[:-8] + '/resources/save.json'
        if not os.path.exists(filename):
            os.mknod(filename)
            saveFile = open(filename, 'w')
            saveFile.write("{\n\t\"levels\": [\n\t]\n}")
            saveFile.close()

        saveFile = open(filename)
        x = json.loads(saveFile.read())
        for key in x['levels']:
            for value in key:
                self.completedLevelList.append(key)

    def getResolution(self) -> list:
        return self.resolution

    def getMusicLevel(self) -> int:
        return int(self.audioLevel)

    def getSfxLevel(self) -> int:
        return int(self.sfxLevel)

    def getLevelList(self) -> list:
        return self.levelList

    def getCompletedLevelList(self) -> list:
        return self.completedLevelList

    # TODO settings write
