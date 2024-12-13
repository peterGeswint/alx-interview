def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Helper to calculate primes using Sieve of Eratosthenes
    def sieve(max_n):
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        return is_prime

    max_num = max(nums)
    primes = sieve(max_num)

    # Precompute prime counts
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
