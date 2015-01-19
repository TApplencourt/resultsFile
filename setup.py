#!/usr/bin/python
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



from distutils.core import setup

"""
- To create a source distribution, run:

python setup.py sdist

- To install the module, run:

python setup.py install

- To create an rpm distribution

python setup.py bdist_rpm
"""

import os
setup(name="resultsFile",
      version=os.getenv("VERSION","1.0"),
      author="Anthony Scemama",
      author_email="scemama@irsamc.ups-tlse.fr",
      license="gpl-license",
      description="Module for I/O on Quantum Chemistry files.",
      packages=["resultsFile","resultsFile.lib","resultsFile.Modules"]
      )

