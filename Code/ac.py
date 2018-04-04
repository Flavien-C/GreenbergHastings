import numpy as np

class CA2D(object):
    def __init__(self,tail,nbEtats):
        self.nbEtats = nbEtats
        self.tail = tail
        self.rayon = 1        
        self.initAlea()

    def __repr__(self):
        res = ""
        for ligne in self.conf:
            for el in ligne:
                res += "%s  " %el
            res += "\n"
        return res 

    def initAlea(self):
        self.conf = np.zeros((self.tail,self.tail),dtype=int)

    def calculPred(self):
        r = self.rayon
        p = np.concatenate((self.conf[-r:,:],self.conf,self.conf[:r,:]))
        self.pred = np.concatenate((p[:,-r:],p,p[:,:r]),axis=1)
    
    def transition(self,lig,col):
        raise NotImplementedError
    
    def etape(self):
        self.calculPred()
        for lig in range(self.tail):
            for col in range(self.tail):
                self.transition(lig,col)


class GreenbergHastings(CA2D):
    def __init__(self,tail):
         CA2D.__init__(self,tail,3)
         self.seuil = 1

    def voisins(self,lig,col):
        """
        À DÉFINIR
        """
        return None

    def transition(self,lig,col):
        etatCour = self.conf[lig,col]
        voisins = self.voisins(lig,col)
        """
        À COMPLÉTER
        """
        
        

class CycleACGH(CA2D):
    def __init__(self,tail,nbEtats,rayon,seuil):
        pass



if '__main__'==__name__:
    pass
