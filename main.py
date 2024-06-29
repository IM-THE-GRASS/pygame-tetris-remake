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

center = (window_width/2,window_height/2)
I = {0:((0,0),(1,0),(2,0),(3,0)), 1:((0,-0),(0,-1),(0,-2),(0,-3)),2:((0,0),(-1,0),(-2,0),(-3,0)), 3:((0,0),(0,1),(0,2),(0,3))}
T = {0:((0,0),(1,0),(0,1),(-1,0)),3:((0,0),(0,1),(1,0),(0,-1)),2:((0,0),(1,0),(0,-1),(-1,0)),1:((0,0),(0,1),(0,-1),(-1,0))}
O = {0:((0,0),(0,1),(1,0),(1,1)),1:((0,0),(0,1),(1,0),(1,1)),2:((0,0),(0,1),(1,0),(1,1)),3:((0,0),(0,1),(1,0),(1,1))}
L = {0:((0,0),(0,1),(0,-1),(1,-1)),1:((0,0),(1,0),(-1,0),(-1,-1)),2:((0,0),(0,-1),(0,1),(-1,1)),3:((0,0),(1,1),(-1,0),(1,0))}
J = {0:((0,0),(0,-1),(0,1),(-1,-1)),1:((0,0),(1,0),(-1,0),(1,-1)),2:((0,0),(0,-1),(1,1),(0,1)),3:((0,0),(-1,1),(-1,0),(1,0))}
S = {0:((0,0),(-1,0),(0,1),(1,1)),1:((0,0),(0,1),(1,0),(1,-1)),2:((0,0),(0,-1),(-1,-1),(1,0)),3:((0,0),(-1,0),(0,-1),(-1,1))}
Z = {0:((0,0),(),(),()),1:((0,0),(),(),()),2:((0,0),(),(),()),3:((0,0),(),(),())}




class peice:
    def __init__(self,shape, position) -> None:
        self.pos = position
        self.rotation = 0
        self.shape = shape
        self.current_positions = {}
        self.last_valid_pos = ()
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
            thesquare["color"] = (255,255,255)
            thesquare["state"] = 0
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
        print(self.rotation)
        if self.rotation <= 0:
            self.rotation = 3 
        else:
            self.rotation = self.rotation - 1
        print(self.rotation)
        draw = self.draw()
        if draw == False and self.rotation < 0:
            self.rotation = self.rotation + 1
        print(self.rotation)
               
            

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
peices = peice(S, start_pos)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame .BUTTON_RIGHT:
                peices.rotate_r()
            if event.button == pygame.BUTTON_LEFT:
                peices.rotate_l()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                peices.pos = (peices.pos[0] + 1, peices.pos[1])
            if event.key == pygame.K_LEFT:
                peices.pos = (peices.pos[0] - 1, peices.pos[1])
            if event.key == pygame.K_DOWN:
                peices.pos = (peices.pos[0], peices.pos[1] - 1)
            if event.key == pygame.K_SPACE:
                peices.pos = (peices.pos[0], peices.pos[1] - 1)
                for i in range(lines):
                    print(i)
                    peices.pos = (peices.pos[0], 0)
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), board)
    
    clock.tick(60)
    if gravity_wait > 60:
        print("down")
        peices.pos = (peices.pos[0],peices.pos[1] - 1)
        gravity_wait = 0
    gravity_wait += 1
        
    peices.draw()

    for square in squares.values():
        pygame.draw.rect(screen, square["color"], square["rect"])
    
    pygame.display.flip()
