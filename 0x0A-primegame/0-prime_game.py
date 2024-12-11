#!/usr/bin/python3
def sieve_of_eratosthenes(max_n):
    """Generate a list of primes up to max_n using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(max_n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes, is_prime


def count_moves(n, primes, is_prime):
    """Count the number of moves possible for a given n."""
    moves = 0
    taken = [False] * (n + 1)

    for prime in primes:
        if prime > n:
            break
        if not taken[prime]:
            moves += 1
            for multiple in range(prime, n + 1, prime):
                taken[multiple] = True

    return moves


def isWinner(x, nums):
    """Determine the winner of the game."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes, is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = count_moves(n, primes, is_prime)
        if moves % 2 == 1:  # Maria wins
            maria_wins += 1
        else:  # Ben wins
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
