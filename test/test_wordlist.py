from src.wordlist import classify_word, get_random_word, WORDS
from src.difficulty import Difficulty

def test_classify_word_by_length():
    # cane = 4 lettere → EASY
    assert classify_word("cane") == Difficulty.EASY
    # scuola = 6 lettere → EASY (perché la regola <=6 => EASY)
    assert classify_word("scuola") == Difficulty.EASY
    # programmazione = lunga → HARD
    assert classify_word("programmazione") == Difficulty.HARD

def test_classify_word_with_rare_letters():
    # parola corta ma con z → dovrebbe alzare la difficoltà almeno a MEDIUM
    result = classify_word("zulu")
    assert result in (Difficulty.MEDIUM, Difficulty.HARD)

def test_get_random_word():
    word = get_random_word(Difficulty.EASY)
    assert isinstance(word, str)
    assert len(word) > 0

def test_words_loaded():
    assert all(isinstance(w, str) for w in WORDS[Difficulty.EASY])
    assert all(isinstance(w, str) for w in WORDS[Difficulty.MEDIUM])
    assert all(isinstance(w, str) for w in WORDS[Difficulty.HARD])
