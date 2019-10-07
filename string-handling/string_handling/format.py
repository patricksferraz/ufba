# -*- coding: utf-8 -*-
"""
This is the format module.

The format module supplies one functions,
    del_accents()
For example,

>>> del_accents('IôiÔ')
'IoiO'
"""


from unicodedata import normalize


def del_accents(txt: str) -> str:
    """Return a string with the deleted accents.

    >>> del_accents('áéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãẽĩõũÃẼĨÕŨçÇ')
    'aeiouAEIOUaeiouAEIOUaeiouAEIOUcC'

    Parameters
    ----------
    txt : str
        String for deleting accents.

    Returns
    -------
    str
        String with the deleted accents.

    """
    return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
