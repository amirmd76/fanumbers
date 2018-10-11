def to_result(x, to_list=False):
    if to_list and not isinstance(x, list):
        return [x]
    return x
