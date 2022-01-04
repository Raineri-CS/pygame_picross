import os
import random
import pygame

from include.settings import SONG_OVER, GameSettings

# TODO sound level stuff based on the config.json thing, INCLUDING SFX/MUSIC separation


class MusicPlayer:
    def __init__(self) -> None:
        self.songList = self.genSongList()
        self.clickList = self.genClickList()
        self.isMusicPlaying = True

        pygame.mixer.music.set_volume(GameSettings().getMusicLevel()/100)

        pygame.mixer.music.load(
            self.songList[random.randrange(0, len(self.songList), 1)], "mp3")
        pygame.mixer.music.play(loops=0, start=0.0, fade_ms=3000)
        pygame.mixer.music.set_endevent(SONG_OVER)

        pass

    def genSongList(self) -> list:
        localSongList = []
        dirname = os.path.dirname(__file__)
        localDir = dirname[:-8] + "/resources/music/"
        for file in os.listdir(localDir):
            localSongList.append(localDir + file)
            pass
        return localSongList

    def togglePlay(self) -> None:
        if(self.isMusicPlaying):
            self.isMusicPlaying = False
            pygame.mixer.music.unload()
            pygame.mixer.music.stop()
        else:
            self.isMusicPlaying = True
            pygame.mixer.music.unload()
            pygame.mixer.music.load(
                self.songList[random.randrange(0, len(self.songList), 1)], "mp3")
            pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=3000)

    def genClickList(self) -> list:
        localClickList = []
        dirname = os.path.dirname(__file__)
        localDir = dirname[:-8] + "/resources/sounds/"
        for file in os.listdir(localDir):
            localClickList.append(localDir + file)
            pass
        return localClickList

    def setVolume(self) -> None:
        pass

    def swapTracks(self) -> None:
        if(self.isMusicPlaying):
            pygame.mixer.music.unload()
            pygame.mixer.music.load(
                self.songList[random.randrange(0, len(self.songList), 1)], "mp3")
            pygame.mixer.music.play(loops=0, start=0.0, fade_ms=3000)
        pass

    def click(self) -> None:
        toBePlayed = pygame.mixer.Sound(
            self.clickList[random.randrange(0, len(self.clickList), 1)])
        pygame.mixer.Sound.set_volume(
            toBePlayed, GameSettings().getSfxLevel()/100)
        pygame.mixer.Sound.play(toBePlayed)
        pass
