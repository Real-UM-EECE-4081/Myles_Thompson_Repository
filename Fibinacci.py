#nterms = int(input("Whats number is the limit? "))

# first two terms
nterms=0
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# generate fibonacci sequence
#if :
print("Fibonacci sequence:")
while n1 < 50:
   print(n1)
   nth = n1 + n2
   # update values
   n1 = n2
   n2 = nth
