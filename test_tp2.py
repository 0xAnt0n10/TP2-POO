import unittest
from tp2 import Carte,Jeu,Pioche, Defausse, Joueur

class Test_Jeu(unittest.TestCase):
    def test_cartes(self):
        carte=Carte("as","pique",0)
        self.assertEqual(carte.get_val_int(),14)
        
    def test_jeu(self):
        jeu=Jeu()
        jeu.set_liste_carte()
        liste=jeu.get_liste_carte()
        derniere_carte=liste[51]
        self.assertEqual(derniere_carte.get_val_str(),"roi")
        self.assertEqual(derniere_carte.get_couleur(),"coeur")
        
    def test_pioche(self):
        jeu=Jeu()
        jeu.set_liste_carte()
        pioche=Pioche()
        pioche.initialiser_pioche(jeu)
        self.assertEqual(pioche.get_len(),26)


    def test_defausse(self):
        defausse=Defausse()
        carte=Carte("as","pique",0)
        defausse.add(carte)
        self.assertIsNotNone(defausse.get_pile())

    def test_joueur(self):
        joueur=Joueur()
        jeu=Jeu()
        jeu.set_liste_carte()
        joueur.initialiser_pioche(jeu)
        self.assertEqual(joueur.get_len_pioche(),26)
        
        
        joueur2=Joueur()
        joueur2.initialiser_pioche(jeu)
        self.assertEqual(joueur.get_carte_en_jeu(),[])
        joueur.tirer_carte()
        joueur2.tirer_carte()
        self.assertNotEqual(joueur.get_carte_en_jeu(),[])
        
        
        joueur.ramasse(joueur2)
        self.assertEqual(joueur.get_carte_en_jeu(),[])
        self.assertEqual(joueur2.get_carte_en_jeu(),[])
        self.assertEqual(joueur.get_len_defausse(),2)
        
        joueur.defausse_devient_pioche()
        self.assertEqual(joueur.get_len_defausse(),0)
        self.assertEqual(joueur.get_len_pioche(),2)
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()
