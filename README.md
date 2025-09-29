# The mysterious word - Developer Documentation

## Table of Contents
- [Code Overview](#code-overview)
- [Requirements](#requirements)
- [How To Run](#how-to-run)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

## Code Overview

### `data/words.py`
Contains the word dataset used during the game. Words may later be categorized by difficulty.

### `src/difficulty.py`
Handles difficulty levels (easy, medium, hard).  
Defines rules such as attempt count or word pool.

### `src/engine.py`
Implements the main game engine:  
- Loads a random word.  
- Tracks attempts.  
- Updates the word reveal status.  
- Determines win/lose conditions.  

### `src/wordlist.py`
Provides utilities to fetch and manage word lists.  
Abstracted from the engine to allow dataset expansion.

### `main.py`
Entry point of the application:
- Initializes the user.
- Calls the engine to start a match.


## Requirements 
The **minimum Python version** required is **3.8**. The older ones won't work.

Dependencies listed in **requirements.txt** (currently none, standard library only).
Install them with:
```
pip install -r requirements.txt
```
## How To Run
From the project root:
```
python engine.py
```

## Roadmap
- [x] Implement complete game loop inside engine.py.
- [ ] Expand words.py with categorized datasets.
- [ ] Implement words from different languages.
- [x] Add support for playing multiple matches without restarting.
- [x] Implement player statistics (wins/losses, difficulty history).
- [x] Improve test coverage.
- [ ] Optional: graphical interface (Tkinter or web).

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Add tests for your changes.
4. Open a Pull Request with a clear description.