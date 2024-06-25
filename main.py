import pygame


pygame.init()
board_width = 200
board_height = 400

lines = 3
width = 2
gap = 10

window_width = 400
window_height = 500

center = (window_width/2,window_height/2)
 


screen = pygame.display.set_mode((window_width, window_height))
def draw_rect(size, pos, color = (0,0,0), surface = screen):
    rec = pygame.Rect(0,0,0,0)
    rec.size = size
    rec.center = pos
    pygame.draw.rect(screen, color, rec)
pygame.display.set_caption("pygame tetris")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(width):
        sq_width = board_width - (gap * (width + 1))
        print(sq_width)
        #sq = pygame.Surface()
    
    
    
    screen.fill((255, 255, 255))
    board = draw_rect((board_width,board_height),center)
    pygame.display.flip()