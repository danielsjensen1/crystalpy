import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from periodic.crystal import Crystal


class DrawLattice(object):
    def __init__(self, crystal, size):
        '''if only the width is given then choose the height according to the golden ratio'''
        fig = plt.figure()
        #  fig.add_axes([left, bottom, width, height]) with values from 0 to 1
        self.ax = fig.add_axes([0.1, 0.1, .8, .8])
        left, right, top, bottom = size
        shell = chain( product(range(-2,2+1), (2,-2)), product((2,-2), range(-1,1+1)) )
        if abs(x) < right and abs(y) > top:
            pass
    
    def radial_cutoff(self, rcut):
        '''Create a circle centered at the origin.'''
        p1 = mpatches.Circle((0,0), rcut, fc='none', edgecolor='red',
                             linewidth=2, linestyle='solid')
        self.ax.add_patch(p1)
    
    def show_plot(self):
        self.ax.set_aspect(1e0)
        plt.show()
    
if __name__ == '__main__':
    oblique = Crystal(([1, 2], [1, -1]), (('Na', (0.5, .1))))
    oblique_plot = DrawLattice(oblique, (-2, 2, -1, 1))
    oblique_plot.radial_cutoff(.5)
    oblique_plot.show_plot()