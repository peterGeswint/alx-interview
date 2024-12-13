def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list): A list where each element is the maximum number (n) for a round.

    Returns:
    str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds, or
         None if there's no overall winner.
    """
    if not nums or x < 1:
        return None

    def sieve(max_n):
        """
        Generate a list of boolean values indicating primality for numbers 0 to max_n.

        Parameters:
        max_n (int): The maximum number up to which to calculate primes.

        Returns:
        list: A list where index i is True if i is prime, otherwise False.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    # Get the maximum value in nums to optimize prime calculations
    max_num = max(nums)
    primes = sieve(max_num)

    # Precompute the cumulative count of primes up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the winner for each round
        if prime_counts[n] % 2 == 1:  # Odd prime count -> Maria wins
            maria_wins += 1
        else:  # Even prime count -> Ben wins
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
