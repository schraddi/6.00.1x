def nfruits(fruits, pattern):
    """
    Dictionary: startFruits // containing the ammount of Fruits brought with Python
    e.g. {'A': 1, 'B': 2, 'C': 3}
    String: pattern // sequence, Python ate his fruits
    
    Return: maximum of left fruits
    """
    for char in pattern:
        if fruits.get(char,0) == 0: return -1
        for aFruit in fruits:
            if char == aFruit:
                fruits[aFruit] -= 1
            else:
                if aFruit != fruits.keys()[-1] : fruits[aFruit] += 1
    return max(fruits.values())

print nfruits({'A': 5, 'B': 7, 'C': 8, 'D': 11, 'E': 4}, 'AAABBBEECAAABBAACCAADDBBAACDCAAABBBAEACCAEADABCB')
