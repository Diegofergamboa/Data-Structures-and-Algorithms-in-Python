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

def even(k):
    """
        Check if an integer is even or not
        
        Args:
        k: int to evaluate
        
        Returns:
        bool: True if k is even and, False otherwise
    """
    if (isinstance(k, int)):
        return (k & 1) == 0
    else:
        return print('Just use integers in the even function')