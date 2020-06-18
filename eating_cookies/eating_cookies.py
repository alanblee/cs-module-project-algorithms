"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1

    eat_one_at_a_time = eating_cookies(n - 1)
    eat_two_at_a_time = eating_cookies(n - 2)
    eat_three_at_a_time = eating_cookies(n - 3)
    return eat_one_at_a_time + eat_two_at_a_time + eat_three_at_a_time


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies"
    )
