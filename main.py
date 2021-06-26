#무한 if문에 감옥
import os 
from time import sleep as s
import random
def clear():
    return os.system("clear")
running = True

list_for_random_p = ["strik", "strik", "strik", "ball", "fly out", "hit", "homerun", "ground ball"]
list_for_random_h = ["strik", "strik" "ball", "fly out", "hit", "homerun", "ground ball"]
gong_su = "su "
strik = 0
ball = 0
out = 0

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
                if out == 3: 
                    print("공수 교대")
                    s(2)
                    clear()
        else:
            s(0.5)
            clear()
    elif a == "log out":
        running = False

print("끝!") 
clear()

#야구 게임