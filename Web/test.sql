Calcolare il codice e il cognome degli autori che non 
hanno scritto alcun libro con più di 10 copie vendute. 

SELECT distinct a.codice, a.cognome
FROM autore a
where not exists (
    SELECT s.codiceaut
    FROM scritto s join libro l
    on s.titolo= l.titolo
    WHERE s.codiceaut = a.codice AND l.copievendute > 10
)

"Calcolare, per ogni autore con età maggiore di 30 anni, il codice dell
'autore ed il numero di copie vendute considerando tutti i suoi libri scritti, 
ma restringendo l’attenzione solo agli autori che hanno scritto almeno 2 libri. "


SELECT s.codiceaut, sum(l.copievendute)
from scritto s join libro l
on s.titolo = l.titolo
join autore a
on s.codiceaut = a.codice
where a.eta > 30 
group by s.codiceaut
having count(s.titolo) >= 2

"Calcolare per ogni autore la media delle copie vendute tra i libri scritti da lui, mostrando il codice dell’autore e tale media." 
