import random

dict = {
  "as": 14,
  "valet": 11,
  "dame": 12,
  "roi" : 13
}

class Carte():
    '''Cette classe permet de créer des objets cartes'''
    def __init__(self,val,couleur,etat_choisi=0):
        ''' data : valeur de la carte, sa couleur, son état (déjà choisi dans un deck ou pas)'''
        self.__val=val
        self.__couleur=couleur
        self.__etat_choisi=etat_choisi
        
    def get_val_str(self):
        '''retourne la valeur sous forme de chaine caractère avec valet, dame roi as'''
        return str(self.__val)
        
    def get_val_int(self):
        '''retourne la valeur de la carte sous forme entière avec valet=10,...as=14'''
        if str(self.__val).isnumeric():
            return int(self.__val)
        else:
            return int(dict[self.__val])
        
    def get_couleur(self):
        ''' retourne la couleur de la carte'''
        return self.__couleur
        
    def get_etat_choisi(self):
        ''' retourne l'état de la carte (1: déjà choisi dans une pioche, 0:pas cencore choisi)'''
        return self.__etat_choisi
        
    def set_etat_choisi(self,etat_choisi):
        ''' modifie la valeur de l'etat choisit (1: déjà choisi dans une pioche, 0:pas cencore choisi)'''
        self.__etat_choisi=etat_choisi



class Jeu():
    '''Cette classe permet de créer et gérer l'ensembles des objets cartes du jeu'''
    def __init__(self):
        ''' data :la liste des cartes du jeu'''
        self.__liste_carte=[]
        
    def get_liste_carte(self):
        '''retourne la liste des cartes de jeu'''
        return self.__liste_carte
        
    def set_liste_carte(self):
        '''établir la liste des cartes de jeu'''
        for i in range(2,11):
            carte=Carte(i,"pique",0)
            self.__liste_carte.append(carte)
            carte=Carte(i,"trefle",0)
            self.__liste_carte.append(carte)
            carte=Carte(i,"carreau",0)
            self.__liste_carte.append(carte)
            carte=Carte(i,"coeur",0)
            self.__liste_carte.append(carte)
            
        for i in ["as","valet", "dame", "roi"]:
            carte=Carte(i,"pique",0)
            self.__liste_carte.append(carte)
            carte=Carte(i,"trefle",0)
            self.__liste_carte.append(carte)
            carte=Carte(i,"carreau",0)
            self.__liste_carte.append(carte)
            carte=Carte(i,"coeur",0)
            self.__liste_carte.append(carte)
    
    def get_une_carte_possible(self):
        '''retourne une carte au hasar de la liste des cartes de jeu'''
        i=random.randint(0, 51)
        return self.__liste_carte[i]


        
class Pioche():
    '''Cette classe permet de créer et gérer une pioche'''
    def __init__(self):
        ''' data : la liste des cartes de la pioche'''
        self.__pile=[]
        
    def set_pioche(self,pioche):
        '''modifie la liste des cartes qui composent la pioche'''
        self.__pile=pioche
        
    def initialiser_pioche(self,jeu):
        '''initialise au hasard la liste des cartes qui composent la pioche'''
        self.__pile=[]
        for i in range(0,26):
            c=jeu.get_une_carte_possible()
            while c.get_etat_choisi()==1:
                c=jeu.get_une_carte_possible()
            self.__pile.append(c)
            c.set_etat_choisi(1)
            
    def tirer_carte(self):
        '''retourne la carte en haut de la pioche, et la supprime de la pioche'''
        c=self.__pile[len(self.__pile)-1]
        self.__pile.pop(len(self.__pile)-1)
        return c
        
    def get_len(self):
        '''renvoie le nombre de carte restante dans la pioche'''
        return len(self.__pile)


class Defausse():
    '''Cette classe permet de créer et gérer une défausse'''
    def __init__(self):
        ''' data : la liste des cartes de la défausse'''
        self.__pile=[]
        
    def reset(self):
        '''vide la liste des cartes de la défausse'''
        self.__pile=[]
    	
    def add(self,c:Carte):
        '''ajoute la carte à la liste des cartes de la défausse'''
        self.__pile.append(c)  

    def get_len(self):
        '''renvoie le nombre de carte restante dans la défausse'''
        return len(self.__pile)
        
    def get_pile(self):
        '''retourne la liste des cartes de la défausse'''
        return self.__pile


    
class Joueur:
    '''Cette classe permet de créer et gérer des objets Joueur'''
    def __init__(self):
        ''' data : la pioche du joueur, sa défausse et la liste de ses cartes actuellement en jeu'''
        self.__pioche=Pioche()
        self.__defausse=Defausse()
        self.__carte_en_jeu=[]
        
    def initialiser_pioche(self,jeu):
        '''établit la pioche du joueur'''
        self.__pioche.initialiser_pioche(jeu)
        
    def tirer_carte(self):
        '''tire une carte de la pioche et la met en jeu'''
        self.__carte_en_jeu.append(self.__pioche.tirer_carte())
        
    def defausse_devient_pioche(self):
        '''transfère la defausse à la pioche, la mélange puis vide la défausse'''
        a=self.__defausse.get_pile().copy()
        random.shuffle(a)
        self.__pioche.set_pioche(a)
        self.__defausse.reset()
        
        
    def get_carte_en_jeu(self):
        '''retourne  la liste des cartes en jeu du joueur'''
        return self.__carte_en_jeu
        
    def reset_carte_en_jeu(self):
        '''vide la liste des cartes en jeu du joueur'''
        self.__carte_en_jeu=[]
        
    def ramasse(self,j2):
        '''ajoute à la défausse du joueur tout les cartes en jeu (les siennes et celles de celui passer en paramètre)'''
        c=self.get_carte_en_jeu()
        for i in range(0,len(c)):
            self.__defausse.add(c[i])
        self.reset_carte_en_jeu()
        
        c=j2.get_carte_en_jeu()        
        for i in range(0,len(c)):
            self.__defausse.add(c[i])
        j2.reset_carte_en_jeu()
        
    def get_len_pioche(self):
        '''retourne le nombre de carte dans la pioche du joueur'''
        return self.__pioche.get_len()
        
    def get_len_defausse(self):
        '''retourne le nombre de carte dans la défausse du joueur'''
        return self.__defausse.get_len()
        
    
if __name__ == "__main__":      
    print("START")

    j1=Joueur()
    j2=Joueur()

    jeu=Jeu()
    jeu.set_liste_carte()

    j1.initialiser_pioche(jeu)
    j2.initialiser_pioche(jeu)

    gagnant=False
    while(gagnant==False):

        if j1.get_len_pioche() == 0:
            j1.defausse_devient_pioche()
        if j2.get_len_pioche() == 0:
            j2.defausse_devient_pioche()
            
        j1.tirer_carte()
        j2.tirer_carte()

        c1=j1.get_carte_en_jeu()
        c2=j2.get_carte_en_jeu()

        print(f"{c1[len(c1)-1].get_val_str()} de {c1[len(c1)-1].get_couleur()} vs {c2[len(c2)-1].get_val_str()} de {c2[len(c2)-1].get_couleur()}")


        if c1[len(c1)-1].get_val_int() > c2[len(c2)-1].get_val_int():
            j1.ramasse(j2)
            print(f"-> Gagnant : j1 {j1.get_len_pioche()}/{j1.get_len_defausse()}")
           
        elif c1[len(c1)-1].get_val_int() < c2[len(c2)-1].get_val_int():
            j2.ramasse(j1)
            print(f"-> Gagnant : j2 {j2.get_len_pioche()}/{j2.get_len_defausse()}")
           
        elif c1[len(c1)-1].get_val_int() == c2[len(c2)-1].get_val_int():
            print("-> Bataille")
            if j1.get_len_pioche() == 0:
                j1.defausse_devient_pioche()
            if j2.get_len_pioche() == 0:
                j2.defausse_devient_pioche()
                
            j1.tirer_carte()
            j2.tirer_carte()
            
            if(j1.get_len_pioche() + j1.get_len_defausse() == 0):
                gagnant="j2"
                break
            if(j2.get_len_pioche() + j2.get_len_defausse() == 0):
                gagnant="j1"
                break

            c1=j1.get_carte_en_jeu()
            c2=j2.get_carte_en_jeu()

            print(f"[cartes cachée] {c1[len(c1)-1].get_val_str()} de {c1[len(c1)-1].get_couleur()} vs {c2[len(c2)-1].get_val_str()} de {c2[len(c2)-1].get_couleur()}")
            print("BATAILLE... : ")
                
           
        
        if(j1.get_len_pioche() + j1.get_len_defausse() == 0):
	        gagnant="j2"
        if(j2.get_len_pioche() + j2.get_len_defausse() == 0):
	        gagnant="j1"
	    
    print(f"---> Gagnant final : {gagnant}")


