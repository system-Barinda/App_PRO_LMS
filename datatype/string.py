# barinda = str("hello world");

# print(barinda);

# data = list(("barinda","system","sylvere"));
# print(type(data))


# data = tuple(("barinda","system","sylvere"));
# print(type(data))

# x = dict(name="barindaaa",age=36);
# print(x);



# thisList = ["apple","banana","cherry","apple","cherry"];
# print(len(thisList))


# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]


# listbarinda = ["abc", 34, True, 40, "male"]

    
# newList = [x for x in listbarinda if isinstance(x, str)]
# newNumber = [ item for item in listbarinda if isinstance(item, int)];



# print("the string values :", newList);
# print("the numbers values :", newNumber);

# for item in listbarinda:
    
  
#     print(item)


# print(list1,list2,list3)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# if "apple" in thislist:
#     print("yes, 'apple' is in the fruits list");
    
    

# student = ["barinda","system","sylvere","barinda","system","sylvere"];
# student1 = ["iradukunda","sandrine","audreille","isimbi"];

# student.extend(student1);
# print(student);

student = ["barinda","system","sylvere","barinda","system","sylvere"]

# for x in range(len(student)):
#     print(x,student[x])
    
 
 
# x = 0;
 
# while x < len(student):
#      print(x, student[x])
#      x += 1


# [print(x, student[x]) for x in range(len(student))];

# [print(x, student[x]) for x in range(len(student)) if student[x] == "barinda"];

# [print(item, student[item]) for item in range(len(student)) if student[item] == "barinda"]


# def myfunc(n):
#     return n


# barinda = myfunc("hello world");

# print(barinda);


tamperature = 77;

celecius = (tamperature - 32) * 5 / 9

print("celecius tamperature: ", celecius);

