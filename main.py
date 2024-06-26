import pygame


pygame.init()
board_width = 200
board_height = 400


columns = 5
gap = 7
sq_width = (board_width - (gap * (columns + 1))) / columns 
print(sq_width)
lines = int(board_height / (sq_width + gap))


window_width = 400
window_height = 600

center = (window_width/2,window_height/2)



screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("pygame tetris")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    
    screen.fill((255, 255, 255))
    
    board = pygame.Rect(0,0,0,0)
    board.size = (board_width,board_height)
    board.center = center
    
    pygame.draw.rect(screen, (0,0,0), board)
    for line in range(lines):
        for i in range(columns):
            
            sq = pygame.Rect(0,0,0,0)
            sq.size = (sq_width,sq_width)
            sq.center = (10,10)
            sq.bottomleft = (board.bottomleft[0] + gap + ((i * gap) + (i * sq_width)), board.bottomleft[1] - gap - ((line * gap) + (line * sq_width))) 
            pygame.draw.rect(screen, (255,255,255), sq)
    
        
    pygame.display.flip()