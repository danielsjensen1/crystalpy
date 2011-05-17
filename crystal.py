from itertools import product as iterproduct
from numpy import arange, array, dot
from numpy.linalg import norm
#  Crystalpy = neat logo, matplotlib (2d)

class Crystal(object):
    '''
    Multidimensional crystal class.
    
    Input
    -----
    latticevecs : list or tuple of 1d numpy arrays
    '''
    def __init__(self, latticevecs, basis):
        self.latticevecs = array(latticevecs)
        #  Assert that lattice vectors are linearly independent
        self.basis = basis
        #  Assert that all of the basis vectors lie in the unit cell
        
        
    def cell_n(self, n):
        latticevec = dot(self.latticevecs, n)
        
        cell = []
        for atom, vector in self.basis:
            map(cell.append, (atom, vector+latticevec))
        return cell
    
    def tile_radially(self, rcutoff):
        radial = []
        icut = 10
        for n in iterproduct(arange(-icut, icut+1), repeat=len(self.latticevecs)):
            latticevec = dot(self.latticevecs, n)
            for atom, vector in self.basis:
                rvec = vector + latticevec
                r = norm(rvec)
#                print r
                if r < rcutoff:
                    radial.append((atom, rvec))
        return radial