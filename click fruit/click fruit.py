import pgzrun
from random import randint

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
score = 0

FONT_COLOR = (255, 255, 255)

game_over = False

WIDTH = 800
HEIGHT = 600

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y) 

def update():
    global game_over, score
    if keyboard.r: 
        game_over = False
        score = 0

def draw():
    global game_over
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()

    if game_over:
        display_message("GAME OVER!", "Score : " + str(score), "Press 'r' key to restart")

def handle_game_over():
    global game_over
    game_over = True

def replace():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

def display_message(heading_text, sub_heading_text, reset_game):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR, owidth=0.5, ocolor="red")
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color=FONT_COLOR, owidth=0.5, ocolor="red")
    screen.draw.text(reset_game, fontsize=40, center=(CENTER_X, CENTER_Y + 55), color=FONT_COLOR, owidth=0.5, ocolor="blue")

def on_mouse_down(pos):
    global score

    if(not(game_over)):
        if apple.collidepoint(pos):         # 사과를 클릭하게 되면 "Good shot!"이라고 나오게 하는 코드
            score += 1
            replace()
        else:
            handle_game_over()                          # 게임 종료

replace()
pgzrun.go()
