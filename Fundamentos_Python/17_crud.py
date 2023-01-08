#Crud create , read, update , delete

number =[1,2,3,4,5,6,7,8,9,0]

print(number[1])
number[-1] = 10
print(number)

number.append(222)
print(number)

number.insert(0, "hello")
print(number)

number.insert(5, "four")
print(number)

new_numbers = [11,12,13,14,15,16,17]
new_list= number + new_numbers
print(new_list)

print(new_list.index(15))

index = new_list.index(15)
new_list[index] = "Fifteen"
print(new_list)

new_list.remove(17)
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)


numbers = [1,4,7,9,5,3,2,7,9,6,"z"]
numbers.sort()
print(numbers)