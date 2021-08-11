def SortTuple(tup):
    n = len(tup)

    for i in range(n):
        for j in range(n - i - 1):

            if tup[j][0] > tup[j + 1][0]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]
    return tup


tup = [("Ama", 20), ("mqni", 32), ("Anna", 25),
       ("Niru", 21), ("Chiru", "D"), ("denny", 22)]
print(SortTuple(tup))

test_tup = (10, 14, 15, 18, 80)

# printing original tuple
print("The original tuple : " + str(test_tup))

N = int(input("value to be checked:"))
res = False
for ele in test_tup:
    if N == ele:
        res = True
        break
print("Does contain required value ? : " + str(res))