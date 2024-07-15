logo = """
   __       _ _   _          __    __ _       
  /__\ ___ | | | | |_ ___   / / /\ \ (_)_ __  
 / \/// _ \| | | | __/ _ \  \ \/  \/ / | '_ \ 
/ _  \ (_) | | | | || (_) |  \  /\  /| | | | |
\/ \_/\___/|_|_|  \__\___/    \/  \/ |_|_| |_|
"""

import re
import random
import operator
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def evaluate_expression(expression):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    result = expression[0]
    for i in range(1, len(expression), 2):
        op = ops[expression[i]]
        b = expression[i + 1]
        result = op(result, b)

    return result
finished = False
while finished != True:
    clear()
    print(logo)
    u_roll = input("What would you like to roll?:\n").lower()
    u_list = u_roll.split(" ")
    #print(u_list)

    d_list =[]
    for item in u_list:
        if "d" in item:
            loop = 0
            ran_num = 0
            number, dice = item.split('d')
            loop = int(number)
            while loop > 0:
                ran_num += int(random.randint(1,int(dice+1)))
                loop -= 1
            d_list.append(ran_num)     
        elif "+" in item or "-" in item:
            d_list.append(item)
        elif "d" not in item and "+" not in item:
            d_list.append(item)
    print(d_list)
    result = evaluate_expression(d_list)
    print(result)
    answer = input("Would you like to roll again? Y/N: ").lower()
    if answer == "y":
        finished = False
    else:
        finished = True


#print(d_list)

result = evaluate_expression(d_list)
print(result)
