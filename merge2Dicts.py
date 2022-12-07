def mergeDicts(x,y):
    x.update(y)
    return x

dictionary1 = {
    1:"a",2:"b",3:"c"
}
dictionary2 = {
    4:"d",5:"e",6:"f"
}
print(mergeDicts(dictionary1,dictionary2))
