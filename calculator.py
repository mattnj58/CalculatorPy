print('Enter the first number')
x = int(input())

print('Enter the second number')
y= int(input())

print('Enter the operation')
op = input()

# print('Enter the equation (with spaces')
# equation = input().split(' ')
# numbers = []
# ops = []

# for i in range(len(equation)):
#     if i%2==0:
#         numbers.append(int(equation[i]))
#         print(equation[i])
#     else:
#         ops.append(equation[i])
#         print(equation[i])


def calculate(x,y,op):
    if op=='+':
        return x + y
    elif op=='-':
        return x - y
    elif op=='*':
        return x * y
    elif op=='/':
        if y!=0:
            return x/y
        else:
            print("Error: unable to divide by 0")
            exit()
        

print("Answer is =",calculate(x,y,op))

