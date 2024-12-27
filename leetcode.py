def minimumCardPickup(cards: list[int]) -> int:
    new = {}
    li = []
    found = 0
    for index, value in enumerate(cards):
        if value in new:
            fin = index - new[value]
            li.append(fin + 1)
            found = 1
            new[value] = index
        # add logic here
        else:
            new[value] = index
    if found:
        return min(li)
    return -1


cards = [
    77,
    10,
    11,
    51,
    69,
    83,
    33,
    94,
    0,
    42,
    86,
    41,
    65,
    40,
    72,
    8,
    53,
    31,
    43,
    22,
    9,
    94,
    45,
    80,
    40,
    0,
    84,
    34,
    76,
    28,
    7,
    79,
    80,
    93,
    20,
    82,
    36,
    74,
    82,
    89,
    74,
    77,
    27,
    54,
    44,
    93,
    98,
    44,
    39,
    74,
    36,
    9,
    22,
    57,
    70,
    98,
    19,
    68,
    33,
    68,
    49,
    86,
    20,
    50,
    43,
]
x = minimumCardPickup(cards)
print(x)
