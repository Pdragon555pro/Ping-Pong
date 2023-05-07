from pygame import *  
score1 = 0 
score = 0 
#класс-родитель для спрайтов   
class GameSprite(sprite.Sprite):  
    #конструктор класса  
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): # добавить еще два параметра при создании и задавать размер прямоугольгника для картинки самим  
        super().__init__()  
   
        # каждый спрайт должен хранить свойство image - изображение  
        self.image = transform.scale(image.load(player_image), (wight, height))  
        self.speed = player_speed  
   
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан  
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   
    def reset(self):  
        window.blit(self.image, (self.rect.x, self.rect.y))  
#класс-наследник для спрайта-игрока (управляется стрелками)  
class Player(GameSprite):  
    def update_r(self):  
        keys = key.get_pressed()  
        if keys[K_UP] and self.rect.y > 5:  
            self.rect.y -= self.speed  
        if keys[K_DOWN] and self.rect.y < win_height - 200:  
            self.rect.y += self.speed  
    def update_l(self):  
        keys = key.get_pressed()  
        if keys[K_w] and self.rect.y > 5:  
            self.rect.y -= self.speed  
        if keys[K_s] and self.rect.y < win_height - 200:  
            self.rect.y += self.speed  
   
#звуки  
# mixer.init()  
# vois = mixer.Sound('vois.ogg')
# vois.set_volume(0.2)  
   
#Игровая сцена:  
back = (0, 128, 0) # цвет фона (background)  
win_width = 900 
win_height = 750  
window = display.set_mode((900, 750))  
window.fill(back) 
 
#флаги отвечающие за состояние игры  
game = True
finish = False
clock = time.Clock()  
FPS = 120 
 
#создания мяча и ракетки      
racket1 = Player('Wawe.png', 30, 200, 9, 20, 200) # при созданни спрайта добавляется еще два параметра  
racket2 = Player('Wawe.png', 850, 200, 9, 20, 200)  
ball = GameSprite('tennis.png', 200, 200, 4, 50, 50) 
 
font.init() 
font2 = font.SysFont('Arial', 36)  
font = font.SysFont('Arial', 35)  
lose1 = font.render('ПЕРВЫЙ ИГРОК ПРОИГРАЛ!', True, (150, 200, 0))  
lose2 = font.render('ВТОРОЙ ИГРОК ПРОИГРАЛ!', True, (150, 200, 0))  
 
speed_x = 5 
speed_y = 5
while game: 
    for e in event.get():  
        if e.type == QUIT:  
            game = False

    if finish != True: 
        window.fill(back)  
        racket1.update_l()  
        racket2.update_r()  
        ball.rect.x += speed_x  
        ball.rect.y += speed_y
   
        if sprite.collide_rect(racket1, ball):  
            speed_x *= -1 
            speed_y *= 1 
            score += 1
            # vois.play()
        if sprite.collide_rect(racket2, ball):
            speed_x *= -1 
            speed_y *= 1 
            score1 += 1 
            # vois.play()
            
        # если мяч достигает границ экрана меняем направление его движения  
        if ball.rect.y > win_height-50 or ball.rect.y < 0:  
            speed_y *= -1  
 
        # если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока  
        if ball.rect.x < 0:  
            finish = True
            ball.kill()
            time.delay(3000)
            finish = False
            window.blit(lose1, (280, 200))
            score1 = 0 
            score = 0 
            ball = GameSprite('tennis.png', 500, 200, 4, 50, 50)

        # если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока  
        if ball.rect.x > win_width:  
            finish = True
            ball.kill()
            time.delay(3000)
            window.blit(lose1, (280, 200))
            finish = False
            score1 = 0 
            score = 0
            ball = GameSprite('tennis.png', 200, 200, 4, 50, 50)
            # window.blit(lose1, (280, 200)) - над этим надо подумать но если что исправляйте

        text = font.render("Счет: " + str(score), 1, (150, 200, 0)) 
        window.blit(text, (10, 20)) 
        text1 = font.render("Счет: " + str(score1), 1, (150, 200, 0))
        window.blit(text1, (750, 20)) 
 
        racket1.reset()  
        racket2.reset()  
        ball.reset()
        
    display.update()
    clock.tick(FPS)