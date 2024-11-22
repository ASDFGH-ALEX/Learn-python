list1=[32,22,43,56,78]
list2=[12,19,65,46,43]
print("Enter list1 ",list1)
print("Enter list2",list2)
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    elif i%2!=0:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list=even_list+odd_list
print("merged list",merged_list)


