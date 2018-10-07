
# import re to remove whitespace from input
import re

# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep
 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')


def fix(n, num):
    # m is used to concatenate all characters between operators.
    m = ""
    # n represents the index of num.
    while n < len(num):
        # This regresive counter mimics the pointer of num that moves to the left.
        n = n - 1
        # If the condition below is satisfied, it means that the pointer is located at the very beginning of num.
        if n == 0:
            # n2 is the position where the concatenated characters will be inserted.
            n2 = n
            # Inside this while statement occurs the concatenation of characters until the pointer detects an operator.
            while (num[n] != '*' and num[n] != '/' and num[n] != '+' and num[n] != '-'):
                m = m + num[n]
                n = n + 1
            # Here the concatenated characters are inserted and the rest is deleted.
            num.insert(n2,m)
            del num[n2+1:len(m)+n2+1]
            # This regresive counter is necessary, because the size of num changes constantly.
            n = n - (len(m)-1)
            m = ""
        # The rest of the code inside the fix() method does basically the same thing.    
        if (num[n] == '*' or num[n] == '/' or num[n] == '+' or num[n] == '-'):
            while n < len(num): # contn < 2
                n = n + 1
                n2 = n
                m = ""
                while (num[n] != '*' and num[n] != '/' and num[n] != '+' and num[n] != '-'):
                    m = m + num[n] 
                    n = n + 1
                    # This conditional statement allows the insertion of concatenated characters (m) even if there isn't an operator. 
                    if n == len(num):
                        break   
                if n == len(num):
                    num.insert(n2,m)
                    del num[n2+1:len(m)+n2+1]
                    break
                else:
                    if num[n] == '*' or num[n] == '/' or num[n] == '+' or num[n] == '-':  
                        num.insert(n2,m)
                        del num[n2+1:len(m)+n2+1] 
                        n = n - (len(m)-1)
    return num

def calculate(num):
    try:
        n = 0
        while n <= len(num)-1:
            # if the multiplication sign is found the characters (previously converted to float) multiply each other. The same apllies for /, +, and -
            if num[n] == '*':
                mult = float(num[n-1])*float(num[n+1])
                num.remove(num[n-1])
                num.remove(num[n-1])
                num.remove(num[n-1])
                num.insert(n-1, str(mult))
                # This regresive counter is useful in case there's another * right next to the previous operation.
                n -= 1
            n += 1    
        n = 0
        # This is the result from the code above: ['5.0', '+', '50.0', '/', '10']
        # print(num)
        while n <= len(num)-1:
            if num[n] == '/':
                div = float(num[n-1])/float(num[n+1])
                num.remove(num[n-1])
                num.remove(num[n-1])
                num.remove(num[n-1])
                num.insert(n-1, str(div))
                n -= 1
            n += 1
        n = 0
        # ['5.0', '+', '5.0']
        # print(num)
        while n <= len(num)-1:
            if num[n] == '+':
                suma = float(num[n-1])+float(num[n+1])
                num.remove(num[n-1])
                num.remove(num[n-1])
                num.remove(num[n-1])
                num.insert(n-1, str(suma))
                n -= 1
            else:
                if num[n] == '-':
                    res = float(num[n-1])-float(num[n+1])
                    num.remove(num[n-1])
                    num.remove(num[n-1])
                    num.remove(num[n-1])
                    num.insert(n-1, str(res))
                    n -= 1
            n += 1 
                 
        print("\nAnswer: "+num[0])
    except ZeroDivisionError:
        while res != '':
            print("\nDivision by zero it's not valid, try again.")
            print("\nPress ENTER To Continue.")
            res = input()
        sleep(0.5)
        clear()
        main()

def main():
    print("\nAllowed Operations:")
    print("=> Addition(+)")
    print("=> Subtraction(-)")
    print("=> Multiplication(*)")
    print("=> Division(/)")
    # The user can insert multiple operations like: 2*2.5+10*5/10
    num = input("\n: ")
    # The sub method removes whitespace if there's any. After a couple tries, the programs seems to work just fine, but just in case, it is recommended to leave it.
    num = re.sub('[\num ]', '', num)
    # num is then converted to list: ['2', '*', '2', '.', '5', '+', '1', '0', '*', '5', '/', '1', '0'] 
    num = list(num)
    n = 0
    print("")
    # print(num)
    while n <= len(num)-1:
        # This conditional statement determines if the fix() method (below) must be used or not.
        if num[n] == '.' or num[n] == '*' or num[n] == '/' or num[n] == '+' or num[n] == '-':
            # This fix method puts together all the characters between operators so the operations can be done. This is the final result: ['2', '*', '2.5', '+', '10', '*', '5', '/', '10']
            fix(n, num)
            break
        n += 1
    # The method calculate() is in charge of doing addition, substraction, multiplication, and division. 
    calculate(num)

global res

res = ''
                      
while (res == ''):
    try:
        # In main() the users input the desired operation.
        main()
        res = input("\nPress ENTER To Continue.\n")
        sleep(0.5)
        clear()
    except:
        # This part is just in case the user inputs something else accidentally.
        while res != '':
            print("\nSomething went wrong, try again.")
            res = input("\nPress ENTER To Continue.\n")
        sleep(0.5)
        clear()
        main() 
   
    
        
                


