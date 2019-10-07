# string_handling

## Installing

```sh
$ pip install string_handling
```

## Usage

```py
from string_handling import find, format

format.del_accents(text) # Return a string with the deleted accents
find.palindromes(msg, delimiter=None, diff_cl=False)
# Returns a dictionary with the palindromes and your respective counts.
# For example {palindrome_1: count, palindrome_2: count}.
find.letters(str, letter=None, diff_cl=False):
# Returns a dictionary with the letter(s) and your respective counts.
# For example {letter_a: count_a, letter_b: count_b}.
```

## Example

```sh
>>> from string_handling find, format
>>> # function del_accents
>>> format.del_accents('áéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãẽĩõũÃẼĨÕŨçÇ')
'aeiouAEIOUaeiouAEIOUaeiouAEIOUcC'
>>> # function palindromes
>>> find.palindromes('arara')
{'arara': 1}
>>> find.palindromes('A madam, a boy, a mom; racecar', ' |, |; ')
{'A': 3, 'madam': 1, 'mom': 1, 'racecar': 1}
>>> find.palindromes('A madam, a boy, a mom; racecar', ' |, |; ', True)
{'A': 1, 'madam': 1, 'a': 2, 'mom': 1, 'racecar': 1}
>>> # function letters
>>> find.letters('A madam, a boy, a mom; racecar', 'a')
{'a': 7}
>>> find.letters('A madam, a boy, a mom; racecar', 'a', True)
{'a': 6}
>>> find.letters('adam, boy, moM', diff_cl=True)
{'a': 2, 'd': 1, 'm': 2, ',': 2, ' ': 2, 'b': 1, 'o': 2, 'y': 1, 'M': 1}
```
