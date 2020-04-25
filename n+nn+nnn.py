#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
a = int(input("Input an integer : "))
n1 = int( "%i" % a )
n2 = int( "%i%i" % (a,a) )
n3 = int( "%i%i%i" % (a,a,a) )
print (n1+n2+n3)
raw_input("Press Enter ")
