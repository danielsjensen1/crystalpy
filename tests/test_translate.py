from itertools import izip_longest
from numpy import array
from numpy.testing import assert_array_almost_equal
import unittest

from periodic.crystal import Crystal


class TestNaCl(unittest.TestCase):
    #  Test data is from the Navy's Crystal Lattie Structures website:
    #  http://cst-www.nrl.navy.mil/lattice/struk.xmol/b1.pos
    #  All distances are written in Angstroms.
    latticevecs = ([0.00000000, 2.81500000, 2.81500000],
                   [2.81500000, 0.00000000, 2.81500000],
                   [2.81500000, 2.81500000, 0.00000000])
    basis = (('Na', array([0.00000000, 0.00000000, 0.00000000])),
             ('Cl', array([2.81500000, 2.81500000, 2.81500000])))

    #          (n1,n2,n3, [Symbol, position, Symbol, position, etc.])
    images = ( (1, 0, 0, ['Na', array([ 0.   , 2.815, 2.815]),
                          'Cl', array([ 2.815, 5.63 , 5.63 ])]),
               (0, 1, 0, ['Na', array([ 2.815, 0.   , 2.815]),
                          'Cl', array([ 5.63 , 2.815, 5.63 ])]),
               (0, 0, 1, ['Na', array([ 2.815, 2.815, 0.   ]),
                          'Cl', array([ 5.63 , 5.63 , 2.815])]),
               (-2, 3, -1, ['Na', array([ 5.63 , -8.445, 2.815]),
                            'Cl', array([ 8.445, -5.63 , 5.63 ])]) )

    def setUp(self):
        self.crystal = Crystal(self.latticevecs, self.basis)

    def test_images(self):
        for (n1, n2, n3, solution) in self.images:
            computed = self.crystal.cell_n((n1, n2, n3))
            print computed[1::2], solution[1::2]
            self.assertEqual(computed[0::2], solution[0::2])
            assert_array_almost_equal(computed[1::2], solution[1::2], decimal=15)
            
#            print computed
#            print basis
#            for sol, com in izip_longest(solution, computed):
#                pass
#            assert_array_equal(basis, computed)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReplicate']
    unittest.main()