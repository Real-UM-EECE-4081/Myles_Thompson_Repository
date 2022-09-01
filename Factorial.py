
def factorials(b):
    if b==0:
        return 1
    else:
        return b*factorials(b-1)
inp=int(input("Choose a number for factorial: "))
print(f'The factorial of {inp} is {factorials(inp)}')