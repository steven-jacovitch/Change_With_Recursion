"""
############################## Homework Recursion ##############################

% Student Name: Steven Jacovitch

% Student Unique Name: sjacovit

% Lab Section 00X: 004

% I worked with the following classmates: Nobody

%%% Please fill in the first 4 lines of this file with the appropriate information before submitting on Canvas.
"""

import math

def change(amount, coins):
    '''
    this function returns a non-negative integer indicating the minimum
    number of coins required to make up the given amount. If there is no possible solution,
    return math.inf

    Parameters
    ----------
    amount: int
        the amount of money to make change for
    coins: list
        a list of coin denominations available to make change with
    '''
    # base cases
    if amount == 0:
        return 0
    if len(coins) == 0 or amount < 0:
        return math.inf
    # if the first coin is greater than the amount, then we can't use it
    if coins[0] > amount:
        return change(amount, coins[1:])
    # once we find a coin that is less than or equal to the amount, we can use it or lose it
    # if we use it, we subtract the amount by the coin and call the function again
    # if we lose it, we call the function again with the next coin
    else:
        use_it = 1 + change(amount - coins[0], coins)
        lose_it = change(amount, coins[1:])
        return min(use_it, lose_it)
    
def giveChange(amount, coins):
    '''
    this function returns a list whose first member is the minimum number of coins(int) and whose second member is a list of the coins in that optimal solution

    Parameters
    ----------
    amount: int
        the amount of money to make change for
    coins: list
        a list of coin denominations available to make change with

    Returns
    -------
    list
        a list whose first member is the minimum number of coins(int) and whose second member is a list of the coins in that optimal solution

    '''
    # base cases
    if amount == 0:
        return [0, []]
    if len(coins) == 0 or amount < 0:
        return [math.inf, []]
    # if the first coin is greater than the amount, then we can't use it
    if coins[0] > amount:
        return giveChange(amount, coins[1:])
    # once we find a coin that is less than or equal to the amount, we can use it or lose it
    # if we use it, we subtract the amount by the coin and call the function again
    # if we lose it, we call the function again with the next coin
    else:
        use_it = giveChange(amount - coins[0], coins)
        use_it[1].append(coins[0])
        lose_it = giveChange(amount, coins[1:])
        if use_it[0] + 1 < lose_it[0]:
            return [use_it[0] + 1, use_it[1]]
        else:
            return lose_it

if __name__ == "__main__":

    coin_list = [1, 5, 10, 25, 50]
    amount = 64

    result = change(amount, coin_list)
    change_result = giveChange(amount, coin_list)
    print("amount: ", amount)
    print("coint list: ", coin_list)
    print("number of coin: ", result)
    print(change_result, "\n")

    coin_list2 = [1, 7, 24, 42]
    amount2 = 18

    result2 = change(amount2, coin_list2)
    change_result2 = giveChange(amount2, coin_list2)
    print("amount: ", amount2)
    print("coint list: ", coin_list2)
    print("number of coins: ", result2)
    print(change_result2, "\n")

    coin_list3 = [4, 6, 8]
    amount3 = 17

    result3 = change(amount3, coin_list3)
    change_result3 = giveChange(amount3, coin_list3)
    print("amount: ", amount3)
    print("coint list: ", coin_list3)
    print("number of coins: ", result3)
    print(change_result3, "\n")
