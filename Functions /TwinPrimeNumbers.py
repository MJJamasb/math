from math import isqrt
from typing import List, Tuple

def _sieve(limit: int) -> List[bool]:
    """Return is_prime[0..limit]."""
    if limit < 2:
        return [False] * (limit + 1)
    is_prime = [False, False] + [True] * (limit - 1)
    for p in range(2, isqrt(limit) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start:limit+1:p] = [False] * ((limit - start)//p + 1)
    return is_prime

def twin_primes_upto(n: int) -> List[Tuple[int, int]]:
    """
    Return all twin-prime pairs (p, p+2) with p+2 <= n.
    Example: n=20 -> [(3, 5), (5, 7), (11, 13), (17, 19)]
    """
    if n < 3:
        return []
    is_prime = _sieve(n)
    return [(p, p + 2) for p in range(2, n - 1) if is_prime[p] and is_prime[p + 2]]

# --- examples ---
if __name__ == "__main__":
    for N in (20, 50, 100):
        print(N, "->", twin_primes_upto(N))
