# Sistemi Dinamici
Appunti del corso _Introduzione ai Sistemi Dinamici_, raccolti durante l'anno accademico 2018-2019. I docenti del corso sono:
* Stefano Marmi
* Daniele Tantari
* Fracensco Grotto
* Ugo Bindini

## Struttura del progetto
Per ora l'idea è di trascrivere in TeX le lezioni separatamente e pensare più avanti ad una struttura più precisa degli argomenti.

Attualmente i file sono:
* `main.tex`: è il file principale della repository. Vengono importati tutti pacchetti necessari e ci sono le impostazioni generali del progetto. 
* `style.sty`: contiene tutte le impostazioni di stile del progetto. 
* `bibliografia.bib`: contiene la bibliografia.
* `Lezioni/lezione[anno]_[mese]_[giorno].tex`: è il vero contenuto di ogni lezione.

### Chi scrive cosa
|**Giorno** |**Docente**|**Tipo**     |**Scrittore**            |
|-----------|:---------:|-------------| ------------------------|
| 9 ottobre |Marmi      |Lezione      | @alepiazza              |
| 10 ottobre|Grotto     |Esercitazione| In attesa delle dispense|
| 16 ottobre|Marmi      |Lezione      | @arn4                   |
| 17 ottobre|Grotto     |Esercitazione| In attesa delle dispense|


### Come scrivere una lezione
A casua delle immagini il tempo di compilazione di `main.tex` può essere molto lungo. Quando includi un'immagine scrivi `\iffigureon` prima di `\begin{figure}` e `\fi` dopo `\end{figure}`. Se nel preambolo di `main.tex` scrivi `\figureontrue` dopo `\newif\iffigureon` le figure verranno include; se invece scrivi `\figureontflase` le immagini non compariranno nel pdf e la compilazione sarà più veloce.
