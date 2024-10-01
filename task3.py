import random 
import string

pw=int(input("Enter the length of password : "))

l=string.ascii_lowercase
u=string.ascii_uppercase
n=string.digits
s=string.punctuation

collection=l+u+n+s
var=random.sample(collection,pw)
password="".join(var)
print(password)