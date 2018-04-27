import matplotlib.pyplot as plt
from matplotlib import animation
from ac import *

class Visu(object):
    def __init__(self,tail=(40,40)):
        self.fig = plt.figure(figsize=tail)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_axis_off()

    def affiche(self,conf):
        self.ax.imshow(conf)
        plt.draw()


class Appli(Visu):
    def __init__(self,ac):
        Visu.__init__(self,tail=(40,40))
        self.ac = ac
        self.enCours = True
        self.ani = animation.FuncAnimation(self.fig, self.miseAjour, interval=500)
        self.im = self.ax.imshow(ac.conf)
        self.fig.canvas.mpl_connect('key_press_event', self.onPress)
        plt.show()

    def miseAjour(self,*args):
        self.ac.etape()
        self.im.set_data(self.ac.conf)

    def onPress(self,event):
        if event.key.isspace():
            if self.enCours:
                self.ani.event_source.stop()
            else:
                self.ani.event_source.start()
            self.enCours = not self.enCours



if '__main__'==__name__:
    #ac = GreenbergHastings(80)
    #Appli(ac)

    # taille, etat, rayon, seuil
    # Obligatoire: 80, 8, 3, 5
    # "Vide": 80, 10, 4, 8
    # "Multi-cellule": 500, 8, 4, 8
    ag = CycleACGH(500, 8, 4, 8)
    Appli(ag)
