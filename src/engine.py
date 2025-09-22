from __future__ import annotations
from typing import Set
from src.wordlist import get_random_word
from src.user import User
from src.difficulty import Difficulty

def start_game(player: User) -> None:
    secret = get_random_word(player.level)
    attempts = player.attempts()
    guessed = ["_" for _ in secret]
    tried_letters: Set[str] = set()

    print("\nInizia la partita!\n")
    print("Parola:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        raw = input("Inserisci una lettera: ").strip().lower()
        if not raw or len(raw) != 1 or not raw.isalpha():
            print("Inserisci una singola lettera valida.\n")
            continue

        if raw in tried_letters:
            print("Hai già provato questa lettera.\n")
            continue

        tried_letters.add(raw)

        if raw in secret:
            for i, ch in enumerate(secret):
                if ch == raw:
                    guessed[i] = raw
            print("Lettera corretta!")
        else:
            attempts -= 1
            print(f"Lettera errata. Tentativi rimasti: {attempts}")

        print("Parola:", " ".join(guessed))
        print("Lettere provate:", ", ".join(sorted(tried_letters)))
        print()

    if "_" not in guessed:
        print(f"🎉 Complimenti {player.nome}! Hai indovinato la parola: {secret}")
        player.wins += 1
        if player.level == Difficulty.EASY:
            player.easy_solved += 1
        elif player.level == Difficulty.MEDIUM:
            player.medium_solved += 1
        elif player.level == Difficulty.HARD:
            player.hard_solved += 1
    else:
        print(f"💀 Hai esaurito i tentativi. La parola era: {secret}")
        player.losses += 1

    answ = input("\nVuoi giocare un'altra partita? [Y/N] ").strip().lower()
    if answ in ("y", "s"):
        start_game(player)
    else:
        player.print_summary()
        print("\nGrazie per aver giocato — alla prossima!")
