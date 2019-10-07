from string_handling.format import del_accents


def test_del_accents():
    assert "aeiouAEIOUaeiouAEIOUaeiouAEIOUcC" == del_accents(
        "áéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãẽĩõũÃẼĨÕŨçÇ"
    )
