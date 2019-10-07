# -*- coding: utf-8 -*-
"""
This is the find module.

The find module supplies one functions,
    palindromes()
For example,

>>> palindromes('ara')
{'ara': 1}
"""


import re
from string_handling.format import del_accents


_PATTERN = r"[^a-zA-ZáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãẽĩõũÃẼĨÕŨçÇ]"


def _pal_diff_cl(str: str, palindromes: dict) -> tuple:
    """Search for palindromes by differentiating the caps lock.

    >>> _pal_diff_cl('ara', {'ARA': 1})
    ('ara', 1)
    >>> _pal_diff_cl('ara', {'ara': 1})
    ('ara', 2)

    Parameters
    ----------
    str : str
        String to search in palindromes.
    palindromes : dict
        List of palindromes.

    Returns
    -------
    tuple
        Tuple containing the key and new count value
        or value 1 to a new palindrome.

    """
    if str in palindromes:
        return str, palindromes[str] + 1
    return str, 1


def _pal_not_diff_cl(str: str, palindromes: dict) -> tuple:
    """Search for palindromes not by differentiating the caps lock.

    >>> _pal_not_diff_cl('arara', {'ARARA': 2})
    ('ARARA', 3)
    >>> _pal_not_diff_cl('ARARA', {'arara': 5})
    ('arara', 6)

    Parameters
    ----------
    str : str
        String to search in palindromes.
    palindromes : dict
        List of palindromes.

    Returns
    -------
    tuple
        Tuple containing the key and new count value
        or value 1 to a new palindrome.

    """
    for pal in palindromes:
        if str.lower() == pal.lower():
            return pal, palindromes[pal] + 1
    return str, 1


_MODES_FIND_PAL = {False: _pal_not_diff_cl, True: _pal_diff_cl}


def palindromes(str: str, delimiter: str = None, diff_cl: bool = False) -> dict:
    """Returns a dictionary with the palindromes and your respective counts.
    For example {palindrome_1: count, palindrome_2: count}.

    >>> palindromes('Socorram-me, subi no ônibus em Marrocos')
    {'Socorram-me, subi no ônibus em Marrocos': 1}
    >>> palindromes('arara')
    {'arara': 1}
    >>> palindromes('A madam, a boy, a mom; racecar', ' |, |; ')
    {'A': 3, 'madam': 1, 'mom': 1, 'racecar': 1}
    >>> palindromes('A madam, a boy, a mom; racecar', ' |, |; ', True)
    {'A': 1, 'madam': 1, 'a': 2, 'mom': 1, 'racecar': 1}
    >>> palindromes('adam, boy, mon', ', ', True)
    {}

    Parameters
    ----------
    str : str
        String to be verified.
    delimiter : str
        A regex containing the delimiters to split the 'message' at a list.
        Default is 'None', using the plain text.
    diff_cl : bool
        A boolean value to activate the caps lock difference. Default is False

    Returns
    -------
    dict
        Dictionary containing the palindromes and your respective counts.

    """
    palindromes = {}
    words = []
    find = _MODES_FIND_PAL[diff_cl]

    if delimiter:
        words = re.split(delimiter, str)
    else:
        words.append(str)

    for w in words:
        n_w = del_accents(w)
        n_w = re.sub(_PATTERN, "", n_w)
        size_w = len(n_w)

        end = size_w >> 1
        start = end if size_w % 2 != 0 else end - 1

        if n_w[:end].lower() == n_w[:start:-1].lower():
            key, value = find(w, palindromes)
            palindromes[key] = value

    return palindromes


def letters(str: str, letter: str = None, diff_cl: bool = False) -> dict:
    """Returns a dictionary with the letter(s) and your respective counts.
    For example {letter_a: count_a, letter_b: count_b}.

    >>> letters('Socorram-me, subi no ônibus em Marrocos')
    {'s': 4, 'o': 5, 'c': 2, 'r': 4, 'a': 2, 'm': 4, '-': 1, 'e': 2, ',': 1, \
' ': 5, 'u': 2, 'b': 2, 'i': 2, 'n': 2, 'ô': 1}
    >>> letters('arara')
    {'a': 3, 'r': 2}
    >>> letters('A madam, a boy, a mom; racecar', 'a')
    {'a': 7}
    >>> letters('A madam, a boy, a mom; racecar', 'a', True)
    {'a': 6}
    >>> letters('adam, boy, moM', diff_cl=True)
    {'a': 2, 'd': 1, 'm': 2, ',': 2, ' ': 2, 'b': 1, 'o': 2, 'y': 1, 'M': 1}

    Parameters
    ----------
    str : str
        String to be verified.
    letter : str
        Letter (optional) to be used in the search.
        Search all letters, if standard
    diff_cl : bool
        A boolean value to activate the caps lock difference. Default is False

    Returns
    -------
    dict
        Dictionary containing the letters and your respective counts.

    """
    lttrs = {}

    if letter:
        letter = letter if diff_cl else letter.lower()
        lttrs[letter] = 0
        for c in str:
            c = c if diff_cl else c.lower()
            if c == letter:
                lttrs[c] += 1
    else:
        for c in str:
            c = c if diff_cl else c.lower()
            if c in lttrs:
                lttrs[c] += 1
            else:
                lttrs[c] = 1

    return lttrs


if __name__ == "__main__":
    from doctest import testmod

    testmod()
