import os 
from time import sleep as s
import random
def clear():
    return os.system("clear")
running = True

list_for_random_p = ["strik", "strik", "strik", "ball", "fly out", "hit", "homerun", "ground ball"]
list_for_random_h = ["strik", "strik" "ball", "fly out", "hit", "homerun", "ground ball"]
gong_su = "su"
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
            print(strik)
    elif a == "log out":
        running = False

print("끝!") 

#야구 게임