#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determine the winner of the game.
    
    Args:
    x (int): Number of rounds.
    nums (List[int]): List of 'n' values for each round.
    
    Returns:
    str: Name of the player that won the most rounds (either 'Maria' or 'Ben').
    """
    
    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n using the Sieve of Eratosthenes."""
        primes = [True] * (n+1)
        p = 2
        while p**2 <= n:
            if primes[p]:
                for i in range(p**2, n+1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n+1) if primes[p]]
    
    def play_game(n, primes):
        """Simulate the game and return the winner ('Maria' or 'Ben')."""
        numbers = set(range(1, n+1))
        turn = 0  # 0 for Maria, 1 for Ben
        
        for prime in primes:
            if prime > n:
                break
            if prime in numbers:
                multiples = set(range(prime, n+1, prime))
                numbers.difference_update(multiples)
                turn = 1 - turn  # Switch turns
        
        return 'Maria' if turn == 1 else 'Ben'
    
    if x <= 0 or not nums:
        return None
    
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n, primes)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

# Test the function
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Example output: Ben
