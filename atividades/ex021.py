import pygame

# PROGRAMA QUE REPRODUZ ARQUIVO MP3

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

