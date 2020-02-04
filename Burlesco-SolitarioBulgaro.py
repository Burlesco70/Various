"""
   Compitino di Elementi di Informatica e Programmazione - Novembre 2019

   Copiare questo file in CognomeMatricola.py usando il proprio cognome
   e il proprio numero di matricola. Se il cognome contiene spazi o apostrofo,
   ignorarli; se contiene lettere accentate, usare la corrispondente lettera
   non accentata.
   
   MODIFICARE SOLTANTO IL FILE CognomeMatricola.py !!!!!!!!
   Quello sara' il file valutato per l'esame.

   TEMPO A DISPOSIZIONE = 1 ora e 15 minuti (75 minuti)
   
   Il progetto consiste nello sviluppo di alcune funzioni cooperanti tra loro,
   ma la struttura della cooperazione (cioe' dell'interazione tra le funzioni)
   e' gia' delineata.
   
   [IMPORTANTE SOPRATTUTTO PER I "RIPETENTI" (ma non solo)]
   Non e' possibile utilizzare caratteristiche del linguaggio che non siano
   state presentate a lezione in questo anno accademico.

   Ciascuna funzione e' descritta nel commento che la precede, che a volte
   contiene anche delle prescrizioni o dei divieti da seguire durante la
   scrittura del codice che valgono soltanto per la funzione a cui si riferisce il commento.
   
   Alcune sezioni di codice sono gia' presenti e non possono essere modificate!
   Le sezioni di codice mancante e da scrivere sono identificate dal commento
   # SCRIVERE QUI 
   
   Il "solitario bulgaro" e' un passatempo che richiede 45 carte da gioco (o altri
   oggetti, dal momento che il valore delle carte non viene utilizzato): non lo si 
   puo' considerare un gioco o un rompicapo perche' il "giocatore" non prende mai
   decisioni, deve soltanto applicare delle regole e procedere fino alla conclusione.
   Si inizia suddividendo le carte in "mucchietti" (che chiameremo, in inglese, "heap",
   che significa, appunto, "mucchio"): il numero dgli heap e' casuale e il numero
   di carte in ciascun heap e' casuale, l'unico vincolo e' che la somma delle
   dimensioni (ovvero del numero di carte) di tutti gli heap sia 45.
   Sono valide anche configurazioni iniziali "degeneri",
   come "un solo heap con 45 carte" oppure "45 heap con una carta ciascuno",
   mentre una configurazione non degenere potrebbe essere:
   5 heap di dimensione 20, 5, 1, 9, 10, rispettivamente.
   Ogni fase di gioco segue questa regola: prendi una carta da ciascuno heap e,
   con queste, crea un nuovo heap, posto alla destra di quelli esistenti;
   uno heap che diventa vuoto scompare.
   Il "gioco" termina quando sono presenti 9 heap, con dimensioni
   1, 2, 3, 4, 5, 6, 7, 8 e 9, in qualsiasi ordine.
   (si puo' dimostrare che il "gioco" termina sempre!)

   Ecco l'esempio di una "partita":
   
   Vuoi giocare? 
   [11, 26, 7, 1] # configurazione iniziale casuale ma valida (numeri positivi con somma 45)
   [10, 25, 6, 4] # lo heap che aveva una carta e' scomparso
   [9, 24, 5, 3, 4]
   [8, 23, 4, 2, 3, 5]
   [7, 22, 3, 1, 2, 4, 6]
   [6, 21, 2, 1, 3, 5, 7] # lo heap che aveva una carta e' scomparso
   [5, 20, 1, 2, 4, 6, 7] # lo heap che aveva una carta e' scomparso
   [4, 19, 1, 3, 5, 6, 7] # lo heap che aveva una carta e' scomparso
   [3, 18, 2, 4, 5, 6, 7] # lo heap che aveva una carta e' scomparso
   [2, 17, 1, 3, 4, 5, 6, 7]
   [1, 16, 2, 3, 4, 5, 6, 8] # lo heap che aveva una carta e' scomparso
   [15, 1, 2, 3, 4, 5, 7, 8] # lo heap che aveva una carta e' scomparso
   [14, 1, 2, 3, 4, 6, 7, 8] # lo heap che aveva una carta e' scomparso
   [13, 1, 2, 3, 5, 6, 7, 8] # lo heap che aveva una carta e' scomparso
   [12, 1, 2, 4, 5, 6, 7, 8] # lo heap che aveva una carta e' scomparso
   [11, 1, 3, 4, 5, 6, 7, 8] # lo heap che aveva una carta e' scomparso
   [10, 2, 3, 4, 5, 6, 7, 8] # lo heap che aveva una carta e' scomparso
   [9, 1, 2, 3, 4, 5, 6, 7, 8] # configurazione "vincente"
   Numero di mosse: 17
   
"""
def main() :
   """
      Alcuni collaudi... NON MODIFICARE
   """
   if (
       play([1, 2, 3, 4, 9, 8, 7, 6, 5]) == 0   # configurazione iniziale gia' "vincente"
	   and play([20, 5, 1, 9, 10]) == 39
	   and play([45]) == 36                     # configurazione iniziale "degenere"
	   and play([1] * 45) == 37                 # altra configurazione iniziale "degenere"
	   and play([1, 2, 3, 4, 9, 8, 7, 6]) == -1 # configurazione iniziale errata
	   and play([50, -5]) == -1                 # configurazione iniziale errata
	   and play([]) == -1                       # configurazione iniziale vuota, quindi errata
	  ) :
      print("Collaudo riuscito (ma non significa che non ci siano errori...)")
   else :
      print("Collaudo non riuscito")
   """
   Qui sotto si possono inserire altri collaudi, ma poi devono essere eliminati (o commentati).
   """
   # EVENTUALMENTE SCRIVERE QUI
   """
   Il codice seguente gestisce ripetute esecuzioni del passatempo
   a partire da configurazioni generate casualmente, fino a quando l'utente non
   chiede di terminare. La sequenza delle operazioni e':
   1) chiedi all'utente se vuole giocare:
      se la risposta INIZIA con n o N, termina;
      con qualsiasi altra risposta (anche "vuota") prosegui
      (in pratica, premendo ripetutamente "Enter" o "Invio" si continua a giocare)
   2) genera una nuova "partita" invocando createRandomConfig
   3) "gioca" fino alla fine, invocando play
   4) visualizza il numero di fasi eseguite
   5) torna al punto 1)
   """
   # SCRIVERE QUI
   while not(input("Vuoi giocare? S/N").lower().startswith("n")):
      play(createRandomConfig())
# fine main

## Crea e restituisce una configurazione iniziale casuale valida per il solitario bulgaro.
#  Crea una configurazione iniziale casuale, con questo algoritmo:
#     crea una nuova lista vuota
#     carte disponibili = 45
#     finche' ci sono carte disponibili
#        genera un numero intero casuale nell'intervallo [1,carte disponibili]
#        sottrae tale dimensione al numero di carte disponibili
#        aggiunge tale dimensione in fondo alla lista
#  @return una configurazione iniziale casuale valida per il solitario bulgaro
def createRandomConfig() :
   from random import randint
   heapList = [] # la lista da riempire e restituire
   carte_disp = 45
   while (carte_disp > 0):
      heapList.append(randint(1,carte_disp))
      carte_disp -= heapList[-1]
   return heapList   
# fine createRandomConfig  

## Fa una mossa del gioco.
#  Riceve la lista degli heap (cioe' delle loro dimensioni)
#  e, agendo su tale lista, riduce di un'unita' la dimensione di
#  tutti gli heap, eliminando quelli che rimangono vuoti;
#  infine, aggiunge un nuovo heap in fondo alla lista, con
#  la dimensione opportuna.
#  @param heapList la lista degli heap attuale, che viene modificata
def nextMove(heapList) :
   newheapList = []
   heapListCount = len(heapList)
   for h in heapList:
      if h>1:
         newheapList.append(h-1)
   newheapList.append(heapListCount)
   return newheapList
# fine nextMove  

## Verifica se il gioco e' finito.
#  Riceve la lista degli heap (cioe' delle loro dimensioni)
#  e restituisce True se il gioco e' finito, altrimenti restituisce False.
#  La funzione NON PUO' MODIFICARE la lista, ne' crearne una copia.
#  @param heapList la lista degli heap attuale
#  @return True se il gioco e' finito, False altrimenti
def finished(heapList) :
   return set(heapList) == {1,2,3,4,5,6,7,8,9}
# fine finished  
   
## Gioca una partita visualizzando le mosse e restituendo il numero di mosse.
#  Riceve la lista iniziale degli heap (cioe' delle loro dimensioni)
#  e fa una mossa dopo l'altra (invocando nextMove), dopo aver verificato che
#  il gioco non sia finito (invocando finished).
#  Visualizza il contenuto iniziale degli heap (passando la lista alla funzione print),
#  poi dopo ogni mossa visualizza di nuovo la lista, nello stesso modo.
#  Quando il gioco e' terminato, restituisce il numero di mosse effettuate.
#  Attenzione: potrebbero essere sufficienti ZERO mosse... se la configurazione
#  iniziale e' gia' una di quelle "vincenti".
#  Se la lista iniziale non e' valida, visualizza la lista e un messaggio d'errore,
#  poi termina restituendo -1 (attenzione: pensare bene a quali condizioni devono
#  essere inizialmente valide per la lista; e' lecito ipotizzare, per semplicita',
#  che sia una lista di numeri interi, eventualmente vuota).
#  @param heapList la lista degli heap attuale, che viene modificata;
#                  potrebbe non essere valida
#  @return il numero di mosse effettuate
def play(heapList) :
   #Check heapList for sum and positive values
   if not(sum(x for x in heapList if x > 0) == 45):
      print(heapList, ": configurazione errata")
      return -1
   #Standard algorithm
   i = 0   
   while not(finished(heapList)):
      print(i, heapList)
      heapList = nextMove(heapList)
      i = i+1
   return i
# fine play  

main()
