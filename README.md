# fanumbers
A Library to work with Farsi(Persian) numbers

## Usages
### to_fa_number
Use this method to convert an integer into a Persian number. You can select encoding, Persian, Arabic or All possibilities (all combinations of Arabic and Persian digits).

```python
from fanumbers import to_fa_number
print(to_fa_number(85))  # returns a str, in Persian digits
print(to_fa_number(75, 'arabic'))  # returns a str, in Arabic digits
print(to_fa_number(2018, 'all'))  # returns a list of strings, all possibilities
```

### from_fa_number
Use this method to convert a number in Persian and Arabic digits to an integer.

```python
from fanumbers import from_fa_number
print(from_fa_number("۸۵۸۵"))  # returns an int, 8585
```

### number_to_words
Use this method to convert int or Arabic/Persian numbers into Persian words.

This method two optional arguments, `ordinal` which is set to False by default and if set to True will return ordinal numbers instead of cardinal. And 
`all_possibilities` which is set to False by default and if set to True, will return a list of all possible writings of the number instead of a single string.

```python
from fanumbers import number_to_words
print(number_to_words(85))  # هشتاد و پنج 
print(number_to_words(7, ordinal=True))  # هفتم
for res in number_to_words(111111111, all_possibilities=True):  # wil return multiple strings
    print(res)
```
