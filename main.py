import pygame


pygame.init()
board_width = 200
board_height = 400


columns = 10
gap = 2
sq_width = (board_width - (gap * (columns + 1))) / columns 
print(sq_width)
lines = int(board_height / (sq_width + gap))
squares = {}
gravity_wait = 0
window_width = 400
window_height = 600

center = (window_width/2,window_height/2)
I = ((0,0),(1,0),(2,0),(3,0))
class peice:
    def __init__(self,shape, position) -> None:
        self.pos = position
        
        self.shape = shape
        self.draw_at(position)
    def draw_at(self, pos):
        for square in self.shape:
            offset_x = square[0] + pos[0]
            offset_y = square[1] + pos[1]
            
            new_pos = (offset_x,offset_y)
            thesquare = squares[new_pos]
            
            thesquare["color"] = (255,0,255)
            thesquare["state"] = 0
            

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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_RIGHT:
            print("roght")
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), board)
    
    clock.tick(60)
    if gravity_wait > 60:
        print("down")
        gravity_wait = 0
    gravity_wait += 1
        
    
    peices = peice(I, (5,lines - 1))

    for square in squares.values():
        pygame.draw.rect(screen, square["color"], square["rect"])
    
    pygame.display.flip()
