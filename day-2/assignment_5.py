# assignment: 6 nums = [10, 20, "Test", None, 3.2, [10, [40, [60, [90]]]]] # Write a program to find out the sum of all these numbers # output = 10 + 20 + 3.2  + 40 + 60 + 90 =  233.2

nested_list=[10, 20, "Test", None, 3.2, [10, [40, [60, [90]]]]]

def total_sum(data):
    total=0
    for item in data:
        if isinstance(item,(int,float)):
            total+=item
        elif isinstance(item,list):
            total+=total_sum(item)
    return total

result=total_sum(nested_list)
print(result)
