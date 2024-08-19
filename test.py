my_dict = {}
while True:
    test_input = input("input: ") 
    if test_input in my_dict:
       my_dict[test_input] += 1
    else: 
        my_dict[test_input] = 1
    print(my_dict)
    if test_input == "quit": break

my_dict_sorted = {key: value for key, value in sorted(my_dict.items())}
print(my_dict_sorted)

def foo():
    global a 
    a = 5

def func():
    print(a)

foo()
func()
