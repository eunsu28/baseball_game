import os 
from time import sleep as s
def clear():
    return os.system("clear")

running = True
while running:
    a = input("입력해 주세요: ")
    print("a")
    s(1)
    clear()
    if a == "log out":
        running = False

print("끝!")
