def standart_function():
    result = []
    for i in range(1000000):
        result.append(i**3)
    return result


def my_gen():
    for i in range(10):
        yield i**3

for res in my_gen():
    print (res)

## also we can pause and resume the generator with next() as next(my_gen) it will give next value of generator.
generator_example = my_gen()
## type(generator_example)
standart_function()
print ("HOW NEXT FUNCTION WORKS ")
print next(generator_example)
print next(generator_example)
print next(generator_example)
