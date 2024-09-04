import pytest
from main import find_removed_word

def test_find_removed_word():
    sentence = "Ложка, лес, комбайн, льдина, обезьяна, микроволновка, видеокарта – это слова"
    assert find_removed_word(sentence) == "микроволновка"
