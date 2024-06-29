#list comprechension
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = [number for number in numbers if number % 2 == 0]



#generators
# def test_generator(n):
#     for i in range(1, n):
#         yield 1

# foo = test_generator(10)

# for i in foo:
#     print(i)

# print("=" * 20)
# for i in foo:  #hich nima chiqmiydi
#     print(i)

 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = (number for number in numbers if number % 2 == 0) #generator
# print(result)
def imtihon(royhat):
    b = [i for i in royhat if i % 3 == 0]
    return b
c = range(1, 10)
u = imtihon(c)
print(u)


