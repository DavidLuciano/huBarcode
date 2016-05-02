#!/usr/bin/env python
"""Coverage and unittest for datamatrix and QR Code library"""

import sys
import unittest

import coverage # get it from http://www.nedbatchelder.com/code/modules/coverage.html

exitcode = 0

coverage.erase()
coverage.start()

import hubarcode.datamatrix.matrixtest
suite = unittest.TestLoader().loadTestsFromName('datamatrix.matrixtest.MatrixTest')
results = unittest.TextTestRunner().run(suite)
if not results.wasSuccessful():
    exitcode += 1


coverage.stop()
coverage.report(['datamatrix/__init__.py',
                 'datamatrix/placement.py',
                 'datamatrix/reedsolomon.py',
                 'datamatrix/textencoder.py',
                 ])

sys.exit(exitcode)
