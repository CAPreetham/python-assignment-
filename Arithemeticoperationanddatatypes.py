print('hi this is Preetham  lets do arthmetic operations ')

#Arthemetic operation
a=10
b=5.5
c="sum"
list1  = [1, "hi", "Python", 2]
tup  = ("hi", "Python", 2)



print("sum")
print(a / b)
print(a+b)
print(a-b)
print(a%b)
print(a+b)
print(a**b)
print(type(a))
print(type(b))
print(type(c))

#list operations

list1  = [1, "hi", "Python", 2]
print(type(list1))

tup  = ("hi", "Python", 2)


#tuples operation
print (tup + tup)

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}

print("1st name is " + d[1])
print("2nd name is " + d[4])

print(d.keys())
print(d.values())

#sets operations

Months = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print('months')
print("\nAdding other months to the set...");
Months.add("July");
Months.add ("August");
print("\nPrinting the modified set...");
print('Months')
print("\nlooping through the set elements ... ")
for i in Months:
    print(i)

