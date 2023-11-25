#  ╭────────────────────────────────────────────────────────────────────╮
#  │ Nima BAYAT nima.bayat@etu.u-paris.fr                               │
#  │ Gabriel FONSECA RODRIGUES gabriel.fonseca-rodrigues@etu.u-paris.fr │
#  │ Zoe LOISEAU POILPRE zoe.poilpre@etu.u-paris.fr                     │
#  ╰────────────────────────────────────────────────────────────────────╯
#
#  ╭──────────────────────────────────────────────────────────────────────────────╮
#  │ L'implémentation de Hamming (7,4) pour commencer. Pour lancer,               │
#  │ utilisez la commande "python3 hamming74.py".                                 │
#  ╰──────────────────────────────────────────────────────────────────────────────╯
#
#  ────────────────────────────────────────────────────────────
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

def obtenir_nombre_4_bits():
    while True:
        try:
            saisie_utilisateur = int(input("Entrez un nombre de 4 bits (entre 0 et 15) : "))
            if 0 <= saisie_utilisateur <= 15:
                bit_array = [int(bit) for bit in bin(saisie_utilisateur)[2:].zfill(4)]
                return bit_array
            else:
                print("Veuillez entrer un nombre entre 0 et 15.")
        except ValueError:
            print("Saisie invalide. Veuillez entrer un entier valide.")

def obtenir_la_position_de_l_erreur():
    while True:
        try:
            saisie_utilisateur = int(input("Entrez la position de l'erreur (entre 0 et 6) : "))
            if 0 <= saisie_utilisateur <= 6:
                return saisie_utilisateur
            else:
                print("Veuillez entrer un nombre entre 0 et 6.")
        except ValueError:
            print("Saisie invalide. Veuillez entrer un entier valide.")

#  ────────────────────────────────────────────────────────────

def hamming74_encode(data):
    if len(data) != 4:
        raise ValueError("La longueur des données doit être de 4 bits.")

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Calculer les trois bits de parité                        │
    #  ╰──────────────────────────────────────────────────────────╯

    p1 = data[3] ^ data[2] ^ data[0]  
    p2 = data[3] ^ data[1] ^ data[0] 
    p4 = data[2] ^ data[1] ^ data[0] 

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Construisez le message codé en plaçant les bits          │
    #  │  de parité aux positions 0, 1, 3, et le reste des        │
    #  │  bits du message aux positions 2, 4, 5, 6, mais de       │
    #  │  droite à gauche, comme Hamming lui-même les a           │
    #  │  écrits de cette manière.                                │
    #  ╰──────────────────────────────────────────────────────────╯

    encoded_message = [p1, p2, data[3], p4, data[2], data[1], data[0]]

    return encoded_message

#  ────────────────────────────────────────────────────────────

def hamming74_decode(received_message):

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Calculer les trois bits de contrôle de parité            │
    #  ╰──────────────────────────────────────────────────────────╯
    
    c1 = received_message[0] ^ received_message[2] ^ received_message[4] ^ received_message[6]
    c2 = received_message[1] ^ received_message[2] ^ received_message[5] ^ received_message[6]
    c4 = received_message[3] ^ received_message[4] ^ received_message[5] ^ received_message[6]

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Calculer la position de l'erreur en décimal              │
    #  ╰──────────────────────────────────────────────────────────╯
    
    error_position_decimal = c1 * 1 + c2 * 2 + c4 * 4
    
    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Si error_position_decimal n'est pas égal à 0, il         │
    #  │  corrige l'erreur ; sinon, le message est correct        │
    #  ╰──────────────────────────────────────────────────────────╯
    
    if error_position_decimal != 0:
        received_message[error_position_decimal - 1] ^= 1 

    #  ╭──────────────────────────────────────────────────────────╮
    #  │ Extract the original data                                │
    #  ╰──────────────────────────────────────────────────────────╯
    decoded_data = [received_message[6], received_message[5], received_message[4], received_message[2]]

    return decoded_data




#  ╭──────────────────────────────────────────────────────────╮
#  │ demander à l'utilisateur d'entrer un nombre de 4 bits    │
#  ╰──────────────────────────────────────────────────────────╯

bits = obtenir_nombre_4_bits()

#  ╭──────────────────────────────────────────────────────────╮
#  │ demander à l'utilisateur d'entrer la position de l'erreur│
#  ╰──────────────────────────────────────────────────────────╯

position = obtenir_la_position_de_l_erreur()


#  ╭──────────────────────────────────────────────────────────╮
#  │ Encoder le message                                       │
#  ╰──────────────────────────────────────────────────────────╯

encoded_message = hamming74_encode(bits)
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

decoded_data = hamming74_decode(received_message)

print(Colors.BLUE + "Données décodées et corrigées:", decoded_data, Colors.RESET)

