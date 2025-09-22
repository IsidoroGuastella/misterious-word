
# La parola misteriosa
Indice dei contenuti:
- [Regole del gioco](#Regole-del-gioco)
- [Scopo](#Scopo)
- [Come termina la partita](#Come-termina-la-partita)



## Regole del gioco
*La parola misteriosa* è un gioco d'astuzia ed intelligenza, dove l'utente che gioca ha a disposizione 10 tentativi.
Di volta in volta il giocatore potrà scegliere una modalità di gioco tra quelle possibili, ovvero **facile**, **medio** o **difficile**, dove cambia la lunghezza delle parole.
È possibile momentaneamente giocare solamente con parole italiane. L'utilizzo di vocaboli estranei alla sola lingua italiana verrà implementato successivamente. 

## Scopo
Lo scopo del gioco è indovinare la parola nascosta fornendo al computer, di volta in volta, delle lettere.
Ogni lettera fornita sarà un tentativo:
- Se la lettera è contenuta all'interno della parola, almeno una volta, il numero di tentativi rimane invariato e viene inserita la lettera in tutte le postazioni nella quale essa è contenuta;
- Se la lettera non è contenuta all'interno della parola nascosta, il tentativo verrà sacrificato e il numero dei tentativi possibili verrà decrementato.

## Come termina la partita
Se i tentativi dovessero terminare prima di aver indovinato la parola nascosta, l'utente avrà perso la partita.

Se i tentativi non dovessero terminare e la parola nascosta viene scoperta la partita termina e l'utente avrà vinto.

In entrambi i casi, la partita termina e l’utente potrà scegliere se iniziare una nuova sfida.