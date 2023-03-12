from pygame import *

win_width = 700
win_height = 500
FPS = 60

window = display.set_mode((win_width, win_height))
display.set_caption("Лабіринт")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class GameSprite():
    def __init__(self, player_image, width, height, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    def reset(self):
        window.blit(self.image, (self.x, self.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.y > 5:
            self.y -= self.speed
        if keys[K_s] and self.y < 405:
            self.y += self.speed
        if keys[K_d] and self.x < 605:
            self.x += self.speed
        if keys[K_a] and self.x > 5:
            self.x -= self.speed
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.x <= 450:
            self.direction = "right"
        if self.x >= win_width - 80:
            self.direction = "left"

        if self.direction == "left":
            self.x -= self.speed
        else:
            self.x += self.speed

class Wall():
    def __init__ (self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player("hero.png", 50, 50, win_height - 100, 5, 4)
monster = Enemy("cyborg.png", 50, 50, win_width - 150, 50, 2)
final = GameSprite("treasure.png", 100, 100, win_width - 50, win_height - 50, 0)

w1 = Wall(154, 205, 50, 100, 20, 530, 10)
w2 = Wall(154, 205, 50, 100, 480, 530, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 440, 20, 10, 360)
w5 = Wall(154, 205, 50, 260, 20, 10, 300)
w6 = Wall(154, 205, 50, 600, 20, 10, 370)
w7 = Wall(154, 205, 50, 350, 380, 10, 100)
w8 = Wall(154, 205, 50, 195, 285, 10, 200)
w9 = Wall(154, 205, 50, 350, 90, 10, 250)
w10 = Wall(154, 205, 50, 520, 200, 10, 280)

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

game = True
finish = False
clock = time.Clock()

font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN", True, (255, 215, 0))
lose = font.render("YOU LOSE", True, (255, 215, 0))

while game:
    for el in event.get():
        if el.type == QUIT:
            game = False
    
    if finish:
        window.blit(background, (0,0))
        player.reset()
        monster.reset()
        final.reset()
        player.update()
        monster.update()
    
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
    
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10):
        finish = True
        window.blit(lose, (200,200))

    display.update()
    clock.tick(FPS)