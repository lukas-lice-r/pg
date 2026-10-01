"""
def add(a ,b):
    c = a + b
    return c

def mul(a, b, c):
    d = a * b * c
    print(d)





if __name__ == "__main__":
#    x = add(int(input()), int(input()))

    mul(1, 1, 1)

    import time


    g = 5
    c = 5

    q = g + c
    time.sleep(2)
    print(q)
"""
import time
# import keyboard

dict = {"ab" : int(1),
        "ac" : int(2),
        "ad" : int(3)
        }

# print(dict["ab"])
smg = True
while smg:
    time.sleep(1)
    print("ahoj")
    print("y/n")
    dd = input()

    if dd == "y":
        print("ano")
        smg = False
    elif dd == "n":
        print("ne")
    else:
        print("spatne")



#    keyboard.is_pressed("q"):
#    smg = False

