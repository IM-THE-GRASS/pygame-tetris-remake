import pygame


pygame.init()
board_width = 200
board_height = 400


columns = 5
gap = 7
sq_width = (board_width - (gap * (columns + 1))) / columns 
print(sq_width)
lines = int(board_height / (sq_width + gap))
squares = {}

window_width = 400
window_height = 600

center = (window_width/2,window_height/2)
I = {(0,1),(1,1),(2,1),(3,1)}
class peice:
    def __init__(self,shape) -> None:
        self.shape = shape
    def draw_at(self, pos):
        for square in self.shape:
            square = squares[square]
            pygame.draw.rect(screen, (255,0,255), square)
            

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("pygame tetris")
running = True
board = pygame.Rect(0,0,0,0)
board.size = (board_width,board_height)
board.center = center
for line in range(lines):
    for i in range(columns):
            
        sq = pygame.Rect(0,0,0,0)
        sq.size = (sq_width,sq_width)
        sq.center = (10,10)
        sq.bottomleft = (board.bottomleft[0] + gap + ((i * gap) + (i * sq_width)), board.bottomleft[1] - gap - ((line * gap) + (line * sq_width))) 
        
        squares[(line, i)] = sq
        print((line, i))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    
    screen.fill((255, 255, 255))
    
    
    
    pygame.draw.rect(screen, (0,0,0), board)
    
    for square in squares.values():
        pygame.draw.rect(screen, (255,255,255), square)
    peices = peice(I)
    peices.draw_at((0,0))
    pygame.display.flip()