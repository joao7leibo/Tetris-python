from settings import *
import random

class Block(pg.sprite.Sprite):
    def __init__(self,tetromino,pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_POS_OFFSET
        self.alive =True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image  #for the custum colors
        #self.image = pg.Surface([TILE_SIZE,TILE_SIZE])  #using default and not custum colors
        #self.image.fill('orange') #fills surface with solid color
        #pg.draw.rect(self.image, 'orange', (1, 1, TILE_SIZE - 2,TILE_SIZE - 2), border_radius=8)
        self.rect = self.image.get_rect()
        #self.rect.topleft = pos[0] *TILE_SIZE, pos[1] *TILE_SIZE  #simplified into below
        #self.rect.topleft = self.pos * TILE_SIZE

        self.sfx_image = self.image.copy()
        self.sfx_image.set_alpha(110)  #transparency value
        self.sfx_speed = random.uniform(0.2, 0.6) #random block speed value
        self.sfx_cycles = random.randrange(6,8)  #cycles for the duration of the effect
        self.cycle_counter = 0

    def sfx_end_time(self):  #determans the duration of the effect. counting cycles according to our animation trigger
        if self.tetromino.tetris.app.anim_trigger:
            self.cycle_counter += 1
            if self.cycle_counter > self.sfx_cycles:
                self.cycle_counter = 0
                return True

    def sfx_run(self):
        self.image = self.sfx_image
        self.pos.y -= self.sfx_speed
        self.image = pg.transform.rotate(self.image, pg.time.get_ticks() * self.sfx_speed)

    def is_alive(self):
        if not self.alive:
            if not self.sfx_end_time():
               self.kill()

    def rotate(self,pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos

    def set_rect_pos(self):
        pos = [self.next_pos, self.pos][self.tetromino.current]
        #self.rect.topleft = self.pos * TILE_SIZE
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_rect_pos()

    def is_collide(self,pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True
class Tetromino:
    def __init__(self, tetris, current=True):
        self.tetris = tetris
        #Block(self,(4, 7))  #was for example
        self.shape =  random.choice(list(TETROMINOES.keys()))
        self.image = random.choice(tetris.app.images)
        self.blocks = [Block(self,pos) for pos in TETROMINOES[self.shape]]
        self.landing = False  #landing attribute. so wont move.bellow direction down=true
        self.current = current

    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]

    def is_collide(self, block_positions):
        return any(map(Block.is_collide, self.blocks, block_positions))
    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        #forming new postions for the blocks
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        #checking if one of the blocks has a coliision at the new position
        is_collide = self.is_collide(new_block_positions)

        if not is_collide:  #if no, moving to new positions
            for block in self.blocks:
                block.pos += move_direction
        elif direction =='down':
            self.landing = True

    def update (self):
        self.move(direction='down')
        #pg.time.wait(200) # temporary solution for the falling speed