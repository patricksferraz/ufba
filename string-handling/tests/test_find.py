from string_handling.find import palindromes, letters


def test_palindromes():
    assert {"Socorram-me, subi no ônibus em Marrocos": 1} == palindromes(
        "Socorram-me, subi no ônibus em Marrocos"
    )


def test_letters():
    assert {
        "s": 4,
        "o": 5,
        "c": 2,
        "r": 4,
        "a": 2,
        "m": 4,
        "-": 1,
        "e": 2,
        ",": 1,
        " ": 5,
        "u": 2,
        "b": 2,
        "i": 2,
        "n": 2,
        "ô": 1,
    } == letters("Socorram-me, subi no ônibus em Marrocos")
