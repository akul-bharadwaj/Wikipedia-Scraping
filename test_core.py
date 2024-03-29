from nlp.core import get_phrases


def test_get_phrase():
    assert "royal challengers" in get_phrases("Royal Challengers Bengaluru")
