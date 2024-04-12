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


# Do using a generator and chaging the range with the range(start, stop, step)