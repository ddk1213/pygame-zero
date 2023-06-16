import pgzrun
import random

# This sets the font color of the message that is displaed at the end of the game.
FONT_COLOR = (255, 255, 255)

# These constants define the size of he game window.
WIDTH = 800
HEIGHT = 600

CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)   # ()is called tuple and when you insert certain number, it will never change.
FINAL_LEVEL = 6                 # This constant defines the number of levels in the game.
START_SPEED = 5                 # This sets the speed at which the stars move down the screen. Higher numbers are slower.
COLORS = ["green", "blue"]      # This line sets the color of the stars that should not be clicked.

# These variables will keep track of if the game is over or not.
game_over = False
game_complete = False
current_level = 1               # This variable will keep track of what level the player's on.

# These lists wil keep track of the stars on the screen.
stars = []
animations = []

redindexnumber = 0

change = 0

def draw():
    global stars, current_level, game_over, game_complete       # These are the global variables used in this function.

    screen.clear()
    screen.blit("space", (0, 0))                                # This adds a background image to the game window.

    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    else:
        for star in stars:                  # drawing stars in list "stars" from index number from small to large numbers.
            star.draw()

def update():                                   # update 함수
    global stars, change
    if len(stars) == 0:                                      # This checks if any stars have been created yet. "len" is the length of the list.
        stars = make_stars(current_level)                    # If the stars list is empty, this function is called.
    
    # print(stars[0].y)                         # This code prints a y value of index number 0 in "stars" list.

    if(change == 0):
        if stars[0].y > 250:
            randomindex = random.randint(0, current_level)
            
            tmp = stars[redindexnumber].x
            stars[redindexnumber].x = stars[randomindex].x
            stars[randomindex].x = tmp
            change = 1

def make_stars(number_of_extra_stars):
    global change
    colors_to_create = get_colors_to_create(number_of_extra_stars)      # This returns a list of colors that will be used to draw the stars.
    new_stars = create_stars(colors_to_create)                          # This function uses the list of colors as a parameter and creates Actors for each star.
    layout_stars(new_stars)                                             # This fuction puts the stars in the right position on the sceen.
    animate_stars(new_stars)                                            # This function makes the stars move down the sceen.
    
    change = 0

    return new_stars                                                    

def get_colors_to_create(number_of_extra_stars):
    global redindexnumber
    colors_to_create = ["red"]                      # This makes the first star in the list red.                             
    for i in range(0, number_of_extra_stars):       # i refers to the current number in the range.
        random_color = random.choice(COLORS)        # This chooses a random color from the list for each additional star.
        colors_to_create.append(random_color)       # This adds the new color to the list.

    random.shuffle(colors_to_create)                # This suffles the random position of the list.
    # print(colors_to_create)
    # print(colors_to_create.index('red'))
    redindexnumber = colors_to_create.index('red')
    # print(redindexnumber)

    return colors_to_create

def create_stars(colors_to_create):             
    new_stars = []                                  # This list will store the nww stars that are created.
    for color in colors_to_create:                  # This loops over the colors_to_create list.
        # print(color)
        star = Actor(color + "-star")               # This combines the two strings.
        new_stars.append(star)  

    return new_stars                                # This returns the updated new_stars list.

def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1       # This calculates the number of gaps on the screen.
    gap_size = WIDTH / number_of_gaps               # This devides the width of the screen by the number of gaps.
    # random.shuffle(stars_to_layout)                 # This suffles the random position of the list.
    for index, star in enumerate(stars_to_layout):  # enumerate(list). If you cannot understand it, execute the code in lines 86~88.
        # print(index, star)
        new_x_pos = (index + 1) * gap_size          # This block sets the position of the current star along the x-azis by multiplying 
                                                    # the position of the star in the list by the sixe of the gap.
        star.x = new_x_pos                          # Setting position


# a = ['thse', 23, 1, 'fas']
# for index, value in enumerate(a):
#     print(index, value) 

def animate_stars(stars_to_animate):
    for star in stars_to_animate:       
        duration = START_SPEED / current_level          # Increasing the speed of star as the level increases.
        star.anchor = ("center", "bottom")              # This sets the star's anchor at the bottom of the star image.
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)        # This calls the handle_game_over() 
                                                                                                    # function when the animation is complete.
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()

def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)                 # This function stops the animations when the player clicks a red star.
    
    if current_level == FINAL_LEVEL:            
        game_complete = True
    else:
        current_level = current_level + 1       
        stars = []              # These blocks reset the stars and the animations on screen.
        animations = []         # 

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color=FONT_COLOR)

pgzrun.go()

# Things to add in this game
# Replacing the red star with other stars and changing the color of original star while stars are comming down.
