#무한 if문에 감옥
import os 
from time import sleep as s
import random
def clear():
    return os.system("clear")
running = True

list_for_random_p = ["strik", "strik", "ball", "fly out", "hit", "homerun", "ground ball"]
list_for_random_h = ["strik", "strik", "ball", "fly out", "hit", "homerun", "ground ball"]
gong_su = "su"
strik = 0
ball = 0
out = 0
my_score = 0
away_score = 0

first = False
second = False
Third = False
while running:
    a = input("입력해 주세요: ")
    if a == "s":
        s(0.1)
        result = random.choice(list_for_random_p)
        print(result)
        if result == "strik":
            strik += 1
            s(0.5)
            clear()
            if strik == 3:
                out += 1
                strik = 0
                print("out")
                s(1)
                clear()

        elif result == "ball":
            ball += 1
            s(0.5)
            clear()
            if ball == 4:
                print("주자 1루")
                first = True
                s(1)
                clear()
                ball = 0

        elif result == "fly out":
            out += 1
            s(0.5)
            clear()  

        elif result == "homerun":
            if gong_su == "su":
                away_score += 1
                s(0.5)
                clear()
            elif gong_su -- "gong":
                my_score += 1
                s(0.5)
                clear()
        else:
            s(0.5)
            clear()

    elif a == "log out":
        running = False

    elif a == "out":
        print(out)

    elif a == "gong su":
        print(gong_su)

    elif a == "score":
        print(f"{my_score} : {away_score}")

    if out == 3: 
        print("공수 교대")
        s(2)
        clear()
        strik = 0
        ball = 0
        out = 0
        if gong_su == "su":
            gong_su = "gong"
        elif gong_su == "gong":
            gong_su = "su"

print("끝!") 
clear()

#야구 게임