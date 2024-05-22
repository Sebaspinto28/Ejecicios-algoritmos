

def contador(hora,target):
    count=0
    for i in hora:
        if i >= target:
            count+=1
    return count
print(contador([1,2,3,4],2))