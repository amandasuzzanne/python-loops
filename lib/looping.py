#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    counter = 10
    while counter > 0:
        print(counter)
        counter = counter - 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    pass
    squares = [i * i for i in int_list]
    return squares

def fizzbuzz():
    # code goes here!
    pass
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

fizzbuzz()