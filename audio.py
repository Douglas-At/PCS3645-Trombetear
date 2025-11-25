import pygame
import os

pygame.mixer.init(frequency=44100) 

sons = {
    1: pygame.mixer.Sound(os.path.join("notas", "1.mp3")),
    2: pygame.mixer.Sound(os.path.join("notas", "2.mp3")),
    3: pygame.mixer.Sound(os.path.join("notas", "3.mp3")),
    4: pygame.mixer.Sound(os.path.join("notas", "4.mp3")),
    5: pygame.mixer.Sound(os.path.join("notas", "5.mp3")),
    6: pygame.mixer.Sound(os.path.join("notas", "6.mp3")),
    7: pygame.mixer.Sound(os.path.join("notas", "7.mp3"))
}

def play_note(nota):
    if nota in sons:
        sons[nota].play()
