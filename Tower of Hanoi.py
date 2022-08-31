
def TowerOfHanoi(n, source, destination, auxiliary,moves=0):

    if n == 1:
        print("Move disk 1 from source", source, "to destinationn", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)

    TowerOfHanoi(n - 1, auxiliary, destination, source)


# Driver code
print("How many disk do you want?")
n=4
#n = input()
TowerOfHanoi(int(n), 'A', 'B', 'C')