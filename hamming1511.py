
#  ╭────────────────────────────────────────────────────────────────────╮
#  │ Nima BAYAT nima.bayat@etu.u-paris.fr                               │
#  │ Gabriel FONSECA RODRIGUES gabriel.fonseca-rodrigues@etu.u-paris.fr │
#  │ Zoe LOISEAU POILPRE zoe.poilpre@etu.u-paris.fr                     │
#  ╰────────────────────────────────────────────────────────────────────╯
#
#  ╭──────────────────────────────────────────────────────────────────────────────╮
#  │ L'implémentation de Hamming (15,11) pour commencer. Pour lancer,             │
#  │ utilisez la commande "python3 hamming1511.py".                               │
#  ╰──────────────────────────────────────────────────────────────────────────────╯
#
#  ────────────────────────────────────────────────────────────------------------
#
# ╭──────────────────────────────────────────────────────────────────────────────╮
# │ Ignorez tout ça, c'est simplement pour demander une saisie utilisateur       │
# │ et pour la coloration.                                                       │
# ╰──────────────────────────────────────────────────────────────────────────────╯

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[32m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'

def obtenir_nombre_11_bits():
    while True:
        try:
            saisie_utilisateur = int(input("Entrez un nombre de 11 bits (entre 0 et 2047) : "))
            if 0 <= saisie_utilisateur <= 2047:
                bit_array = [int(bit) for bit in bin(saisie_utilisateur)[2:].zfill(11)]
                return bit_array
            else:
                print("Veuillez entrer un nombre entre 0 et 2047.")
        except ValueError:
            print("Saisie invalide. Veuillez entrer un entier valide.")



def obtenir_la_position_de_l_erreur():
    while True:
        try:
            saisie_utilisateur = int(input("Entrez la position de l'erreur (entre 0 et 15) : "))
            if 0 <= saisie_utilisateur <= 6:
                return saisie_utilisateur
            else:
                print("Veuillez entrer un nombre entre 0 et 15.")
        except ValueError:
            print("Saisie invalide. Veuillez entrer un entier valide.")


#  ────────────────────────────────────────────────────────────---------------

def hamming_encode(data):
    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Calculer les bits de parité                              │
    #  ╰──────────────────────────────────────────────────────────╯
    p1 = data[0] ^ data[1] ^ data[3] ^ data[4] ^ data[6] ^ data[8] ^ data[10]
    p2 = data[0] ^ data[2] ^ data[3] ^ data[5] ^ data[6] ^ data[9] ^ data[10]
    p4 = data[1] ^ data[2] ^ data[3] ^ data[7] ^ data[8] ^ data[9] ^ data[10]
    p8 = data[4] ^ data[5] ^ data[6] ^ data[7] ^ data[8] ^ data[9] ^ data[10]

    hamming_code = [p1, p2, data[0], p4, data[1], data[2], data[3], p8, data[4], data[5], data[6], data[7], data[8], data[9], data[10]]

    return hamming_code

def hamming_decode(received):
    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Calculer les bits de contrôle de parité                  │
    #  ╰──────────────────────────────────────────────────────────╯
    s1 = received[0] ^ received[2] ^ received[4] ^ received[6] ^ received[8] ^ received[10] ^ received[12] ^ received[14]
    s2 = received[1] ^ received[2] ^ received[5] ^ received[6] ^ received[9] ^ received[10] ^ received[13] ^ received[14]
    s4 = received[3] ^ received[4] ^ received[5] ^ received[6] ^ received[11] ^ received[12] ^ received[13] ^ received[14]
    s8 = received[7] ^ received[8] ^ received[9] ^ received[10] ^ received[11] ^ received[12] ^ received[13] ^ received[14]

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Calculer la position de l'erreur en décimal              │
    #  ╰──────────────────────────────────────────────────────────╯
    error_position = s1 + 2 * s2 + 4 * s4 + 8 * s8

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Si error_position_decimal n'est pas égal à 0, il         │
    #  │  corrige l'erreur ; sinon, le message est correct        │
    #  ╰──────────────────────────────────────────────────────────╯
    if error_position != 0:
        received[error_position - 1] ^= 1

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Extract the original data                                │
    #  ╰──────────────────────────────────────────────────────────╯
    decoded_data = [received[2], received[4], received[5], received[6], received[8], received[9], received[10], received[11], received[12], received[13], received[14]]

    return decoded_data

#  ────────────────────────────────────────────────────────────---------------

#  ╭──────────────────────────────────────────────────────────╮
#  │ demander à l'utilisateur d'entrer un nombre de 15 bits   │
#  ╰──────────────────────────────────────────────────────────╯

bits = obtenir_nombre_11_bits()

#  ╭──────────────────────────────────────────────────────────╮
#  │ demander à l'utilisateur d'entrer la position de l'erreur│
#  ╰──────────────────────────────────────────────────────────╯

position = obtenir_la_position_de_l_erreur();

#  ╭──────────────────────────────────────────────────────────╮
#  │ Encoder le message                                       │
#  ╰──────────────────────────────────────────────────────────╯

encoded_message = hamming_encode(bits)
print(Colors.BLUE + f"La représentation binaire : {bits}", Colors.RESET)
print(Colors.YELLOW + "Le message encodé sans erreur:", encoded_message, Colors.RESET)

#  ╭──────────────────────────────────────────────────────────╮
#  │ Simuler une erreur en inversant un bit                   │
#  ╰──────────────────────────────────────────────────────────╯

received_message = encoded_message.copy()
received_message[position] ^= 1

print(Colors.RED + "Le message avec erreur:", received_message , Colors.RESET)

#  ╭──────────────────────────────────────────────────────────╮
#  │ Décoder le message                                       │
#  ╰──────────────────────────────────────────────────────────╯

decoded_data = hamming_decode(received_message)

print(Colors.BLUE + "Données décodées et corrigées:", decoded_data, Colors.RESET)

