#!/usr/bin/env python
#   resultsFile is a library which allows to read output files of quantum 
#   chemistry codes and write input files.
#   Copyright (C) 2007 Anthony SCEMAMA 
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#   Anthony Scemama
#   LCPQ - IRSAMC        
#   Universite Paul Sabatier
#   118, route de Narbonne      
#   31062 Toulouse Cedex 4      
#   scemama@irsamc.ups-tlse.fr 



from library import * 
from math import *

class atom(object):
   """Class for an atom."""

   def __init__(self):
       self._name = None
       self._charge = None
       self._coord = None
       self._basis = None
       
   def __repr__(self):
       out = "%8s %10.3f  %10.6f %10.6f %10.6f"%tuple(\
            [self.name, self.charge]+list(self.coord))
       return out

   def __repr__debug__(self):
       out = ""
       out += "Atom:\n"
       out += " Name        : "+str(self.name)+'\n'
       out += " Charge      : "+str(self.charge)+'\n'
       out += " Coord       : "+str(self.coord)+'\n'
       out += " Basis set   : "+str(self.basis)+'\n'
       return out

   def __cmp__(self,other):
       assert ( isinstance(other,atom) )
       if self.charge < other.charge:
          return -1
       elif self.charge > other.charge:
          return 1
       elif self.charge == other.charge:
          return 0

   for i in "name charge coord basis".split():
     exec """
def get_%(i)s(self): return self._%(i)s
def set_%(i)s(self,value): self._%(i)s = value
%(i)s = property(fget=get_%(i)s,fset=set_%(i)s) """%locals()


class atomDataElement(object):
   """Atomic database."""

   def __init__(self,symbol,charge,covalR,vdwR,valence,color,mass):
           self.symbol = symbol
           self.charge = int(charge)
           self.covalR = float(covalR)
           self.vdwR   = float(vdwR)
           self.mass   = float(mass)
           self.valence= int(valence)
           self.color  = int(color)

   def __repr__(self):
           out = ""
           out += "%3d  "%(self.charge)
           out += "%3s  "%(self.symbol)
           out += "%10.6f  "%(self.covalR)
           out += "%10.6f  "%(self.vdwR)
           out += "%3d  "%(self.valence)
           out += "%3d  "%(self.color)
           out += "%10.6f  "%(self.mass)
           return out

atomDataText = """
   0  X    0.0      0.75      0  8    0.0
   0  XX   0.0      0.75      0  8    0.0
   1  H    0.370000 1.200000  1  0    1.0079
   2  He	  0.700000 1.700000  0  2    4.00260
   3  Li	  1.230000 1.700000  1  5    6.941
   4  Be	  0.890000 1.700000  2  5    9.01218
   5  B 	  0.900000 1.700000  3  5   10.81
   6  C    0.850000 1.700000  4  8   12.011
   7  N    0.740000 1.550000  3  3   14.0067
   8  O    0.740000 1.520000  2  1   15.9994
   9  F    0.720000 1.470000  1  7   18.998403
  10  Ne	  0.700000 1.700000  0  1   20.179
  11  Na	  1.000000 1.700000  1  6   22.98977
  12  Mg	  1.360000 1.700000  2  6   24.305
  13  Al   1.250000 1.940000  3  6   26.98154
  14  Si   1.170000 2.100000  4  5   28.0855
  15  P    1.100000 1.800000  3  6   30.97376
  16  S    1.100000 1.800000  6  4   32.06
  17  Cl   0.990000 1.750000  1  6   35.453
  18  Ar	  0.700000 1.700000  0  5   39.948
  19  K 	  2.030000 1.700000  1  5   39.0983
  20  Ca	  1.740000 1.700000  2  5   40.08
  21  Sc	  1.440000 1.700000  0  5   44.9559
  22  Ti	  1.320000 1.700000  0  5   47.90
  23  V    1.220000 1.980000  0  5   50.9415
  24  Cr   0.000000 1.940000  0  5   51.996
  25  Mn   1.160000 1.930000  0  5   54.9380
  26  Fe   0.000000 1.930000  0  5   55.9332
  27  Co   1.150000 1.920000  0  5   58.9332
  28  Ni	  1.170000 1.700000  0  5   58.70
  29  Cu	  1.250000 1.700000  0  5   63.546
  30  Zn	  1.250000 1.700000  0  5   65.38
  31  Ga	  1.200000 2.020000  0  0   69.72
  32  Ge	  1.210000 1.700000  0  5   72.59
  33  As	  1.160000 1.960000  0  1   74.9216
  34  Se	  0.700000 1.700000  0  5   78.96
  35  Br	  1.240000 2.100000  0  6   79.904
  36  Kr	  1.910000 1.700000  0  5   83.80
  37  Rb	  1.620000 1.700000  0  5   85.4678
  38  Sr	  1.450000 1.700000  0  5   87.62
  39  Y 	  1.340000 1.700000  0  5   88.9059
  40  Zr	  1.290000 2.210000  0  5   91.22
  41  Nb	  1.290000 1.700000  0  5   92.9064
  42  Mo   1.240000 2.060000  0  5   95.94
  43  Tc	  1.250000 1.700000  0  5   98
  44  Ru   0.000000 2.010000  0  5  101.07
  45  Rh   1.340000 2.010000  0  5  102.9055
  46  Pd   1.410000 2.040000  0  5  106.4 
  47  Ag   1.500000 1.700000  0  5  107.868
  48  Cd	  1.400000 1.700000  0  5  112.41
  49  In	  1.410000 1.700000  0  5  114.82
  50  Sn	  1.370000 1.700000  0  5  118.69
  51  Sb	  1.330000 1.700000  0  5  121.75
  52  Te	  0.700000 1.700000  0  5  127.60
  53  I 	  1.330000 2.150000  1  6  126.9045
  54  Xe	  1.980000 1.700000  0  5  131.30
  55  Cs	  1.690000 1.700000  0  5  132.9054
  56  Ba	  1.690000 1.700000  0  5  137.33
  57  La	  0.000000 0.800000  0  5  138.9055
  58  Ce	  1.690000 1.700000  0  5  140.12
  59  Pr	  1.690000 1.700000  0  5  140.9077
  60  Nd	  1.690000 1.700000  0  5  144.24
  61  Pm	  1.690000 1.700000  0  5  145
  62  Sm	  1.690000 1.700000  0  5  150.4
  63  Eu	  1.690000 1.700000  0  5  151.96
  64  Gd	  1.690000 1.700000  0  5  157.25
  65  Tb	  1.690000 1.700000  0  5  158.9254
  66  Dy	  1.690000 1.700000  0  5  162.50
  67  Ho	  1.690000 1.700000  0  5  164.9304
  68  Er	  1.690000 1.700000  0  5  167.26
  69  Tm	  1.690000 1.700000  0  5  168.9342
  70  Yb	  1.690000 1.700000  0  5  173.04
  71  Lu	  1.690000 1.700000  0  5  174.967
  72  Hf	  1.440000 1.700000  0  5  178.49
  73  Ta	  1.340000 1.700000  0  5  180.9479
  74  W 	  1.300000 1.700000  0  5  183.85
  75  Re	  1.280000 1.700000  0  5  186.207
  76  Os	  1.260000 2.020000  0  5  190.2
  77  Ir	  1.290000 2.030000  0  5  192.22
  78  Pt	  1.340000 1.700000  0  5  195.09
  79  Au	  1.440000 1.700000  0  9  196.9665
  80  Hg	  1.550000 1.700000  0  5  200.59
  81  Tl	  1.540000 1.700000  0  5  204.37
  82  Pb	  1.520000 1.700000  0  5  207.2
  83  Bi	  1.520000 1.700000  0  5  208.9804
  84  Po	  1.400000 1.700000  0  5  209
  85  At	  0.700000 1.700000  0  5  210
  86  Rn	  2.400000 1.700000  0  5  222
  87  Fr	  2.000000 1.700000  0  5  223
  88  Ra	  1.900000 1.700000  0  5  226.0254
  89  Ac	  1.900000 1.700000  0  5  227.0278
  90  Th	  1.900000 1.700000  0  5  232.0381
  91  Pa	  1.900000 1.700000  0  5  231.0359
  92  U 	  1.900000 1.700000  0  5  238.029
  93  Np   2.0      2.0       0  5  237.0482
  94  Pu   2.0      2.0       0  5  244
  95  Am   2.0      2.0       0  5  243
  96  Cm   2.0      2.0       0  5  247
  97  Bk   2.0      2.0       0  5  247
  98  Cf   2.0      2.0       0  5  251
  99  Es   2.0      2.0       0  5  254
 100  Fm   2.0      2.0       0  5  257
 101  Md   2.0      2.0       0  5  258
 102  No   2.0      2.0       0  5  259
 103  Lr   2.0      2.0       0  5  260
"""

atomData = 110*[None]

for line in atomDataText.splitlines():
    try:
      charge, symbol, covalR, vdwR, valence, color, mass = line.split()
      at = atomDataElement(symbol,charge,covalR,vdwR,valence,color,mass)
      atomData[int(at.charge)] = at
    except:
      pass



if __name__ == '__main__':
        for s in atomData:
                print s

