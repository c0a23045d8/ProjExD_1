import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    mx = (0)
    my = (0)
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # 背景画像Surfaceを作成
    fbg_img = pg.transform.flip(bg_img, True, False) # flipで反転した背景画像
    koukaton_3 = pg.image.load("fig/3.png")
    koukaton_3 = pg.transform.flip(koukaton_3, True, False)
    krect = koukaton_3.get_rect() #こうかとんRectを取得する
    krect.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200 #練習7-2
        screen.blit(bg_img, [-x, 0]) #screen surfaceに背景画像Surfaceを張り付ける
        screen.blit(fbg_img, [-x+1600 , 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(fbg_img, [-x+4800, 0])
        key_lst = pg.key.get_pressed()
        #演習前
        # if key_lst[pg.K_UP]:
        #     krect.move_ip((0, -1))
        # if key_lst[pg.K_DOWN]:
        #     krect.move_ip((0, +1))
        # if key_lst[pg.K_RIGHT]:
        #     krect.move_ip((+1, 0))
        # if key_lst[pg.K_LEFT]:
        #     krect.move_ip((-1, 0))
        # if not key_lst[pg.K_RIGHT]:
        #     krect.move_ip((-1, 0))
        #演習後
        my = (0)
        if not key_lst[pg.K_RIGHT]:
            mx = -1
        if key_lst[pg.K_UP]:
            my -= 1
        if key_lst[pg.K_DOWN]:
            my += 1
        if key_lst[pg.K_RIGHT]:
            mx += 1
        if key_lst[pg.K_LEFT]:
            mx -= 1
        krect.move_ip((mx, my))
        mx = 0
        my = 0
        screen.blit(koukaton_3, krect) #screen syrfaceにkoukatonイメージを張り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()