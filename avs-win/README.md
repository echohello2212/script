Python-script som skapar en EICAR-testfil för att kontrollera om antivirus/EDR fungerar.
Krav
Windows
Python

Användning
python: av-test.py

Scriptet skapar AV-TEST-NOT-DANGEROUS.txt på Desktop och kontrollerar om AV/EDR reagerar.
Resultat
Filen saknas = AV/EDR reagerade (förväntat)
Filen finns kvar = AV/EDR reagerade inte
Obs: EICAR är en ofarlig teststräng, inte ett riktigt virus.
