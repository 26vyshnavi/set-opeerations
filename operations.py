#union of lists

def union(list1 , list2):
final_list = list(set(list1) | set(list2))
return final_list
list1 = [0,1,2,3,4,5,6]
list2 = [4,5,6,8]
print(union(lists1, lists2))


#intersection of lists

def intersection(list1,list2):
return list(set(list1) & set(list2))
list1 = [0,1,2,3,4,5,6,8]
list2 = [2,4,7,9]
print(intersection(list1, list2))


#difference of lists

def differnce(l1,l2):
return list(set(l1)-set(l2))+list(set(l2)-set(l1))
l1 = [0,1,2,3,4,5,6,8]
l2 = [1,2,3,4,5]


#symmetric differnce

list_1 = [0,1,2,3,5,9]
list_2 = [2,9,6,8]
print(list_1.symmetric_differnce(list_2))
