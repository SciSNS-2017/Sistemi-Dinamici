[![build status](https://gitlab.com/marco-venuti/sistemi-dinamici/badges/master/build.svg)](https://gitlab.com/marco-venuti/sistemi-dinamici/-/jobs/artifacts/master/raw/Sistemi-Dinamici.pdf?job=compile_pdf)
# Sistemi Dinamici
Appunti del corso _Introduzione ai Sistemi Dinamici_, raccolti durante l'anno accademico 2018-2019. I docenti del corso sono:
* Stefano Marmi
* Daniele Tantari
* Fracensco Grotto
* Ugo Bindini

Il PDF più recente si può scaricare [qui](https://gitlab.com/marco-venuti/sistemi-dinamici/-/jobs/artifacts/master/raw/Sistemi-Dinamici.pdf?job=compile_pdf).

### Struttura del progetto
Per ora l'idea è di trascrivere in TeX le lezioni separatamente e pensare più avanti ad una struttura più precisa degli argomenti.

Attualmente i file sono:
* `main.tex`: è il file principale della repository. Vengono importati tutti pacchetti necessari e ci sono le impostazioni generali del progetto.
* `style.sty`: contiene tutte le impostazioni di stile del progetto, include alcuni pacchetti e definisce nuovi comandi, ambienti theorem ecc. utili per velocizzare la scrittura e uniformare lo stile.
* `bibliografia.bib`: contiene la bibliografia.
* `Lezioni/lezione[anno]_[mese]_[giorno].tex`: è il vero contenuto di ogni lezione.

### Elenco lezioni
| **Giorno**  | **Docente** | **Scrittore**             |
|-------------|-------------|---------------------------|
| 9 ottobre   | Marmi       | @alepiazza                |
| 10 ottobre  | Grotto      | @Konnoi5, @marco-venuti   |
| 16 ottobre  | Marmi       | @arn4, @marco-venuti      |
| 17 ottobre  | Grotto      | @marco-venuti             |
| 23 ottobre  | Bindini     | @alepiazza                |
| 24 ottobre  | Marmi       | @alepiazza                |
| 30 ottobre  | Bindini     | @alepiazza, @marco-venuti |
| 7 novembre  | Tantari     |                           |
| 13 novembre | Grotto      |                           |
| 14 novembre | Marmi       | @alepiazza, @marco-venuti |
| 20 novembre | Marmi       | @alepiazza                |
| 21 novembre | Marmi       | @alepiazza                |
| 27 novembre | Marmi       | @alepiazza                |
| 28 novembre | Tantari     |                           |
| 4 dicembre  | Marmi       |                           |
| 5 dicembre  | Tantari     |                           |
| 11 dicembre | Bindini     |                           |
| 12 dicembre | Tantari     | @marco-venuti             |
| 18 dicembre | Correzione  |                           |
| 19 dicembre | Marmi       | @alepiazza                |
| 8 gennaio   | Marmi       | @alepiazza                |
| 9 gennaio   | Marmi       |                           |
| 15 gennaio  | Grotto      |                           |
| 16 gennaio  | Tantari     |                           |
| 22 gennaio  | Bindini     |                           |
| 23 gennaio  | Bindini     |                           |
| 29 gennaio  | Marmi       |                           |
| 30 gennaio  | Marmi       |                           |
| 5 febbraio  | Tantari     |                           |
| 6 febbraio  | Tantari     |                           |

### Come scrivere una lezione
A causa delle immagini il tempo di compilazione di `main.tex` può essere molto lungo. Quando includi un'immagine scrivi `\iffigureon` prima di `\begin{figure}` e `\fi` dopo `\end{figure}`. Se nel preambolo di `main.tex` scrivi `\figureontrue` dopo `\newif\iffigureon` le figure verranno incluse; se invece scrivi `\figureonfalse` le immagini non compariranno nel pdf e la compilazione sarà più veloce.
