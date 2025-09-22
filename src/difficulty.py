from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

# Number of attempts is the same for all difficulties
ATTEMPTS = 10  

def parse_difficulty(value: str) -> Difficulty:
    """
    Convert a user input into Difficulty.
    Accepts: '1'/'easy', '2'/'medium', '3'/'hard' (case-insensitive).
    Raises ValueError for invalid inputs.
    """
    v = value.strip().lower()
    mapping = {
        "1": Difficulty.EASY,
        "easy": Difficulty.EASY,
        "facile": Difficulty.EASY,
        "2": Difficulty.MEDIUM,
        "medium": Difficulty.MEDIUM,
        "medio": Difficulty.MEDIUM,
        "3": Difficulty.HARD,
        "hard": Difficulty.HARD,
        "difficile": Difficulty.HARD,
    }
    try:
        return mapping[v]
    except KeyError as e:
        raise ValueError(f"Invalid difficulty: {value!r}") from e
