def coincidence(inputList, inputRange):
    if (inputList is None or inputRange is None):
        return []
    result = [x for x in inputList \
        if (isinstance(x,(float, int)) and \
        (x>=inputRange[0] and x<=inputRange[-1]))]    
    return result

print(coincidence([1,2,None,"jlakdj",5,3,6,range(10,100)],range(2,6)));
