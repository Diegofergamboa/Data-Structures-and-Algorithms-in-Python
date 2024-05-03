# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def multiple(n, m):
    """
        Check if n is multiple of m.
        
        Args:
        n (int) The number to check.
        m (int) The potential dividor.
        
        Returns:
        bool: True if n is a multiple of m, False otherwise.        
    """
    if isinstance(n, int) and isinstance(m, int):
        return n % m == 0
    else:
        return False


# R-1.2 Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def even_binary(k):
    """
        Check if an integer is even or not - BINARY SOLUTION
        
        Args:
        k: int to evaluate
        
        Returns:
        bool: True if k is even and, False otherwise
    """
    if (isinstance(k, int)):
        return (k & 1) == 0
    else:
        return print('Just use integers in the even function')
    
    
def even_recursive(k):
    """
        Check if an integer is even or not - RECURSIVE SOLUTION
        
        Args:
        k: int to evaluate
        
        Returns:
        bool: True if k is even and, False otherwise
    """
    if (k == 0):
        return True
    elif (k == 1):
        return False
    elif(k < 0):
        return even_recursive(k + 2)
    else:
        return even_recursive(k - 2)
    
    
# R-1.3 Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def minmax(data):
    """
        Review the whole data and search the min and max value into the data given without use min and max built.in functions
        
        Args: 
        data: sequence (list, dic, tuple)
        
        Returns:
        tuple: a tuple with the min and the max value.
    """
    data_order = sorted(data)
    data_length = len(data_order)
    ans = (data_order[0], data_order[data_length - 1])
    return ans

# R-1.4 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
    """
        Sum all the squares of all the positive int before n using a for loop
        
        Args:
        n: int to use as a max range to sum the squares behind it
        
        Returns:
        An int with the final sum
    """
    if isinstance(n, int) and n > 0:
        ans = 0
        for i in range(0,n):
            ans += pow(i, 2)
        return ans

# R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely- ing on Python’s comprehension syntax and the built-in sum function.

def sum_of_squares_c(n):
    """
        Sum all the squares of all the positive int before n using a comprehension
        
        Args:
        n: int to use as a max range to sum the squares behind it
        
        Returns:
        An int with the final sum
    """
    if (n > 0 and isinstance(n, int)):
        return sum(i ** 2 for i in range(0, n))
    else:
        print('Invalid input')
        
        
# R-1.6 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.

def sum_of_odd_squares(n):
    """
        Sum all the squares of all the odds positive int before n
        
        Args:
        n: int to use as a max range to sum the squares behind it
        
        Returns:
        An int with the final sum of all the squares from the odds numbers
    """
    ans = 0
    if n > 0 and isinstance(n, int):
        for i in range(0, n):
            if i % 2 != 0:
                ans += pow(i,2)
    else:
        print('Invalid input')
    return ans

# R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely- ing on Python’s comprehension syntax and the built-in sum function.

def sum_of_odd_squares_generator(n):
    """
        Sum all the squares of all the odds positive int before n using a generator
        
        Args:
        n: int to use as a max range to sum the squares behind it
        
        Returns:
        An int with the final sum of all the squares from the odds numbers
    """
    if n > 0 and isinstance(n, int):
        return sum(pow(i, 2) for i in range(0, n) if i % 2 != 0)
    else:
        print('Invalid input')
        
        
# R-1.8 Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for in- dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?

# Answer -> So, if s is a string of length n, and s[k] is used for index -n ≤ k < 0, then the equivalent positive index j would be j = k + n.


# R-1.9 What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?

# Using this syntax for the tange range(start, stop[, step])

def range_constructor(start, end, step):
    return list(range(start, end, step))

# Answer -> range_constructor(50, 81, 10)

# R-1.10 What parameters should be sent to the range constructor, to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

# Answer -> 
# print(range_constructor(8, -10, -2))

# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
def comprehension_constructor():
    return [2 ** i for i in range(0, 9)]


# R-1.12 Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module in- cludes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.
import random
def get_random_range(data):
    if not data:
        ValueError('get_random_range without param')
    index = random.randrange(len(data))
    return data[index]


# R-1.13 Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.

# Algorithm: Reverse

# Inputs: 
# - A list of numbers (list)

# Outputs:
# - The same list inverted

# Steps:
# 1. Create an empty list
# 2. For each element in the list push it into the begin of the new list:
# 3. Return the new list

# With Python functions.
def reverse_native(data):
    """
        Function to reverse a list
        
        Args:
            data: List, to reverse
        
        Return:
            List reversed
    """
    
    if isinstance(data, list):
        data.reverse()
        return data
    else:
        return None


# r-1.14 Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.

def products_odd(sequence):
    """
        Based in a sequence, returns the combination or pair of numbers of the sequence where the product is odd
        
        Args:
            sequence: list to check
            
        Return:
            List with the pairs
    """
    pairs_odd_products = []
    for i in range(len(sequence)):
        for j in sequence[i+1:]:
            product = sequence[i] * j
            if product % 2 != 0:
                pairs_odd_products.append([sequence[i], j])
    return pairs_odd_products

# r-1.15 Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct)

def compare_n(sequence):
    """
    Check if all numbers in the sequence are distinct.
    
    Args:
        sequence: list of numbers
    
    Returns:
        True if all numbers are distinct, False otherwise
    """
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[i] == sequence[j]:
                return False
    return True


# r-1.16 - r-1.17
def scale(data, factor):
    for val in data:
        val *= factor

def realscale(data, factor):
    #data*=factor #This will concatenate the array with itself multiple times!  
    for i in range (len(data)):
        data[i]*=factor
        
        
# r-1.18 Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

list_to_comprehension = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
comprehension_list = [i * (i + 1) for i in range(0, len(list_to_comprehension))]

# r-1.19 Demonstrate how to use Python’s list comprehension syntax to produce thelist[ a , b , c ,..., z ],butwithouthavingtotypeall26such characters literally.
alphabet = [chr(ord('a') + i) for i in range(26)]

# r-1.20 Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possi- ble order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.

def shuffle_randint(sequence):
    new_sequence = []
    indexes = list(range(len(sequence)))
    while indexes:
        random_index = random.randint(0, len(indexes) - 1)
        new_sequence.append(sequence[indexes.pop(random_index)])
    return new_sequence

# r-1.21 Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D).

# lines = []

# try:
#     while True:
#         line = input()
#         lines.append(line)
# except EOFError:
#     for line in reversed(lines):
#         print(line)

# r-1.22 Write a short Python program that takes two arrays a and b of length n storing int values, and returns the dot product of a and b. That is, it returns an array c of length n such that c[i] = a[i]·b[i], for i = 0,...,n−1.

# def doct_constructor(a,b):
#     c = []
#     counter = 0
#     if isinstance(a, list) and isinstance(b, list):
#         while counter < len(a):
#             print(counter)
#             c.append(a[counter])
#             c.append(b[counter])
#             counter += 1 
#     return c
# print(doct_constructor([1,2,3], ['a','b','c']))


def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("The matrix should have the same length")
    
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    
    return result


# r-1.23 Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the following error message: “Don’t try buffer overflow attacks in Python!”
def printerIndex(list, index):
    try:
        return (list[index])
    except IndexError:
        return ('Don’t try buffer overflow attacks in Python!')
    

# r-1.24 Write a short Python function that counts the number of vowels in a given character string.
import re

def countVowels(string):
    pattern = r'[aeiouAEIOU]'
    coincidence = re.findall(pattern, string)
    return len(coincidence)

# r-1.25 Write a short Python function that takes a strings, representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return "Lets try Mike".

def deletePunctuation(string):
    pattern = r'[^\w\s]'
    cleaned_string = re.sub(pattern, '', string)
    return cleaned_string


# r-1.26 Write a short program that takes as input three integers, a, b, and c, from the console and determines if they can be used in a correct arithmetic formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”
def validate_operations(a, b, c):
    if a + b == c or b + c == a or a * b == c:
        return True
    else:
        return False
    
# r-1.27 In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer. The third of those implementa- tions, from page 41, was the most efficient, but we noted that it did not yield the factors in increasing order. Modify the generator so that it reports factors in increasing order, while maintaining its general performance ad- vantages.

def factors(n):
    k=1
    p = None
    while k*k  < n:
        if n % k == 0:
            if k == p :
                break
            yield k
            p = n // k
            yield p
            if k == p :
                break
        k+=1

def sorted_factors(n):
    k=1
    while k*k  < n:
        if n % k == 0:
            yield k
        k+=1
    if k*k == n:
        yield k
    
    while k <= n//2:
        k+=1
        if n % k == 0:
            yield k
    yield n
    
# r-1.28 For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a Euclidean norm of 42 +32 = 16+9 = 25 = 5. Give an implemen- tation of a function named norm such that norm(v, p) returns the p-norm value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.

import math

def euclidianFunction(list):
    """
        Function to calculate the Euclidian of an array of numbers given
        
        Args:
            list: List with the numbers to calculate
        
        Return:
            Int with the final result of the euclidian function 
    """
    norm_value = 0
    for i in list:
        norm_value += pow(i, 2)
    return math.sqrt(norm_value)

# r-1.29 Write a Python program that outputs all possible strings formed by using thecharacters c , a , t , d , o ,and g exactlyonce.

def generate_strings(characters, current_string=''):
    if len(characters) == 0:
        print(current_string)
    else:
        for i in range(len(characters)):
            remaining_characters = characters[:i] + characters[i+1:]
            generate_strings(remaining_characters, current_string + characters[i])
            
            
# r-1.30 Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.
def divider_in_two_counter(num):
    """
        Function to count the quantity in that a number is minor than 2 dividing it by two
        
        Args:
            num: Int with the number to count on divisions
        
        Return:
            Int that represents the count
    """
    if isinstance(num, int) and num >= 2:
        counter = 0
        while num >=2:
            num = num/2
            counter += 1
        return counter
    return counter


# r-1.31 Write a Python program that can “make change.” Your program should take two numbers as input, one that is a monetary amount charged and the other that is a monetary amount given. It should then return the number of each kind of bill and coin to give back as change for the difference between the amount given and the amount charged. The values assigned to the bills and coins can be based on the monetary system of any current or former government. Try to design your program so that it returns as few bills and coins as possible.
def money_changer(money_charged, money_given):
    """
    The purpose of this function is to create a money changer
    
    Args:
        money_charged: Int, amount of money charged
        money_given: Int, amount of money given
        
    Returns:
        Dictionary, quantity of change to give in Colombian currency denominations
    """
    
    if money_given < money_charged:
        return {}
    
    cop_money = {
        100000: 0,
        50000: 0,
        20000: 0,
        10000: 0,
        5000: 0,
        2000: 0,
        1000: 0,
        500: 0,
        200: 0,
        100: 0,
        50: 0
    }
    
    exchange_amount = money_given - money_charged
    money_to_give = exchange_amount
    
    for bill in sorted(cop_money.keys(), reverse=True):
        while money_to_give >= bill:
            cop_money[bill] += 1
            money_to_give -= bill
            
    return cop_money


# r-1.32 