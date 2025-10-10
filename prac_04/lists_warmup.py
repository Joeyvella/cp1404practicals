numbers = [3, 1, 4, 1, 5, 9, 2]
#numbers[0]- 3
#numbers[-1]- 2
#numbers[3]- 1
#numbers[:-1]- reverse
#numbers[3:4] - 1
#5 in numbers -  True
#7 in numbers - False
#"3" in numbers - False as it is asking for a string
#numbers + [6, 5, 3] - [3,1,4,1,5,9,2,6,5,3] (adds 6 5 3 to the list)

#Change the first element of numbers to "ten"
numbers[0] = "ten"

#Change the last element of numbers to 1
numbers[-1] = 1

#Print all the elements from numbers except the first two (slice)
print(numbers[2:])

#Print whether 9 is an element of numbers
print(9 in numbers)