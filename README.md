
# Implémentation de Hamming (7,4)

```console
foo@bar:~$ python3 hamming74.py

Entrez un nombre de 4 bits (entre 0 et 15) : 10
Entrez la position de l'erreur (entre 0 et 6) : 3
La représentation binaire : [1, 0, 1, 0]
Le message encodé sans erreur: [0, 1, 0, 0, 1, 0, 1]
Le message avec erreur: [0, 1, 0, 1, 1, 0, 1]
Données décodées et corrigées: [1, 0, 1, 0]
```

```console
foo@bar:~$ python3 hamming1511.py

Entrez un nombre de 11 bits (entre 0 et 2047) : 84
Entrez la position de l'erreur (entre 0 et 15) : 4
La représentation binaire : [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
Le message encodé sans erreur: [1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]
Le message avec erreur: [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]
Données décodées et corrigées: [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
```

