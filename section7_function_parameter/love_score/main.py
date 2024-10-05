def calculate_love_score(name1, name2):
    true_chars = set('TRUE')
    love_chars = set('LOVE')

    def count_love(name):
        total_true = sum(1 for char in name.upper() if char in true_chars)
        total_love = sum(1 for char in name.upper() if char in love_chars)
        return str(total_true) + str(total_love)
    
    total = count_love(name1 + name2)
    print(total)

