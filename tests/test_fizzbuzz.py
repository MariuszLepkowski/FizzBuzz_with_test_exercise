from fizzbuzz import fizzbuzz

def test_returns_number():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_returns_numbers_divisible_by_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_returns_numbers_divisible_by_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_returns_numbers_divisible_by_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"




