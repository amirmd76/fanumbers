ARABIC_DIGITS_LIST = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
PERSIAN_DIGITS_LIST = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']


def list_to_dict(ls, rev=False):
    res = {}
    for i, val in enumerate(ls):
        if rev:
            res[val] = i
        else:
            res[i] = val
    return res


ENGLISH_TO_ARABIC_DIGITS = list_to_dict(ARABIC_DIGITS_LIST)
ARABIC_TO_ENGLISH_DIGITS = list_to_dict(ARABIC_DIGITS_LIST, True)
ENGLISH_TO_PERSIAN_DIGITS = list_to_dict(PERSIAN_DIGITS_LIST)
PERSIAN_TO_ENGLISH_DIGITS = list_to_dict(PERSIAN_DIGITS_LIST, True)

DIGITS_1 = ['صفر', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه']
DIGITS_10 = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده']
DIGITS_10_2 = ['',  '', 'بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود']
_DIGITS_100 = ['', ['صد', 'یکصد'], 'دویست', 'سیصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد']
DIGITS_100 = [x if isinstance(x, list) else [x] for x in _DIGITS_100]
