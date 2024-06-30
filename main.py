import pygame


pygame.init()
board_width = 200
board_height = 400


columns = 13
gap = 2
sq_width = (board_width - (gap * (columns + 1))) / columns 
print(sq_width)
lines = int(board_height / (sq_width + gap))
squares = {}
gravity_wait = 0
window_width = 400
window_height = 600
start_pos = (int(columns / 2), lines - 4)
lock_delay = 3

center = (window_width/2,window_height/2)
I = {0:((0,0),(1,0),(2,0),(3,0)), 1:((0,-0),(0,-1),(0,-2),(0,-3)),2:((0,0),(-1,0),(-2,0),(-3,0)), 3:((0,0),(0,1),(0,2),(0,3))}
T = {0:((0,0),(1,0),(0,1),(-1,0)),3:((0,0),(0,1),(1,0),(0,-1)),2:((0,0),(1,0),(0,-1),(-1,0)),1:((0,0),(0,1),(0,-1),(-1,0))}
O = {0:((0,0),(0,1),(1,0),(1,1)),1:((0,0),(0,1),(1,0),(1,1)),2:((0,0),(0,1),(1,0),(1,1)),3:((0,0),(0,1),(1,0),(1,1))}
L = {0:((0,0),(0,1),(0,-1),(1,-1)),1:((0,0),(1,0),(-1,0),(-1,-1)),2:((0,0),(0,-1),(0,1),(-1,1)),3:((0,0),(1,1),(-1,0),(1,0))}
J = {0:((0,0),(0,-1),(0,1),(-1,-1)),1:((0,0),(1,0),(-1,0),(1,-1)),2:((0,0),(0,-1),(1,1),(0,1)),3:((0,0),(-1,1),(-1,0),(1,0))}
S = {0:((0,0),(-1,0),(0,1),(1,1)),1:((0,0),(0,1),(1,0),(1,-1)),2:((0,0),(0,-1),(-1,-1),(1,0)),3:((0,0),(-1,0),(0,-1),(-1,1))}
Z = {0:((0,0),(1, 0),(-1, 1),(0, 1)),1:((0,0),(-1,0),(0,1),(-1,-1)),2:((0,0),(-1,0),(0,-1),(1,-1)),3:((0,0),(0,-1),(1,1),(1,0))}




class peice:
    def __init__(self,shape, position) -> None:
        self.pos = position
        self.rotation = 0
        self.shape = shape
        self.current_positions = {}
        self.last_valid_pos = ()
        
        self.grounded = False
        self.touching_others = False
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
            
        for square in self.current_positions:
            thesquare = squares[square]
            
            thesquare["state"] = 0
        
        for sq in self.shape[self.rotation]:
            print(sq)
            if squares[new_pos]["state"] == 1:
                new_x = sq[0] + self.pos[0]
                new_y = sq[1] + self.pos[1]
                new_pos = (new_x,new_y)
                self.pos = self.last_valid_pos
                self.touching_others = True
                return False
            else:
                self.touching_others = False
                
        for sq in self.current_positions:
            thesquare = squares[sq]
            thesquare["color"] = (255,255,255)
        self.current_positions.clear()
        for square in new_current:
            position = squares[square]
            position["color"] = (255,0,255)
            position["state"] = 1
            self.current_positions[square] = 1
            self.last_valid_pos = self.pos
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
current_peice = peice(Z, start_pos)
lock_timer = 0
lock_timer_enabled = False
lock_delay = lock_delay * 60
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame .BUTTON_RIGHT:
                current_peice.rotate_r()
            if event.button == pygame.BUTTON_LEFT:
                current_peice.rotate_l()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_peice.pos = (current_peice.pos[0] + 1, current_peice.pos[1])
            if event.key == pygame.K_LEFT:
                current_peice.pos = (current_peice.pos[0] - 1, current_peice.pos[1])
            if event.key == pygame.K_DOWN:
                current_peice.pos = (current_peice.pos[0], current_peice.pos[1] - 1)
            if event.key == pygame.K_SPACE:
                current_peice.pos = (current_peice.pos[0], current_peice.pos[1] - 1)
                for i in range(lines):
                    current_peice.pos = (current_peice.pos[0], 0)
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
            current_peice = peice(L, start_pos)
            lock_timer_enabled = False
            lock_timer = 0
        lock_timer += 1
        
        
    current_peice.draw()
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), board)
    
    
    if gravity_wait > 60:
        current_peice.pos = (current_peice.pos[0],current_peice.pos[1] - 1)
        gravity_wait = 0
    
    gravity_wait += 1

    for square in squares.values():
        pygame.draw.rect(screen, square["color"], square["rect"])
    
    pygame.display.flip()
