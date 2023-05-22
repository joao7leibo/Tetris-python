import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR =(48,39,20)
BG_COLOR = (24, 89, 117)

ANIM_TIME_INTERVAL = 150 #milliseconds
FAST_ANIM_TIME_INTERVAL = 15

SPRITE_DIR_PATH = 'assets/sprites'
FONT_PATH = 'assets/font/FREAKSOFNATUREMASSIVE.ttf'

TILE_SIZE = 50
FIELD_SIZE = FIELD_W, FIELD_H =10,20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H =1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

#movement direction
MOVE_DIRECTIONS = {'left': vec(-1,0), 'right':vec(1,0),'down':vec(0,1)}
NEXT_POS_OFFSET = vec(FIELD_W * 1.233,FIELD_H * 0.45)
INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)

#making the shapes
TETROMINOES = {
    'T': [(0, 0), (-1,0),(1, 0),(0, -1)],
    'O': [(0, 0), (0,-1),(1, 0),(1, -1)],
    'J': [(0, 0), (-1,0),(0, -1),(0, -2)],
    'L': [(0, 0), (1,0),(0, -1),(0, -2)],
    'I': [(0, 0), (0, 1),(0, -1),(0, -2)],
    'S': [(0, 0), (-1,0),(0, -1),(1, -1)],
    'Z': [(0, 0), (1,0),(0, -1),(-1, -1)]
}