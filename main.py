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
def draw_rect(size, pos, surface = screen, color = (0,0,0)):
    rec = pygame.Surface(size)
    topleft = (pos[0] - (size[0] / 2),pos[1] - (size[1] / 2))
    rec.fill(color)
    surface.blit(rec,topleft)
    rec.fill(color)
    return rec
pygame.display.set_caption("pygame tetris")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    
    screen.fill((255, 255, 255))
    
    for i in range(width):
        sq_width = board_width - (gap * (width + 1))
        sq = draw_rect((sq_width,sq_width),(10,10), board, (255,0,255))
        print(sq)
    board = draw_rect((board_width,board_height),center)
    pygame.display.flip()