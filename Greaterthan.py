g=int(input("Choose a number: "))
print(g)
h=int(input("How many numbers do you want in your list?: "))
list=[]
for i in range(0,h):
    list.append(int(input(f'What do you want your {i+1} to be: ')))
print("List of numbers to check to see are greater than",list)
greaterthan=[]
for i in range(len(list)):
    if g<list[i]:
        greaterthan.append(list[i])
print("List of all numbers greater than your chosen number",greaterthan)
