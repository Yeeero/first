import pygame
import random
import time
from pygame.locals import *
#基类
class Base(object):
    def __init__(self,x,y,screen,files):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(files);
#飞机基类
class BasePlane(Base):
    def __init__(self,x,y,screen,files):
        Base.__init__(self,x,y,files)
        self.bullet_list = []
    #映射飞机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    #映射子弹
    def display_bullet(self):
        for bullet in self.bullet_list:
            bullet.display()
            if bullet.judge():
                self.bullet_list.remove(bullet)#删除越界子弹
#子弹基类               
class BaseBullet(Base):
    def __init__(self,screen,x,y,files):
        Base.__init__(self,x,y,files)
       #子弹越界判断
    def judge(self):
        if self.y < 0 or self.y > 850 or self.x < 0 or self.x > 480:
            return True
        else:
            return False
class HeroPlane(BasePlane):
    def __init__(self,screen,files):
        BasePlane.__init__(self,200,710,screen,files)
    #飞机左移
    def moveLeft(self):
        self.x -= 5
    #飞机右移
    def moveRight(self):
        self.x += 5
    #飞机发射子弹
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x + 40, self.y - 20))

class EnemyPlane(BasePlane):
    def __init__(self,screen,files):
        BasePlane.__init__(self,0,0,screen,files)
        self.direction = "right"
    def move(self):
        self.y += 1
        if self.x > 430:
            self.direction = "left"
        if self.x <= 0:
            self.direction ="right"
        if self.direction == "right":
            self.x += 5
        else:
            self.x -=5

    def fire(self):
        r = random.randint(1,100)
        if r ==1 or r == 20:
            self.bullet_list.append(Bullet(self.screen, self.x + 25, self.y + 40))
class Bullet(BaseBullet):
    def __init__(self,screen,x,y):
        BaseBullet.__init__(self,screen,x,y,"./feiji/bullet.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.y -= 10
        
class EnemyBullet(BaseBullet):
    def __init__(self,screen,x,y):
        BaseBullet.__init__(self,screen,x,y,"./feiji/bullet1.png")
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.y += 10
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
                hero1.fire()

def main():
    #创建窗口
    screen=pygame.display.set_mode((480,852),0,32)
    #创建一个背景图片
    background = pygame.image.load("./feiji/background.png")
    #创建一架飞机
    files = "./feiji/hero1.png"
    hero1 = HeroPlane(screen,files)
    #创建敌方飞机
    e_files0="./feiji/enemy0.png"
    enemy0 = EnemyPlane(screen,e_files0)
    while True:
        #映射背景图
        screen.blit(background,(0,0))
        #映射己方飞机
        hero1.display()
        #映射子弹
        hero1.display_bullet()
        #映射敌方飞机
        enemy0.display()
        enemy0.move()
        enemy0.fire()
        enemy0.display_bullet()
        #更新界面图
        pygame.display.update()
        keyboard_event(hero1)
        time.sleep(0.01)

if  __name__=="__main__":
    main()
