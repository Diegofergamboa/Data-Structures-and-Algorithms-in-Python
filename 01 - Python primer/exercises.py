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


# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

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
    
    
# Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

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