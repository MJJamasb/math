def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def goldbach_pairs_count(n):
    """
    Return the number of unique prime pairs (p1, p2) such that:
    p1 + p2 = n, for even n > 2.
    """
    if n <= 2 or n % 2 != 0:
        raise ValueError("n must be an even integer greater than 2")
    
    count = 0
    for p1 in range(2, n // 2 + 1):
        p2 = n - p1
        if is_prime(p1) and is_prime(p2):
            count += 1
    return count


# Example usage
n = 26
print(f"Number of prime pairs for {n}: {goldbach_pairs_count(n)}")
