


#-------------------------------------
#---------- Iterable vs Iterator-----
#--------------------------------------
# Iterable
# [1] Object Contains Data That can be Iterated Upon
# [2] Examples (String , Tuple , Dictionary , Set , List)
#----------------------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next () Method Return 1 Element At A Time
# [2] You can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls hier iter() Method on The Iterable Behind The Scene
# [4] Gives "Stopiteration" If Theres No Next Element


# Iterable

myString = "Salar" 

myList = [1,2,3,4,5]


for letter in myString :
    print(letter , end = " ") # Salar


for number in myList :
    print(number) # 1 2 3 4 5 

print("-" * 50) # --------------------------------------------------


# Iterator

myString = "Salar" 
# print(next(myString)) # TypeError: 'str' object is not an iterator

myIterator = iter(myString)
print(next(myIterator)) # S
print(next(myIterator)) # a
print(next(myIterator)) # l
print(next(myIterator)) # a
print(next(myIterator)) # r



for letter in "Salar" :
    print(letter , end = " ") # S a l a r


for letter in iter("Salar") :
    print(letter , end = " ") # S a l a r





 




