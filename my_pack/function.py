#func1
def in_array (num1, num2, num3) :
    array = [num1,num2,num3]
    big =  bigger(array)
    return big

#func2
def bigger (array) : # 5,3,9

    big = array[0]
    i = 0
    for x in array :
        if big  < array[i] :
            big =array[i]
        i+=1
    return big


#func3
def sender (num) :
    printer(num)

#func 4

def printer(num) :
    print(num)
