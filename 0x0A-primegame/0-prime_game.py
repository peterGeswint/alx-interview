#!/usr/bin/python3
"""
Prime Game Module

This module provides a function to determine thewinnerofaprimenumbergameplayed
between Maria and Ben. The game involves removingprimenumbersandtheirmultiples
from a set of consecutive integers. The player who cannot make a move loses.

Example usage:
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))  # Output: 'Ben'

Attributes:
    None

Functions:
    isWinner(x, nums):
        Determines the winner of the prime number game for each round.

"""


def isWinner(x, nums):
    """
    Determine the winner of the game.

    Args:
    x (int): Number of rounds.
    nums (List[int]): List of 'n' values for each round.

    Returns:
    str: Name of the player that won the most rounds(either'Maria'or'Ben').
    If the winner cannot be determined, returns None.

    The function first generatesalistofprimenumbersuptothemaximumpossible
    value of 'n' using the SieveofEratosthenes.Itthensimulateseachroundofthe
    game, where players take turnsremovingprimenumbersandtheirmultiplesfromthe
    set. The player who cannotmakeamovelosestheround.Thefunctionkeepstrack
    of the number ofroundswonby Maria and Ben, and returns theplayerwiththemost
    wins.
    """
    def sieve_of_eratosthenes(n):
        """GeneratealistofprimenumbersuptonusingtheSieveofEratosthenes.

        Args:
        n (int): The upper limit for generating prime numbers.

        Returns:
        List[int]: A list of prime numbers up to n.
        """
        primes = [True] * (n+1)
        p = 2
        while p**2 <= n:
            if primes[p]:
                for i in range(p**2, n+1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n+1) if primes[p]]

    def play_game(n, primes):
        """Simulate the game and return the winner ('Maria' or 'Ben').

        Args:
        n (int): The size of the set of consecutive integers.
        primes(List[int]):A listofprimenumbersuptothemaximumpossible'n'.

        Returns:
        str: The winner of the game ('Maria' or 'Ben').
        """
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
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
