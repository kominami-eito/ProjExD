import pygame as pg
import sys
import random

class Screen:
    def __init__(self, fn, wh, title):
        pg.display.set_caption(title)
        self.width, self.height = wh
        self.disp = pg.display.set_mode((self.width, self.height))
        self.rect= self.disp.get_rect()
        self.image = pg.image.load(fn)

class Bird(pg.sprite.Sprite):
    key_delta = {pg.K_UP   : [0, -1],
                 pg.K_DOWN : [0, +1],
                 pg.K_LEFT : [-1, 0],
                 pg.K_RIGHT: [+1, 0],}

    def __init__(self, fn, r, xy):
        super().__init__()
        self.image = pg.image.load(fn)
        self.image = pg.transform.rotozoom(self.image, 0, r)
        self.rect= self.image.get_rect()
        self.rect.center = xy

    def update(self, screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key] == True:
                self.rect.centerx += delta[0]
                self.rect.centery += delta[1]
                # 練習7
                if check_bound(screen.rect, self.rect) != (1,1): 
                    self.rect.centerx -= delta[0]
                    self.rect.centery -= delta[1]

class Bomb(pg.sprite.Sprite):
    def __init__(self, color, r, vxy, screen):
        super().__init__()
        self.image = pg.Surface((2*r,2*r))                     # 爆弾用のSurface
        self.image.set_colorkey((0,0,0))                     # 黒色部分を透過する
        pg.draw.circle(self.image, color, (r,r), r)   # 爆弾用Surfaceに円を描く
        self.rect = self.image.get_rect()                    # 爆弾用Rect
        self.rect.centerx = random.randint(0, screen.rect.width)
        self.rect.centery = random.randint(0, screen.rect.height)
        #screen.blit(self.image, self.rect)                   # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
        self.vx, self.vy = vxy
    
    def update(self, screen):
        self.rect.move_ip(self.vx, self.vy)
        x, y = check_bound(screen.rect, self.rect)
        self.vx *= x # 横方向に画面外なら，横方向速度の符号反転
        self.vy *= y # 縦方向に画面外なら，縦方向速度の符号反転

class Score():
    def __init__(self, fs):
        self.font = pg.font.Font(None, fs)
        self.scores = pg.time.get_ticks()//1000 #スコアの計算　1秒につき1増えるようにする
        self.txt = self.font.render(str(f"Score:{self.scores}point"), True, (0, 0, 0))

def main():
    clock = pg.time.Clock()
    
    # 練習1
    screen = Screen("fig/pg_bg.jpg", (1600, 900), "逃げろ！こうかとん")
    screen.disp.blit(screen.image, (0,0))

    # 練習3
    tori = Bird("fig/3.png", 2, (900, 400))
    screen.disp.blit(tori.image, tori.rect)               # こうかとん画像用のSurfaceを画面用Surfaceに貼り付ける
    toris = pg.sprite.Group()
    toris.add(Bird("fig/3.png", 2, (900, 400)))

    # 練習5
    bomb = Bomb((255, 0, 0), 10,(+2, +2), screen)                     # 爆弾用のSurface
    screen.disp.blit(bomb.image, bomb.rect)                   # 爆弾用のSurfaceを画面用Surfaceに貼り付ける

    bombs = pg.sprite.Group()
    for i in range(5):
        bombs.add(Bomb((255, 0, 0), 10,(+i+1, +i+1), screen))
    
    score = Score(80)
    screen.disp.blit(score.txt, (0, 0))
    
    while True:
        # 練習2
        screen.disp.blit(screen.image, (0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT: return       # ✕ボタンでmain関数から戻る

        # 練習4
        toris.update(screen)
        #screen.disp.blit(tori.image, tori.rect)
        toris.draw(screen.disp)

        # 練習6
        bombs.update(screen)
        #screen.disp.blit(bomb.image, bomb.rect)
        bombs.draw(screen.disp)
        
        # 練習8
        if len(pg.sprite.groupcollide(toris, bombs, False, False)) != 0: return

        score = Score(80)
        screen.disp.blit(score.txt, (0, 0))

        pg.display.update()  # 画面の更新
        clock.tick(1000) 
    
# 練習7
def check_bound(sc_r, obj_r): # 画面用Rect, ｛こうかとん，爆弾｝Rect
    # 画面内：+1 / 画面外：-1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right  < obj_r.right : x = -1
    if obj_r.top  < sc_r.top  or sc_r.bottom < obj_r.bottom: y = -1
    return x, y


if __name__ == "__main__":
    pg.init() 
    main()
    pg.quit()
    sys.exit()