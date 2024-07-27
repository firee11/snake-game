import turtle
import time
import os
from snake import Snake
from food import Food
from score import Score

log_files = os.listdir('./Logs')
PLACEHOLDER = "[name]"

for log_file in log_files:
    error_count = 0
    warning_count = 0   
    info_count = 0
with open(f'./Logs/{log_file}', 'r') as file:
    with open(f'./Reports/Report_for_{log_file}', 'w' ) as report_file:
        report_file.write(f'ERROR: {error_count}\n')
        report_file.write(f'WARING: {warning_count}\n')
        report_file.write(f'{info_count}\n')
        

    for line in file:
        if 'ERROR' in file:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif 'INFO' in line:
            info_count += 1
    
with open("./DraftingLetters-main/Contacts/names.txt", "r") as file:
    names=file.readlines()
    print(names)
with open("./storage/storage.txt", "r") as file:
    content = file.read()
    print(content)
with open("./storage/storage.txt", "w") as file:
    content = file.write("overwrite the file with this string")


with open("./DraftingLetters-main/Email/draft.txt", "r") as draft:
    draft_letter = draft.read()
    for name in names:
        name = name.strip()
        letter = draft_letter.replace(PLACEHOLDER, name)
        with open(f"./DraftingLetters-main/send/Letter_for_{name}.txt" , "w") as new_file:
            new_file.write(letter)
with open("./Contacts/names.txt" , "r") as file:
    names = file.readlines()
names = file.readlines()
snake = Snake()
food=Food()
score = Score()
ts = turtle.getscreen()
ts.screensize(600,600)
ts.bgcolor("black")
ts.title("Classic Snake Game")
ts.tracer(0)


ts.listen()
ts.onkey(snake.up , "Up")
ts.onkey(snake.down, "Down")
ts.onkey(snake.left, "Left")
ts.onkey(snake.right,"Right")
is_game_started = True

while True:
    snake.move()
    ts.update()
    time.sleep(0.1)
    
    if snake.head.distance(food) < 20:
        snake.extend()
        food.reposition()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    for segment in snake.segments:
       if segment == snake.head:
           pass
       elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

