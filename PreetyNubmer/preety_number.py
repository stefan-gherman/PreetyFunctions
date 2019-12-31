def the_price_of_beauty(num):
    '''
    The function takes a number of int type and based on how large it is
    it returns it in a format that can be read more easily, similiar to YouTube
    views numbers.

    num : int
    return type: string
    '''
    if type(num) is not int:
        return f"Given parameter is not of integer type."
    inner_num = num
    number_of_digs = 0

    suffixes = {'K': [4, 5, 6], 'M': [7, 8, 9], 'B': [10, 11, 12], 'T': [
        13, 14, 15], 'QUAD': [16, 17, 18], 'QUIN': [19, 20, 21]}
    if inner_num > 0 and inner_num < 1000:
        return num
    else:
        flag2 = False
        flag3 = False
        while inner_num > 0:
            if inner_num > 99 and inner_num < 1000:
                third_dig = inner_num % 10
                if third_dig:
                    flag3 = True
                second_dig = (inner_num // 10) % 10
                if second_dig:
                    flag2 = True
                first_dig = (inner_num // 100) % 10
            number_of_digs += 1
            inner_num = inner_num // 10
        for key in suffixes.keys():
            if number_of_digs in suffixes[key]:
                magnitude = key
                for elem in range(len(suffixes[key])):
                    if number_of_digs == suffixes[key][elem]:
                        pos = elem
                        break
            # else:
            #     return f"This number breaks the space-time continuum"
        if pos == 2:
            return f'{first_dig}{second_dig}{third_dig}{magnitude}'
        elif pos == 1:
            if flag3 == True:
                return f'{first_dig}{second_dig}.{third_dig}{magnitude}'
            return f'{first_dig}{second_dig}{magnitude}'
        elif pos == 0:
            if flag3 == True:
                return f'{first_dig}.{second_dig}{third_dig}{magnitude}'

            else:
                if flag2 == True:
                    return f'{first_dig}.{second_dig}{magnitude}'
                else:
                    return f'{first_dig}{magnitude}'


print(the_price_of_beauty(102356))
