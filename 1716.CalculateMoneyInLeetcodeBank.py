def totalMoney(n):
    """
    :type n: int
    :rtype: int
    """
    weekNumber = 0
    bankTotal = 0
    for i in range(n):
        weekNumber = i // 7
        bankTotal = i 