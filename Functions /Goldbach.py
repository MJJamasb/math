from math import isqrt
from typing import Dict, List, Tuple, Optional

def sieve(limit: int) -> List[bool]:
    """Return a boolean list is_prime up to and including limit."""
    if limit < 2:
        return [False] * (limit + 1)
    is_prime = [False, False] + [True] * (limit - 1)
    for p in range(2, isqrt(limit) + 1):
        if is_prime[p]:
            start = p * p
            step = p
            is_prime[start:limit+1:step] = [False] * ((limit - start) // step + 1)
    return is_prime

def goldbach_one_pair(e: int, is_prime: List[bool]) -> Optional[Tuple[int, int]]:
    """
    Return one prime pair (p, q) with p + q = e (e must be even > 2), or None if not found.
    Chooses the smallest p that works.
    """
    if e % 2 != 0 or e <= 2:
        raise ValueError("e must be an even integer > 2")
    for p in range(2, e // 2 + 1):
        if is_prime[p] and is_prime[e - p]:
            return p, e - p
    return None

def goldbach_all_pairs(e: int, is_prime: List[bool]) -> List[Tuple[int, int]]:
    """
    Return all prime pairs (p, q) with p + q = e (p <= q). e must be even > 2.
    """
    if e % 2 != 0 or e <= 2:
        raise ValueError("e must be an even integer > 2")
    pairs = []
    for p in range(2, e // 2 + 1):
        q = e - p
        if is_prime[p] and is_prime[q]:
            pairs.append((p, q))
    return pairs

def verify_goldbach(limit: int, first_pair_only: bool = True) -> Dict[int, Tuple[int, int] | List[Tuple[int, int]]]:
    """
    Verify Goldbach's conjecture for all even numbers 4..limit.
    Returns a dict mapping each even e to either:
      - a single (p, q) pair if first_pair_only=True, or
      - a list of all (p, q) pairs if first_pair_only=False.
    Raises AssertionError if a counterexample is found.
    """
    if limit < 4:
        return {}
    is_prime = sieve(limit)
    results: Dict[int, Tuple[int, int] | List[Tuple[int, int]]] = {}
    for e in range(4, limit + 1, 2):
        if first_pair_only:
            pair = goldbach_one_pair(e, is_prime)
            if pair is None:
                raise AssertionError(f"Counterexample found at {e}")
            results[e] = pair
        else:
            pairs = goldbach_all_pairs(e, is_prime)
            if not pairs:
                raise AssertionError(f"Counterexample found at {e}")
            results[e] = pairs
    return results

# ---- Examples ----
if __name__ == "__main__":
    # Verify up to 1,000,000 returning just one pair per even number
    sample = verify_goldbach(100)  # try 1_000_000 if you want; may take a bit longer
    for e in range(4, 26, 2):
        print(f"{e} = {sample[e][0]} + {sample[e][1]}")

    # Get all pairs for a specific even number
    primes_table = sieve(200)
    print("All pairs for 100:", goldbach_all_pairs(100, primes_table))
