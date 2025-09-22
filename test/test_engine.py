from src.engine import start_game
from src.user import User
from src.difficulty import Difficulty
import src.engine as engine

def test_engine_runs(monkeypatch, capsys):
    # forza la parola segreta su qualcosa di facile
    monkeypatch.setattr(engine, "get_random_word", lambda _: "cane")

    player = User(nome="Tester", level=Difficulty.EASY)

    # input sufficienti: lettere della parola + 'n' per uscire
    inputs = iter(["c", "a", "n", "e", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    start_game(player)

    captured = capsys.readouterr()
    assert "Complimenti Tester" in captured.out
