from fanumbers import consts


def to_fa_number(num, type='persian'):
    """
    :param num: int
    :param type: str, 'persian', 'arabic' or 'all'
    :return: a str if type is not 'all', otherwise a list of all possibilities
    """
    if type not in ["persian", "arabic", "all"]:
        raise ValueError("type should be 'persian', 'arabic' or 'all'")
    nums = str(num)
    res = ''
    if type == "all":
        res = ['']
    for x in nums:
        d = int(x)
        if type == "arabic":
            res += consts.ENGLISH_TO_ARABIC_DIGITS[d]
        elif type == "persian":
            res += consts.ENGLISH_TO_PERSIAN_DIGITS[d]
        else:
            new_res = []
            for i in range(len(res)):
                org = res[i]
                res[i] = org + consts.ENGLISH_TO_ARABIC_DIGITS[d]
                new_res.append(org + consts.ENGLISH_TO_PERSIAN_DIGITS[d])
            res += new_res
    return res


def from_fa_number(num):
    """
    :param num: string, containing arabic and persian digits
    :return: an int
    """
    res = 0
    for x in num:
        d = int(consts.ARABIC_TO_ENGLISH_DIGITS.get(x, consts.PERSIAN_TO_ENGLISH_DIGITS.get(x, None)))
        res = 10 * res + d
    return res
