import pytest
from main import fizzbuzz

def test_cases():
    fb_result = fizzbuzz()
    assert fb_result[2] == "Fizz" 
    assert fb_result[4] == "Buzz"  
    assert fb_result[14] == "FizzBuzz"  
    assert fb_result[98] == "Buzz"  
    assert fb_result[0] == "1" 