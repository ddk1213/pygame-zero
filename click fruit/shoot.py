import pgzrun
from random import randint


apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
score = 0

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()

def replacee():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

# 지금 막히는 부분은 score가 사과를 클릭할때마다 1점식 늘게 하는것과, 죽고 나서 최동 score를 나오게 하는것이다. (형 변환 참고)


def on_mouse_down(pos):
    global score

    if apple.collidepoint(pos):         # 사과를 클릭하게 되면 "Good shot!"이라고 나오게 하는 코드
        score += 1
        print("Good shot!")
        replacee()
    else:
        score = str(score)
        print("You mised!")
        print("score: " + score)
        quit()                          # 강제종료

replacee()
pgzrun.go()
