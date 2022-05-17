import pygame as pg
import sys
import random 

key_delta = {pg.K_UP : [0, -1],
             pg.K_DOWN : [0, +1],
             pg.K_LEFT : [-1, 0],
             pg.K_RIGHT : [+1, 0],}

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1200,600))
    sc_rect = screen.get_rect()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img = pg.transform.scale(bg_img, (1200,600))
    bg_rect = bg_img.get_rect()
    #bg_rect.center = (1500,500)
    screen.blit(bg_img, bg_rect)

    tori_img = pg.image.load("fig/8.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400
    screen.blit(tori_img, tori_rect)

    X = random.randint(0, 225)
    Y = random.randint(0, 225)
    Z = random.randint(0, 225)
    bomb = pg.Surface((20,20))
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb,(X,Y,Z),(10, 10),10)
    bomb_rect = bomb.get_rect()
    bomb_rect.centerx = random.randint(0, sc_rect.width)
    bomb_rect.centery = random.randint(0, sc_rect.height)
    screen.blit(bomb, bomb_rect)
    vx, vy = +1, +1



    while True:
        screen.blit(bg_img, bg_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_states = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_states[key] == True:
                tori_rect.centerx += delta[0]
                tori_rect.centery += delta[1]
                if check_bound(sc_rect, tori_rect) != (1,1):
                    tori_rect.centerx -= delta[0]
                    tori_rect.centery -= delta[1]
        screen.blit(tori_img, tori_rect)

        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb, bomb_rect)
        x, y = check_bound(sc_rect, bomb_rect)
        vx *= x
        vy *= y

        if tori_rect.colliderect(bomb_rect): return

        pg.display.update()
        clock.tick(1000)

def check_bound(sc_r, obj_r):
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right:
        x = -1
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom:
        y = -1
    return x, y


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()