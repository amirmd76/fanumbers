from fanumbers import consts, utils, numbers


def _number_to_words(num, all_possibilities=False):
    if num < 10:
        return [consts.DIGITS_1[num]]
    if num < 100:
        x, y = int(str(num)[0]), int(str(num)[-1])
        if num < 20:
            return [consts.DIGITS_10[y]]
        if y == 0:
            return [consts.DIGITS_10_2[x]]
        return ["{} و {}".format(consts.DIGITS_10_2[x], _number_to_words(y, all_possibilities)[0])]
    if num < 1000:
        x = int(str(num)[1:])
        f = int(str(num)[0])
        res = []
        if x == 0:
            res2 = ['']
        else:
            res2 = [" و " + item for item in _number_to_words(x, all_possibilities)]
        for item in res2:
            if all_possibilities:
                for w in consts.DIGITS_100[f]:
                    res.append(w + item)
            else:
                res.append(consts.DIGITS_100[f][0] + item)
        return res

    if num < int(1e6):
        nums = str(num)
        nums = '0' * (6 - len(nums)) + nums
        x = int(nums[:3])
        y = int(nums[3:])
        res = []
        if y == 0:
            res2 = ['']
        else:
            res2 = [" و " + item for item in _number_to_words(y, all_possibilities)]

        pre = []
        if x == 1:
            pre.append('هزار')
            if all_possibilities:
                pre.append('یک هزار')
        else:
            pre = [item + " هزار" for item in _number_to_words(x, all_possibilities)]
        for f in pre:
            for item in res2:
                res.append(f + item)
        return res
    nums = str(num)
    le = (len(nums) - 1) // 3
    if le > 4:
        raise ValueError("num should be less than 1e15")
    words = ['', '', 'میلیون', 'میلیارد', 'تریلیون']
    lr = le * 3
    ll = len(nums) - lr
    x = int(str(nums)[:ll])
    y = int(str(nums)[ll:])
    pre = [item + " " + words[le] for item in _number_to_words(x, all_possibilities)]
    res = []
    if y == 0:
        res2 = ['']
    else:
        res2 = [" و " + item for item in _number_to_words(y, all_possibilities)]
    for f in pre:
        for item in res2:
            res.append(f + item)
    return res


def number_to_words(num, ordinal=False, all_possibilities=False):
    """
    :param num: an int, or a str containing arabic and persian digits, only works for < 1e15
    :param ordinal: a boolean, False for cardinal and True for ordinal
    :param all_possibilities: it can be True to return all possibilities
    :return: a word, or a list of words in case all_possibilities = True
    """
    if not isinstance(num, int):
        num = numbers.from_fa_number(num)
    if ordinal:
        if num == 0:
            return utils.to_result('صفرم', all_possibilities)
        if num == 1:
            if all_possibilities:
                return ['یکم', 'اول']
            else:
                return 'یکم'
    res = _number_to_words(num, all_possibilities)
    if ordinal:
        ans = []
        for item in res:
            ans.append(item + "م")
        if all_possibilities:
            return ans
        else:
            return ans[0]
    if all_possibilities:
        return res
    return res[0]

