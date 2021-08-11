# Break statement inside for loop
my_list = ['Nanu', 'Nenu', 'budivantha', 'upitu', 'Super', 'hollywood']

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'hollywood':
        print('Found the name Super')
        break
        print('After break statement')

#Continue inside nested loop

print('Loop is Terminated')

 # Pass statement in for-loop
test_list = ["Guru","Maro","Charu","bar","haru"]
for i in test_list:
      if i == 'Charu':
        print('Gate Pass executed')
        pass
        print(i)



for i in range(4):
    for j in range(4):
        if j==2:
            continue
        print("The number is ",i,j);

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")