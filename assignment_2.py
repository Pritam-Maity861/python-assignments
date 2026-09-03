# Assigment 2: Write a python program to create your own version of copy.deepcopy method 

list1=[10, 20, "Test", None, 3.2, [10, [40, [60, [90]]]]]

def MyDeepCopy(data):
    if not isinstance(data, list):
        return data
    mylist=[]
    for item in data:
        print(item)
        mylist.append(MyDeepCopy(item))
    return mylist

result=MyDeepCopy(list1)
result[5][1][1][0] = 121
print("original list-->",list1)
print("deepcopy version-->",result)