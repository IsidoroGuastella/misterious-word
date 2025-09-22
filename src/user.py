from __future__ import annotations
from src.difficulty import parse_difficulty, Difficulty, ATTEMPTS

class User:
    def __init__(self, nome: str = "Guest", level: Difficulty | None = None) -> None:
        self.nome = nome
        self.level = level

        # statistiche
        self.wins = 0
        self.losses = 0
        self.easy_solved = 0
        self.medium_solved = 0
        self.hard_solved = 0

    def welcome(self) -> None:
        print(f"Benvenuto al gioco della 'Parola misteriosa', {self.nome}!\n")

        answ = input("Vuoi cambiare nickname? [Y/N] ").strip().lower()
        while answ not in ("y", "n", "s"):
            print("Risposta non valida. Inserisci 'Y' o 'N'.")
            answ = input("Vuoi cambiare nickname? [Y/N] ").strip().lower()
        if answ in ("y", "s"):
            self.change_name()

        self.choose_level()

    def change_name(self) -> None:
        while True:
            new = input("Inserisci il nuovo nickname: ").strip()
            if new:
                self.nome = new
                print(f"Nickname aggiornato: {self.nome}\n")
                return
            print("Nickname non valido, riprova.")

    def choose_level(self) -> None:
        prompt = (
            "\nSeleziona il livello di gioco (numero o nome):\n"
            "[1] Facile\n"
            "[2] Medio\n"
            "[3] Difficile\n"
            "Scelta: "
        )
        while True:
            raw = input(prompt)
            try:
                self.level = parse_difficulty(raw)
                print(f"Livello impostato su: {self.level.name}\n")
                return
            except ValueError as e:
                print(f"{e}\nRiprova.\n")

    def attempts(self) -> int:
        return ATTEMPTS

    def print_summary(self) -> None:
        """Mostra un riepilogo delle statistiche del giocatore."""
        print("\n=== RIEPILOGO PARTITE ===")
        print(f"Giocatore: {self.nome}")
        print(f"Vittorie: {self.wins}")
        print(f"Sconfitte: {self.losses}")
        print("Parole indovinate per livello:")
        print(f"  Facile    -> {self.easy_solved}")
        print(f"  Medio     -> {self.medium_solved}")
        print(f"  Difficile -> {self.hard_solved}")
        print("=========================\n")
