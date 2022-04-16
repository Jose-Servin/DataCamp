from mysimplepackage.simplemodule import count_words


def test_count_words():
    assert count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) == 6
