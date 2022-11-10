from Crypto.PublicKey import RSA
from batch_gcd import batch_gcd
import random

#Creation du'une liste qui va contenir nos clés
Key_List=[]

#creation d'une liste qui contiendra les differente type de clé qu'on génerera
bit=[1024,2048]

#Boucle qui permet de generer les clés
for i in range(1 , 100000 ) :
    N=random.choice(bit) #ici on affecte a N un nombre aleatoire choisi parmi la liste defini plus haut

    Cle= RSA.generate(N)
    Key_List.append(Cle.n)

#On remplit le fichier en y ajoutant nos clés générées
f=open('Key_generated.txt','w')
for x in range(1,len(Key_List)):
            f.write("\n"+str(Key_List[x]))
f.close()

#Detection des doublons
visited = set()
Doublons = [x for x in Key_List if x in visited or (visited.add(x) or False)]

print("Nous remarquons qu'on a --->" +str(len(Doublons))+" <----doublons")

batch_gcd(*Key_List) #application du batch-gcd()

print("----------->  le batch-gcd a ete effectué <-------------")

