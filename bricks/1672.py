# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/richest-customer-wealth/
from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    return max([sum(item) for item in accounts])


if __name__ == '__main__':
    accounts = [[1, 2, 3], [3, 2, 1]]
    accounts = [[1, 5], [7, 3], [3, 5]]
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    print(maximumWealth(accounts))
