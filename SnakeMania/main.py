from turtle import *
from random import randrange
from freegames import square, vector

# Initialize the food position and snake with a single segment
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    # Ensure the snake cannot move directly opposite its current direction
    if (aim.x != -x) and (aim.y != -y):
        aim.x = x
        aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    # Check if the snake collided with the boundaries or itself
    if not inside(head) or head in snake:
        game_over()
        return

    snake.append(head)

    # Check if the snake ate the food
    if head == food:
        print('Snake Length:', len(snake))
        # Place new food at a random position
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # If the snake didn't eat the food, remove the tail segment
        snake.pop(0)

    # Clear the screen
    clear()

    # Draw the snake segments
    for body in snake:
        square(body.x, body.y, 9, 'black')

    # Draw the food
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

def game_over():
    "Display game over message and exit gracefully."
    # Mark the head of the snake in red
    square(snake[-1].x, snake[-1].y, 9, 'red')
    update()
    print('Game Over! Your final score:', len(snake))
    bye()  # Close the turtle graphics window

# Set up the game window
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Change title to "Snakemania"
title("Snakemania")

# Assign arrow key controls
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Start the game loop
move()

# Start the turtle graphics event loop
done()
