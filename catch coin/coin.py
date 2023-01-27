import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

hedgehog = Actor("hedgehog")
hedgehog.pos = 300, 300

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")        # 배경색깔

    # 이미지를 화면에 그림
    fox.draw()
    hedgehog.draw()
    coin.draw()

    # 문자를 화면에 그림
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Finale Score: " + str(score), topleft=(10, 10), fontsize=60)

def on_mouse_down(pos):
    if game_over:
        quit()

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def time_up():
    global game_over
    game_over = True

def update():
    global score

    # 여우가 움직이는 동작, 키보드 방향키
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2


    if keyboard.w:
        hedgehog.y = hedgehog.y - 2
    elif keyboard.a:
        hedgehog.x = hedgehog.x - 2
    elif keyboard.s:
        hedgehog.y = hedgehog.y + 2
    elif keyboard.d:
        hedgehog.x = hedgehog.x + 2

    coin_collected = fox.colliderect(coin)
    coin_collected2 = hedgehog.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()

    if coin_collected2:
        score = score - 10
        place_coin()

clock.schedule(time_up, 60.0)            # 써져있는초(60.0초) 후에 타임업
place_coin()
pgzrun.go()