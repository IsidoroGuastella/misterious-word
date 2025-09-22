import random
from pathlib import Path
from src.difficulty import Difficulty

# lettere italiane meno comuni
RARE_LETTERS = set("zqxjkwy")

def classify_word(word: str) -> Difficulty:
    """Classify a word into a difficulty level using heuristics."""
    length = len(word)
    rare_count = sum(1 for ch in word if ch in RARE_LETTERS)

    # Easy: corte e senza lettere rare
    if length <= 6 and rare_count == 0:
        return Difficulty.EASY
    # Hard: molto lunghe o con tante lettere rare
    elif length >= 10 or rare_count >= 2:
        return Difficulty.HARD
    # Tutto il resto va su medium
    else:
        return Difficulty.MEDIUM

def load_words(fname: str) -> dict[Difficulty, list[str]]:
    """Load and classify words from a txt file using heuristics."""
    words = {Difficulty.EASY: [], Difficulty.MEDIUM: [], Difficulty.HARD: []}
    path = Path(__file__).resolve().parent.parent / "data" / fname

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if len(word) < 4:
                continue
            diff = classify_word(word)
            words[diff].append(word)

    return words

WORDS = load_words("parole_IT.txt")

def get_random_word(difficulty: Difficulty) -> str:
    return random.choice(WORDS[difficulty])
