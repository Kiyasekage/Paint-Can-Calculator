import math
def can_needed(w,h):
    area = w*h
    can = math.ceil(area/4)
    print("Estimate amount of can : ",can)


print("Welcome to Painting Wall Calculator")
print("I assume that you're here to find out how many cans do you need..")
print("For your information, 1 can of paint can cover 4 square meters of wall")
name = input("What's your name?\n")
width = int(input(f"Input your wall width,{name} : "))
height = int(input(f"Input your wall height,{name} :"))
can_needed(width,height)
