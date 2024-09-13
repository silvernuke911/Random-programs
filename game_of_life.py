import time
import pygame
import numpy as np

color_BG = (10,10,10)
color_GRID = (40,40,40)
color_DIE_NEXT = (20,20,20)
color_ALIVE_NEXT = (255,255,255)

def update(screen, cells,size,width_progress=False):
    updated_cells = np.zeros((cells.shape[0],cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2,col-1:col+2])-cells[row,col]
        color = color_BG if cells[row,col]==0 else color_ALIVE_NEXT

        if cells[row,col]==1:
            if alive<2 or alive>3:
                if width_progress:
                    color=color_DIE_NEXT
            elif 2<= alive <= 3:
                updated_cells[row,col]=1
                if width_progress:
                    color=color_ALIVE_NEXT
        else:
            if alive==3:
                updated_cells[row,col]=1
                if width_progress:
                    color=color_ALIVE_NEXT   
        pygame.draw.rect(screen,color, (col*size, row*size, size-1,size-1))
    return updated_cells

def main():
    pygame.init()
    screen=pygame.display.set_mode((800,600))

    cells=np.zeros((60,80))
    screen.fill(color_GRID)
    update(screen,cells,10)

    pygame.display.flip()
    pygame.display.update()

    running=False
    delete=False
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    running=not running
                    update(screen, cells, 10)
                    pygame.display.update()
                if event.key==pygame.K_k:
                    cells=cells=np.zeros((60,80))
                    pygame.display.update()
                if event.key==pygame.K_a:
                    delete=not delete
            if pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                if cells[pos[1]//10,pos[0]//10]==1 and delete==True:
                    cells[pos[1]//10,pos[0]//10]=0
                else:
                    cells[pos[1]//10,pos[0]//10]=1
                update(screen, cells, 10)
                pygame.display.update()
        screen.fill(color_GRID)

        if running:
            cells=update(screen,cells,10,width_progress=True)
            pygame.display.update()
        
        time.sleep(0.0001)

if __name__=='__main__':
    main()