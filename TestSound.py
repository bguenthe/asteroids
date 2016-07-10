import pygame
import time
from pydub import AudioSegment

pygame.mixer.init(44100, -16, 2, 2048)
#pygame.mixer.init()
song = AudioSegment.from_file("missile.mp3", format="mp3")
pygame.mixer.Sound(song.raw_data)

so = pygame.mixer.Sound(song.raw_data)
print(1)
so.play()
print(2)
time.sleep(1)