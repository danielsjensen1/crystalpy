from periodic.crystal import Crystal


latticevecs = ((4.59373000,  0.00000000,  0.00000000),
               (0.00000000,  4.59373000,  0.00000000),
               (0.00000000,  0.00000000,  2.95812000))
basis = (('Ti',  (0.00000000,  0.00000000,  0.00000000)),
         ('Ti',  (2.29686500,  2.29686500,  1.47906000)),
         ('O',   (1.40246577,  1.40246577,  0.00000000)),
         ('O',   (-1.40246577, -1.40246577,  0.00000000)),
         ('O',   (3.69933077,  0.89439923,  1.47906000)),
         ('O',   (0.89439923,  3.69933077,  1.47906000)))


if __name__ == '__main__':
    TiO2 = Crystal(latticevecs, basis)
    rcutoff = 2e0
    atomlist = TiO2.tile_radially(rcutoff)
    filename = 'TiO2_rcut_{0:.2f}.xyz'.format(rcutoff)
    with open(filename, 'w') as f:
        f.write(str(len(atomlist))+'\n')
        f.write('crystal.py-generated xyz file'+'\n')
        for (symbol, position) in atomlist:
            f.write(symbol+'   '+str(position)[1:-1]+'\n')