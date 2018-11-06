import pygame
import time
from pygame.locals import *
class HeroPlane(object):
    def __init__(self,screen,files):
        self.x = 200
        self.y = 710
        self.image = pygame.image.load(files)
        self.screen = screen
        self.bullet_list = []
    def blitHero(self):
        self.screen.blit(self.image,(self.x,self.y))
    def moveLeft(self):
        self.x -= 5
    def moveRight(self):
        self.x += 5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
    def display_bullet(self):
        for bullet in self.bullet_list:
            bullet.display()
class Bullet(object):
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x + 40
        self.y = y - 20
        self.image = pygame.image.load("./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.y -= 10
def keyboard_event(hero1):
    #获取键盘事件等
    for event in pygame.event.get():
        #判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                #x -= 5
                hero1.moveLeft()
            #检测按钮是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                #x += 5
                hero1.moveRight()
            #检测是否是空格键
            elif event.key == K_SPACE:
                print("space")
                #飞机开火发射子弹
                bullet = hero1.fire()

def main():
    #创建窗口
    screen=pygame.display.set_mode((480,852),0,32)
    #创建一个背景图片
    background = pygame.image.load("./feiji/background.png")
    #创建一架飞机
    #hero1 = pygame.image.load("./feiji/hero1.png")
    #x=200
    #y=710
    files = "./feiji/hero1.png"
    hero1 = HeroPlane(screen,files)
    while True:
        #映射背景图
        screen.blit(background,(0,0))
        #映射己方飞机
        hero1.blitHero()
        #映射子弹
        hero1.display_bullet()
        pygame.display.update()
        keyboard_event(hero1)
        time.sleep(0.01)

if  __name__=="__main__":
    main()
