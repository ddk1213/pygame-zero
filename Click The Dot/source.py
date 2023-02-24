import pgzrun
from random import randint

WIDTH = 400     # 화면 넓이.
HEIGHT = 400       #화면 크기.

dots = []       # 빈 리스트를 한 이유는 하나 하나 10개까지 다 안쓰려고이다.
lines = []

next_dot = 0
timer = 0

for dot in range(0, 10):        # 10개까지 점을 반복.
    actor = Actor("dot")        # Actor은 images에 있는 사진을 찾는(정보를 가지고 오는) 함수.
    actor.pos = randint(20, WIDTH -20), randint(20, HEIGHT -20)     # ranint즉, 무작위로 함.
    dots.append(actor)      # append는 괄호안에 있는 값을 리스트 제일 뒤에 추가. 리스트 이름.append(추가할 값) => 무조건 맨 뒤에 추가.


def draw():

    screen.fill("black")            # 배경색 겁정으로 바꾸는 코드.
    number = 1                      # 어떤 숫자부터 시작할지 (이 코드에 경우는 1부터).
    for dot in dots:                # 반복문.
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))        # number를 str로 바꾸고 숫자들을 그림.
        dot.draw()                  # 점을 그리는 코드.
        number = number +1          # 숫자를 1개씩 늘리는 코드.

    for line in lines:            
        screen.draw.line(line[0], line[1], (255, 0, 0)) 

    screen.draw.text(str(round(timer, 2)), topleft=(10, 10), color=(255, 0, 0), fontsize=30)  


def on_mouse_down(pos):
    global next_dot
    global lines

    if(next_dot < 10):                          # 선이 그어진 수가 10 미만일때만 아래 코드들이 작동하게 함으로서 선을 다 귿고 다른곳을 클릭해도 종료가 안됨.
        if dots[next_dot].collidepoint(pos):           # 플레이어가 순서대로 클릭했는지 확인하는 코드
            if next_dot:                    # 첫번째 점을 클릭했는지 확인하는 
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))          # 두 점 사이의 선을 그려주는 코드
                sounds.ringing.play()
            next_dot = next_dot + 1         # next_dot += 1과 next_dot = next_dot + 1은 같다
        else:
            # 다른거 눌렀을때 초기화
            lines = []                 
            next_dot = 0

def update():
    global timer
    
    if(next_dot < 10):
        timer += 1 / 60

pgzrun.go()
