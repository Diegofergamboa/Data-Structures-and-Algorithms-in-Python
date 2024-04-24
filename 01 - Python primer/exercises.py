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