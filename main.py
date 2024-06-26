import pygame
import random

pygame.init()
board_width = 200
board_height = 400


columns = 13
gap = 2
sq_width = (board_width - (gap * (columns + 1))) / columns 
lines = int(board_height / (sq_width + gap))
squares = {}
gravity_wait = 0
window_width = 400
window_height = 600
start_pos = (int(columns / 2), lines - 4)
lock_delay = 3

center = (window_width/2,window_height/2)
colors = {"I":(68, 114, 196),"T":(237, 125, 49),"O":(255, 192, 0),"L":(112, 48, 160),"J":(112, 173, 71),"S":(255, 0, 0),"Z":(0,0,255)}
I = {0:((0,0),(1,0),(2,0),(3,0)), 1:((0,-0),(0,-1),(0,-2),(0,-3)),2:((0,0),(-1,0),(-2,0),(-3,0)), 3:((0,0),(0,1),(0,2),(0,3)),"color":colors["I"]}
T = {0:((0,0),(1,0),(0,1),(-1,0)),3:((0,0),(0,1),(1,0),(0,-1)),2:((0,0),(1,0),(0,-1),(-1,0)),1:((0,0),(0,1),(0,-1),(-1,0)),"color":colors["T"]}
O = {0:((0,0),(0,1),(1,0),(1,1)),1:((0,0),(0,1),(1,0),(1,1)),2:((0,0),(0,1),(1,0),(1,1)),3:((0,0),(0,1),(1,0),(1,1)),"color":colors["O"]}
L = {0:((0,0),(0,1),(0,-1),(1,-1)),1:((0,0),(1,0),(-1,0),(-1,-1)),2:((0,0),(0,-1),(0,1),(-1,1)),3:((0,0),(1,1),(-1,0),(1,0)),"color":colors["L"]}
J = {0:((0,0),(0,-1),(0,1),(-1,-1)),1:((0,0),(1,0),(-1,0),(1,-1)),2:((0,0),(0,-1),(1,1),(0,1)),3:((0,0),(-1,1),(-1,0),(1,0)),"color":colors["J"]}
S = {0:((0,0),(-1,0),(0,1),(1,1)),1:((0,0),(0,1),(1,0),(1,-1)),2:((0,0),(0,-1),(-1,-1),(1,0)),3:((0,0),(-1,0),(0,-1),(-1,1)),"color":colors["S"]}
Z = {0:((0,0),(1, 0),(-1, 1),(0, 1)),1:((0,0),(-1,0),(0,1),(-1,-1)),2:((0,0),(-1,0),(0,-1),(1,-1)),3:((0,0),(0,-1),(1,1),(1,0)),"color":colors["Z"]}
peices = [I, T, O, L, J, S, Z]



class peice:
    def __init__(self,shape, position) -> None:
        self.color = shape["color"]
        self.pos = position
        self.rotation = 0
        self.shape = shape
        self.current_positions = {}
        self.last_valid_pos = ()
        
        self.grounded = False
        self.touching_others = False
        self.draw()
        
        
    def hard_drop(self):
        while not self.grounded and not self.touching_others:
            self.pos = (self.pos[0], self.pos[1] - 1)
            self.draw()
        self.pos = (self.pos[0], self.pos[1] + 1)
        self.draw()
    def draw(self):
        new_current = {}

        
        
        for square in self.shape[self.rotation]:
            new_x = square[0] + self.pos[0]
            new_y = square[1] + self.pos[1]
            new_pos = (new_x,new_y)
            
            try: # make sure that the square that is trying to go to actually exists
                new_current[new_pos] = squares[new_pos]
            except:
                self.pos = self.last_valid_pos
                return False
            
        for sq in self.current_positions:
            thesquare = squares[sq]
            
            thesquare["state"] = 0
            thesquare = squares[sq]
            thesquare["color"] = (255,255,255)
        self.current_positions.clear()
        for sq in new_current:
            square = squares[sq]
            if square["state"] == 1:
                self.touching_others = True
                self.pos = self.last_valid_pos
                self.draw()
                return False
            
        
        for square in new_current:
            position = squares[square]
            position["color"] = self.color
            position["state"] = 1
            self.current_positions[square] = 1
            self.last_valid_pos = self.pos
        return True
    def rotate_r(self):
        if self.rotation >= 3:
            self.rotation = 0 
        else:
            self.rotation = self.rotation + 1
        draw = self.draw()
        if draw == False and self.rotation >= 3:
            self.rotation = self.rotation - 1
    def rotate_l(self):
        if self.rotation <= 0:
            self.rotation = 3 
        else:
            self.rotation = self.rotation - 1
        draw = self.draw()
        if draw == False and self.rotation < 0:
            self.rotation = self.rotation + 1
               
def get_random_peice():
    random_peice = random.choice(peices)
    return random_peice
    
def clear_lines():
    
    for y in range(lines):
        squares_in_row = {}
        for x in range(columns):
            squares_in_row[x] = squares[(x, y)]["state"] == 1
        line_full = all(squares[(x, y)]["state"] == 1 for x in range(columns))
        if line_full:
            print(line_full)
            for above_y in range(y + 1,start_pos[1]):
                for x in range(columns):
                    squares[(x, above_y - 1)]["state"] = squares[(x, above_y)]["state"]
                    squares[(x, above_y - 1)]["color"] = squares[(x, above_y)]["color"]
                    squares[(x, above_y)]["state"] = 0
                    squares[(x, above_y)]["color"] = (255, 255, 255)
                
                
                    

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("pygame tetris")
running = True
board = pygame.Rect(0,0,0,0)
board.size = (board_width,board_height)
board.center = center
clock = pygame.time.Clock()
for line in range(lines):
    for i in range(columns):
            
        sq = pygame.Rect(0,0,0,0)
        sq.size = (sq_width,sq_width)
        sq.bottomleft = (board.bottomleft[0] + gap + ((i * gap) + (i * sq_width)), board.bottomleft[1] - gap - ((line * gap) + (line * sq_width))) 
        
        squares[(i, line)] = {"rect": sq, "color": (255,255,255), "state": 0}
current_peice = peice(get_random_peice(), start_pos)
lock_timer = 0
lock_timer_enabled = False
lock_delay = lock_delay * 60
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                current_peice.rotate_l()
            if event.key == pygame.K_RIGHT:
                current_peice.pos = (current_peice.pos[0] + 1, current_peice.pos[1])
            if event.key == pygame.K_LEFT:
                current_peice.pos = (current_peice.pos[0] - 1, current_peice.pos[1])
            if event.key == pygame.K_DOWN:
                current_peice.pos = (current_peice.pos[0], current_peice.pos[1] - 1)
            if event.key == pygame.K_SPACE:
                worked = True  
                while worked == True:
                    current_peice.pos = (current_peice.pos[0], current_peice.pos[1] - 1)
                    worked = current_peice.draw()
                lock_timer = 999
                    
                    
    current_positions = current_peice.current_positions.keys()
    for sq_pos in current_positions:
        if sq_pos[1] < 1 and current_peice.grounded == False:
            current_peice.grounded = True
    if current_peice.grounded or current_peice.touching_others:
        lock_timer_enabled = True
    else:
        lock_timer_enabled = False
    
    if lock_timer_enabled:
    
        if lock_timer >= lock_delay:
            current_peice = peice(get_random_peice(), start_pos)
            lock_timer_enabled = False
            lock_timer = 0
        lock_timer += 1
        
    clear_lines()
    current_peice.draw()
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), board)
    
    
    if gravity_wait > 60:
        current_peice.pos = (current_peice.pos[0],current_peice.pos[1] - 1)
        gravity_wait = 0
    
    gravity_wait += 1

    for square in squares.values():
        pygame.draw.rect(screen,square["color"],square["rect"])
    
    pygame.display.flip()
