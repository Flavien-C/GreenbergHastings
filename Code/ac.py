import numpy as np

class CA2D(object):
    def __init__(self, tail, nbEtats):
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
        self.conf = np.random.randint(0, self.nbEtats, size=(self.tail,self.tail))


    def calculPred(self):
        r = self.rayon
        p = np.concatenate((self.conf[-r:,:],self.conf,self.conf[:r,:]))
        self.pred = np.concatenate((p[:,-r:],p,p[:,:r]), axis=1)
    
    def transition(self, lig, col):
        raise NotImplementedError
    
    def etape(self):
        self.calculPred()
        for lig in range(self.tail):
            for col in range(self.tail):
                self.transition(lig, col)


class GreenbergHastings(CA2D):
    def __init__(self, tail):
         CA2D.__init__(self, tail, 3)
         self.seuil = 1

    def voisins(self, lig, col):
        nord = self.pred[lig+1, col+1]
        sud = self.pred[lig+2, col+1]
        ouest = self.pred[lig+1, col]
        est = self.pred[lig+1, col+2]
        return np.array([nord, sud, ouest, est])

    def transition(self, lig, col):
        etatCour = self.conf[lig, col]
        voisins = self.voisins(lig, col)
        if etatCour == 1:
            self.conf[lig, col] = 2
        elif etatCour == 2:
            self.conf[lig, col] = 0
        else:
            if 1 in voisins:
                self.conf[lig, col] = 1
        

class CycleACGH(CA2D):
    def __init__(self, tail, nbEtats, rayon, seuil):
        CA2D.__init__(self, tail, nbEtats)
        self.seuil = seuil
        self.rayon = rayon
    
    def voisins(self, lig, col):
        return self.pred[lig:lig+2*self.rayon+1, col:col+2*self.rayon+1]
    
    def transition(self, lig, col):
        etatCour = self.conf[lig, col]
        voisins = self.voisins(lig, col)
        if etatCour != 0:
            self.conf[lig, col] = (self.conf[lig, col] + 1) % self.nbEtats
        else:
            if np.count_nonzero(voisins == 1) >= self.seuil:
                self.conf[lig, col] = 1
            
        



if '__main__'==__name__:
    #grh = GreenbergHastings(4)
    #print(grh)
    #grh.calculPred()
    #print(grh.pred)
    
    #print(grh.voisins(0,0))
    #grh.transition(0,0)
    #print(grh)
    #for step in range(5):
    #    grh.etape()
    #    print(grh)    
    
    acgh = CycleACGH(7, 8, 3, 5)
    print(acgh)
    acgh.calculPred()
    #print(acgh.voisins(0,0))
    #acgh.transition(0,0)
    #print(acgh)
    #first trans
    acgh.etape()
    print(acgh)