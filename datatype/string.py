# barinda = str("hello world");

# print(barinda);

# data = list(("barinda","system","sylvere"));
# print(type(data))


# data = tuple(("barinda","system","sylvere"));
# print(type(data))

# x = dict(name="barindaaa",age=36);
# print(x);



thisList = ["apple","banana","cherry","apple","cherry"];
print(len(thisList))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


listbarinda = ["abc", 34, True, 40, "male"]

    
newList = [x for x in listbarinda if isinstance(x, str)]
newNumber = [ item for item in listbarinda if isinstance(item, int)];



print("the string values :", newList);
print("the numbers values :", newNumber);

# for item in listbarinda:
    
  
#     print(item)






# print(list1,list2,list3)