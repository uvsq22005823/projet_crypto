import tkinter as tk

texte1 = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
texte2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
texte3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"


def decalage(lettre_message, lettre_cle):
    """Alors ça c'est la correction mais ça marche pas bien -_-"""
    return chr((ord(lettre_message) + ord(lettre_cle))%256)


def dec_texte(texte, cle):
    texte_code = ""
    t, c = 0, 0
    while len(texte_code) < len(texte):
        if texte[t] == " " or texte[t] == ":" or texte[t] == "," or texte[t] == "?" or texte[t] == "." or texte[t] == "2" or texte[t] == "6":
            texte_code += texte[t]
        else:
            texte_code += decalage(texte[t], cle[c%len(cle)])
        t, c = t + 1, c + 1
        if c == len(cle):
            c = 0
    return texte_code


def chiffre():
    resultat.delete(0, tk.END)
    if entree_texte.get() == "" or entree_cle.get() == "":
        label_res.config(text="Il manque quelque chose en entrée :/")
    resultat.insert(0, dec_texte(entree_texte.get(), entree_cle.get()))


def chiffre_deux(texte, clef):
    resultat.delete(0, tk.END)
    resultat.insert(0, dec_texte(texte, clef))
    return dec_texte(texte, clef)


def dechiffrement(texte_a_decoder, cle):
    texte_decode = ""
    t, c = 0, 0
    while len(texte_decode) < len(texte_a_decoder):
        if texte_a_decoder[t] == " " or texte_a_decoder[t] == ":" or texte_a_decoder[t] == "," or texte_a_decoder[t] == "?" or texte_a_decoder[t] == "." or texte_a_decoder[t] == "2" or texte_a_decoder[t] == "6":
            texte_decode += texte_a_decoder[t]
        else:
            texte_decode += decalage(texte_a_decoder[t], chr(256-ord(cle[c%len(cle)])))
        t, c = t + 1, c + 1
        if c == len(cle):
            c = 0
    return texte_decode


def dechiffre():
    resultat.delete(0, tk.END)
    if entree_texte.get() == "" or entree_cle.get() == "":
        label_res.config(text = "Il manque quelque chose en entrée :/")
    else:
        resultat.insert(0, dechiffrement(entree_texte.get(), entree_cle.get()))


def chiffre_xor(lettre_message, lettre_cle):
    return chr(ord(lettre_message) ^ ord(lettre_cle))


def creer_liste_clef(taille):
    possibilite_clef = [chr(i) for i in range(256)]
    for i in range(taille):
        # On crée une liste de toutes les combinaisons possibles
        a = [j for j in possibilite_clef]  # On ajoute notre alphabet à a
        for y in range(i):
            a = [x + j for j in possibilite_clef for x in a]
    return a


def brute_force_cesar(texte_a_trouver):
    """Trouve une clé longue de 1 et une suite de caractères qui
       correspondent au texte à trouver. Pas sûr de l'idée."""
    alphabet = "abcdefghijklmnopqrstuvwxyz :,?.0123456789'"
    # Tous les caractères possibles / vus dans les textes à décoder
    liste_car = []
    # Liste vide qui contiendra les combinaisons de caractères possibles
    texte_test = ""
    # Texte codé à comparé avec le texte initial
    l = 0 # Index de liste_car
    m = 0  # Index de la clef
    t = 1  # Taille clef
    clef = creer_liste_clef(t)
    for i in range(len(texte_a_trouver)):
        # On crée une liste de toutes les combinaisons possibles
        a = [j for j in alphabet]  # On ajoute notre alphabet à a
        for y in range(i):
            a = [x + j for j in alphabet for x in a]
            # On ajoute chaque caractère à chaque caractère
            # (pas sûr de cette phrase -_-)
    liste_car = liste_car + a  # On ajoute ce qu'on a trouvé à notre liste
    while texte_test != texte_a_trouver:  
        # Tant qu'on code pas pareil que ce qu'on cherche
        texte_test = chiffre_deux(str(liste_car[l]), clef) 
        # On teste l'encodage avec le texte et la clef actuels
        l += 1 # On regarde le caractère suivant
        if l >= len(liste_car):  # Ne pas aller out of range
            l = 0
            m += 1  # On change la clef
            if m == 256:
                t += 1
                clef = creer_liste_clef(t)
    m += -1
    entree_cle.insert(0, clef[m])
    return ord(clef[m])


racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

entree_cle = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_cle.grid(row = 1, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

label_cle = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer la clé ici.")
label_cle.grid(row = 1, column = 1)

bouton_coder=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)

bouton_decoder=tk.Button(racine,text="Déchiffrer texte",fg="black",  width=15,command=dechiffre)
bouton_decoder.grid(row=2, column=1)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)

label_res=tk.Label(racine,font = ("helvetica", "20"), text="Résultat ici.")
label_res.grid(row = 3, column=1)

# print("La clef est : chr", brute_force_cesar("kd"))
# La clé trouvée est chr 255 -> ÿ (pb lié au code initial ?)
texte1_decode = "le prochain fichier aura un code par substitution alphabetique: chaque lettre est remplacee par une autre. utiliser la frequence des lettres pour decoder le message."

alphabet_francais = [[7.11, 'a'], [1.14, 'b'], [3.18, 'c'], [3.67, 'd'], [12.10, 'e'], [1.11, 'f'], [1.23, 'g'], [1.11, 'h'], [6.59, 'i'], [0.34, 'j'], [0.29, 'k'], [4.96, 'l'], [2.62, 'm'], [6.39, 'n'], [5.02, 'o'], [2.49, 'p'], [0.65, 'q'], [6.07, 'r'], [6.51, 's'], [5.92, 't'], [4.49, 'u'], [1.11, 'v'], [0.17, 'w'], [0.38, 'x'], [0.46, 'y'], [0.15, 'z']]


def str_convert(liste):
    """Renvoie un texte depuis une liste qui contient un texte découpé"""
    texte_str = ""
    for a in range(len(liste)):
        texte_str += str(liste[a])
    return texte_str


def trouver_frequence_lettre(lettre, texte):
    """Trouve le nombre d'itérations d'une lettre dans un texte"""
    # Oui le nom porte à confusion
    compteur = 0
    for i in texte:
        if i == lettre:
            compteur += 1
    return compteur


def trouver_frequence_texte(texte):
    """Applique la fonction précédante pour toutes les lettres"""
    # On obtient vraiment une fréquence cette fois
    alphabet_francais_texte = [0 for i in range(26)]
    for i in range(26):
        alphabet_francais_texte[i] = [alphabet_francais_texte[i], chr(i + 97)]
    for i in range(26):
        alphabet_francais_texte[i][0] = round((trouver_frequence_lettre(chr(i + 97), texte) * 100) / len(texte), 3)
    alphabet_francais_texte.sort(reverse=True)
    return alphabet_francais_texte


def substituer(texte):  # Donne une vague idée mais pas efficace, mal codé
    """Remplace les lettres selon leur fréquence, en se basant sur
       la fréquence moyenne d'apparition des lettres dans
       l'alphabet français."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    texte_lettre_only = []
    for car in texte:
        if car in alphabet:
            texte_lettre_only.append(car)
    nouveau_texte = list(texte)
    j = 0
    alphabet_francais_texte = trouver_frequence_texte(texte_lettre_only)
    alphabet_francais.sort(reverse=True)
    for lettre in texte_lettre_only:
        a = False
        i = 0
        if nouveau_texte[j] == " " or nouveau_texte[j] == ":" or nouveau_texte[j] == "," or nouveau_texte[j] == "?" or nouveau_texte[j] == "." or nouveau_texte[j] == "2" or nouveau_texte[j] == "6":
            j += 1
        else:
            while a == False:
                if lettre == alphabet_francais_texte[i][1]:
                    nouveau_texte[j] = alphabet_francais[i][1]
                    a = True
                else:
                    i += 1
                    if i == 26:
                        i = 0
        j += 1
    texte_str = str_convert(nouveau_texte)
    return texte_str


# print(substituer(texte2))


def substituer_lettre(texte, lettre_initiale, lettre_finale):
    nouveau_texte = list(texte)
    i = 0
    for lettre in texte:
        if lettre == lettre_initiale:
            nouveau_texte[i] = lettre_finale
        i += 1
    nouveau_texte = str_convert(nouveau_texte)
    return nouveau_texte

# print(alphabet_francais)
# print(trouver_frequence_texte(texte2))
# print(texte2)

alphabet_decode = ['z', 'b', 'd', 'n', 'e', 'm', 'l', 'h', 's', 'j', 'i', 'h', 'g', 'a', 'r', 'p', 'p', 'r', 'o', 't', 't', 'c', 'f', 'e', 'u', 'y']
# Obtenu par essai et erreur (en testant la fonction substituer_lettre en boucle)

def decode_substitution(texte, alphabet):
    """Effectue une substitution par rapport à un alphabet donné."""
    nouveau_texte = []
    alphabet_francais = [[7.11, 'a'], [1.14, 'b'], [3.18, 'c'], [3.67, 'd'], [12.10, 'e'], [1.11, 'f'], [1.23, 'g'], [1.11, 'h'], [6.59, 'i'], [0.34, 'j'], [0.29, 'k'], [4.96, 'l'], [2.62, 'm'], [6.39, 'n'], [5.02, 'o'], [2.49, 'p'], [0.65, 'q'], [6.07, 'r'], [6.51, 's'], [5.92, 't'], [4.49, 'u'], [1.11, 'v'], [0.17, 'w'], [0.38, 'x'], [0.46, 'y'], [0.15, 'z']]
    for lettre in texte:
        a = False
        i = 0
        if lettre == " " or lettre == ":" or lettre == "," or lettre == "?" or lettre == "." or lettre == "2" or lettre == "6" or lettre == "'":
            nouveau_texte.append(lettre)
        else:
            while a == False:
                if lettre == alphabet_francais[i][1]:
                    nouveau_texte.append(alphabet[i])
                    a = True
                else:
                    i += 1
                    if i == 26:
                        i = 0
    texte_sub = str_convert(nouveau_texte)
    return texte_sub

texte2_decode = "le prochain fichier est code par un mot de passe de taille inconnu et contient l'indice. les lettres du mot de passe permettent de décaler les lettres du message original modulo 26. seules les lettres de a a z sont chiffrees."

# print(decode_substitution(texte2, alphabet_decode))

def position_lettre(lettre):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_liste = list(alphabet)
    for i in range(len(alphabet_liste)):
        if lettre == alphabet_liste[i]:
            return i


def decaler_les_lettres(texte, clef):
    liste_texte = list(texte)
    liste_clef = list(clef)
    a = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_liste = list(alphabet)
    for i in range(len(liste_texte)):
        if liste_texte[i] in alphabet:
            if position_lettre(liste_texte[i])+position_lettre(liste_clef[a]) < 0:
                liste_texte[i] = alphabet_liste[position_lettre(liste_texte[i])+position_lettre(liste_clef[a])]
            else:
                liste_texte[i] = alphabet_liste[position_lettre(liste_texte[i])-position_lettre(liste_clef[a])]
            a += 1
            if a == len(clef):
                a = 0
        elif liste_texte[i] == " ":
            a = 0
        else:
            a += 1
            if a == len(clef):
                a = 0
    return str_convert(liste_texte)


def decaler_les_lettres_sans_espace(texte, clef):
    liste_texte = list(texte)
    liste_clef = list(clef)
    a = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_liste = list(alphabet)
    for i in range(len(liste_texte)):
        if liste_texte[i] in alphabet:
            if position_lettre(liste_texte[i])+position_lettre(liste_clef[a]) < 0:
                liste_texte[i] = alphabet_liste[position_lettre(liste_texte[i])+position_lettre(liste_clef[a])]
            else:
                liste_texte[i] = alphabet_liste[position_lettre(liste_texte[i])-position_lettre(liste_clef[a])]
            a += 1
            if a == len(clef):
                a = 0
        elif liste_texte[i] == " ":
            pass
        else:
            a += 1
            if a == len(clef):
                a = 0
    return str_convert(liste_texte)


def decaler_les_lettres_en_bourrin(texte, clef):
    # Celui-là marche
    liste_texte = list(texte)
    liste_clef = list(clef)
    a = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_liste = list(alphabet)
    for i in range(len(liste_texte)):
        if liste_texte[i] in alphabet:
            if position_lettre(liste_texte[i])+position_lettre(liste_clef[a]) < 0:
                liste_texte[i] = alphabet_liste[position_lettre(liste_texte[i])+position_lettre(liste_clef[a])]
            else:
                liste_texte[i] = alphabet_liste[position_lettre(liste_texte[i])-position_lettre(liste_clef[a])]
        a += 1
        if a == len(clef):
            a = 0
    return str_convert(liste_texte)



def creer_clef_lettre(taille):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(taille):
        clef = [j for j in alphabet]
        for y in range(i):
            clef = [x + j for j in alphabet for x in clef]
    return clef


liste_des_clef = creer_clef_lettre(4)
#for j in range(len(liste_des_clef)):
#    coucou = decaler_les_lettres(texte3,liste_des_clef[j])
#    if "bravo a" in coucou:
#        print(coucou, liste_des_clef[j])

#for j in range(len(liste_des_clef)):
#    coucou = decaler_les_lettres_sans_espace(texte3,liste_des_clef[j])
#    if "bravo a" in coucou:
#        print(coucou, liste_des_clef[j])

for j in range(len(liste_des_clef)):
    coucou = decaler_les_lettres_en_bourrin(texte3,liste_des_clef[j])
    if "bravo a" in coucou:
        print(coucou, liste_des_clef[j])

# Pour "bravo a" j'avais essayé "grace a" au depart mais cela n'avait pas fonctionne, donc j'ai essaye "bravo a" et ca a marche

texte3_decode = "bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?"

racine.mainloop()
