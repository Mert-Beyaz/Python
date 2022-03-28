import random
coin = int(input("Enter the number of coins to drop..:"))
throw = 0
box_1 = 0
box_2 = 0
box_3 = 0
box_4 = 0
box_5 = 0
box_6 = 0
box_7 = 0
box_8 = 0
box_9 = 0
box_10 = 0
#The boxes represent the last place the coin fell. First, they all have 0 coins.
while throw != coin:
#The cycle must continue until the number of throws equals the number of coins.
    throw_number = 0
    left = 0
    while throw_number != 10: #Nine of those drops fall into the first box if left. Eight of these drops fall to the left, and one to the right, to the second box. If nine of these falls fall to the right, the tenth falls to the box.
        choose = random.randint(0, 1) #If we represent the event of falling to the left with 0, we also represent the event of falling to the right with 1.
        if choose == 0:
            left += 1
        throw_number += 1
    if left == 0:
         box_10 += 1
    elif left == 1:
         box_9 += 1
    elif left == 2:
         box_8 += 1
    elif left == 3:
         box_7 += 1
    elif left == 4:
         box_6 += 1
    elif left == 5:
         box_5 += 1
    elif left == 6:
         box_4 += 1
    elif left == 7:
         box_3 += 1
    elif left == 8:
         box_2 += 1
    else:
         box_1 += 1
    throw += 1
print("Number of coins in chamber 1 is...:", box_1)
print("Number of coins in chamber 2 is...:", box_2)
print("Number of coins in chamber 3 is...:", box_3)
print("Number of coins in chamber 4 is...:", box_4)
print("Number of coins in chamber 5 is...:", box_5)
print("Number of coins in chamber 6 is...:", box_6)
print("Number of coins in chamber 7 is...:", box_7)
print("Number of coins in chamber 8 is...:", box_8)
print("Number of coins in chamber 9 is...:", box_9)
print("Number of coins in chamber 10 is...:", box_10)

list = [box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10] #I put the boxes in a list to find out which box had the most coins.
line = 1
coin_in_box_1 = (box_1-(box_1-1))*"o" #I had to take the box variable and multiply it by one. I also wrote something like this so that it could be accepted.
coin_in_box_2 = (box_2-(box_2-1))*"o"
coin_in_box_3 = (box_3-(box_3-1))*"o"
coin_in_box_4 = (box_4-(box_4-1))*"o"
coin_in_box_5 = (box_5-(box_5-1))*"o"
coin_in_box_6 = (box_6-(box_6-1))*"o"
coin_in_box_7 = (box_7-(box_7-1))*"o"
coin_in_box_8 = (box_8-(box_8-1))*"o"
coin_in_box_9 = (box_9-(box_9-1))*"o"
coin_in_box_10 = (box_10-(box_10-1))*"o"
print("  ","|", "1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10|")
print("---+---+---+---+---+---+---+---+---+---+---+")
greater_box = 0
for i in list:
    if i >= greater_box:
        greater_box = i
while line != greater_box+1:
        if line >= 10:#The reason I use if here is because the histogram breaks down when there are two-digit numbers when printing. I leave extra space when I print single-digit numbers.
            if box_1 == 0: #If there is no coin in the box, I have set up such a system to write spaces, not 0.
                coin_in_box_1 = " "
            if box_2 == 0:
                coin_in_box_2 = " "
            if box_3 == 0:
                coin_in_box_3 = " "
            if box_4 == 0:
                coin_in_box_4 = " "
            if box_5 == 0:
                coin_in_box_5 = " "
            if box_6 == 0:
                coin_in_box_6 = " "
            if box_7 == 0:
                coin_in_box_7 = " "
            if box_8 == 0:
                coin_in_box_8 = " "
            if box_9 == 0:
                coin_in_box_9 = " "
            if box_10 == 0:
                coin_in_box_10 = " "
            print(line,"|",coin_in_box_1,"|",coin_in_box_2,"|",coin_in_box_3,"|",coin_in_box_4,"|",coin_in_box_5,"|",coin_in_box_6,"|",coin_in_box_7,"|",coin_in_box_8,"|",coin_in_box_9,"|",coin_in_box_10,"|")
            line += 1
            box_1 -= 1
            box_2 -= 1
            box_3 -= 1
            box_4 -= 1
            box_5 -= 1
            box_6 -= 1
            box_7 -= 1
            box_8 -= 1
            box_9 -= 1
            box_10 -= 1
        else:
            if box_1 == 0:
                coin_in_box_1 = " "
            if box_2 == 0:
                coin_in_box_2 = " "
            if box_3 == 0:
                coin_in_box_3 = " "
            if box_4 == 0:
                coin_in_box_4 = " "
            if box_5 == 0:
                coin_in_box_5 = " "
            if box_6 == 0:
                coin_in_box_6 = " "
            if box_7 == 0:
                coin_in_box_7 = " "
            if box_8 == 0:
                coin_in_box_8 = " "
            if box_9 == 0:
                coin_in_box_9 = " "
            if box_10 == 0:
                coin_in_box_10 = " "
            print(line," |",coin_in_box_1,"|",coin_in_box_2,"|",coin_in_box_3,"|",coin_in_box_4,"|",coin_in_box_5,"|",coin_in_box_6,"|",coin_in_box_7,"|",coin_in_box_8,"|",coin_in_box_9,"|",coin_in_box_10,"|")
            line += 1
            box_1 -= 1
            box_2 -= 1
            box_3 -= 1
            box_4 -= 1
            box_5 -= 1
            box_6 -= 1
            box_7 -= 1
            box_8 -= 1
            box_9 -= 1
            box_10 -= 1

print("---+---+---+---+---+---+---+---+---+---+---+")