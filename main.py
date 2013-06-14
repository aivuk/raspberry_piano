# -*- coding: utf-8 -*-

import os, sys
import random
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.set_num_channels(16)
screen = pygame.display.set_mode((468,60))
clock = pygame.time.Clock()
test_sound = pygame.mixer.Sound('match0.wav')
note_keys = [K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p]
track_keys = [K_a, K_s, K_d, K_j, K_k, K_l]

notes = {}
tracks = [] 
tkey = {}

playing_tracks = set()

def load_sounds(notes, tracks):
    notes[K_q] = pygame.mixer.Sound('sounds/1-C2.wav')
    notes[K_w] = pygame.mixer.Sound('sounds/2-D2.wav')
    notes[K_e] = pygame.mixer.Sound('sounds/3-F2.wav')
    notes[K_r] = pygame.mixer.Sound('sounds/4-G2.wav')
    notes[K_t] = pygame.mixer.Sound('sounds/5-A2.wav')
    notes[K_y] = pygame.mixer.Sound('sounds/pentatonic-1.wav')
    notes[K_u] = pygame.mixer.Sound('sounds/pentatonic-2.wav')
    notes[K_i] = pygame.mixer.Sound('sounds/pentatonic-3.wav')
    notes[K_o] = pygame.mixer.Sound('sounds/pentatonic-4.wav')
    notes[K_p] = pygame.mixer.Sound('sounds/pentatonic-5.wav')

    sound_files = os.listdir('sounds')

    for f in sound_files:
        if f[0:5] == 'track':
            tracks.append(pygame.mixer.Sound('sounds/{}'.format(f)))

def proc_events(notes):
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
            elif event.key in note_keys:
                notes[event.key].play()
            elif event.key in track_keys and not tkey.has_key(event.key):
                random_track = random.choice(list(tracks_range - playing_tracks))
                tkey[event.key] = random_track
                tracks[random_track].play(fade_ms=1000, loops=-1)
                playing_tracks.add(random_track)
        elif event.type == KEYUP:
            if event.key in note_keys:
                notes[event.key].fadeout(500)
            elif event.key in track_keys:
                tracks[tkey[event.key]].fadeout(1000) 
                playing_tracks.remove(tkey[event.key])
                tkey.pop(event.key)

    return True
     

load_sounds(notes, tracks)
tracks_range = set(xrange(len(tracks)))

running = True
while running:
    clock.tick(60)
    running = proc_events(notes)    

pygame.quit()

