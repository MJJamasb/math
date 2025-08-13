def check_perfect_number(n):
    # Find divisors excluding n itself
    divisors = [i for i in range(1, n) if n % i == 0]
    
    # Check if it's perfect
    is_perfect = sum(divisors) == n
    
    # Output results
    print(f"Number: {n}")
    print(f"Divisors: {divisors}")
    print(f"Sum of divisors: {sum(divisors)}")
    if is_perfect:
        print(f"{n} is a PERFECT number.")
    else:
        print(f"{n} is NOT a perfect number.")
    
    return is_perfect, divisors

# Example usage:
check_perfect_number(28)
