# #map
# #map(function,iter(list,tuple,set,dicionary))
# def maultiply(num):
#     return num*num
# result=map(multiply,(2,4,6,8))
# print(tuple(result))


# #map(function,iter(list,tuple,set,dicionary))
# def multiply(num):
#     return num*num
# #result=map(multiply,(2,4,6,8))
# result=map(lamda i:i*i, (2,4,6,8))
# print((tuple((result))))


##########


def toUpper(str): 
    return str.upper()
res=map(toUpper,("software","sem","3"))
# print(list(res))


newlist=list(res)
newlist.append("HEY")
print(newlist)
# newlist=tuple(res)
# newlist.append("HEY tuple")
# print(newlist)

dict_item={"a":"Car","b":"Bike","c":"Train"}
a=map(lambda i:(i[0]+"__",i[1]+"y"),dict_item.items())
print(dict(a))

dict_item={"a":"Car","b":"Bike","c":"Train"}
a=map(lambda i:(i[0]+"__",i[1]+"d"), dict_item())
print(dict(a))


