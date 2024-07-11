def logical(x):
    if x == 1:
        return 1
    else:
        return(x + logical(x-1))
    
result = logical(3)
print(result)
