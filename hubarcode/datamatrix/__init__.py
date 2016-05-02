#!/usr/bin/env python

"""2D Datamatrix barcode encoder

All needed by the user is done via the DataMatrixEncoder class:

>>> encoder = DataMatrixEncoder("HuDoRa")
>>> # encoder.save( "test.png" )
>>> print encoder.get_ascii()
XX  XX  XX  XX  XX  XX  XX
XX  XXXX  XXXXXX      XXXXXX
XXXXXX    XX          XX
XXXXXX    XX        XXXX  XX
XXXX  XX  XXXXXX
XXXXXX    XXXXXXXX    XXXXXX
XX    XX  XXXXXXXX  XXXX
XX    XX      XXXX      XXXX
XX  XXXXXXXXXX    XXXX
XX  XXXX    XX            XX
XX  XXXXXX  XXXXXX      XX
XXXXXX  XX  XX  XX  XX    XX
XX    XX              XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXX


Implemented by Helen Taylor for HUDORA GmbH.

Detailed documentation on the format here:
http://grandzebu.net/informatique/codbar-en/datamatrix.htm
Further resources here: http://www.libdmtx.org/resources.php

You may use this under a BSD License.
"""

__revision__ = "$Rev$"

from textencoder import TextEncoder
from placement import DataMatrixPlacer


class DataMatrixEncoder:
    """Top-level class which handles the overall process of
    encoding input data, placing it in the matrix and
    outputting the result"""

    def __init__(self, text):
        """Set up the encoder with the input text.
        This will encode the text,
        and create a matrix with the resulting codewords"""

        enc = TextEncoder()
        codewords = enc.encode(text)
        self.width = 0
        self.height = 0
        matrix_size = enc.mtx_size

        self.matrix = [[None] * matrix_size for _ in range(0, matrix_size)]

        placer = DataMatrixPlacer()
        placer.place(codewords, self.matrix)


    def get_ascii(self):
        """Write an ascii version of the matrix out to screen"""

        def symbol(value):
            """return ascii representation of matrix value"""
            if value == 0:
                return '  '
            elif value == 1:
                return 'XX'

        return '\n'.join([''.join([symbol(cell) for cell in row]) for row in self.matrix]) + '\n'

    def put_cell(self, (posx, posy), colour=1):
        """Set the contents of the given cell"""

        self.matrix[posy][posx] = colour

    def add_border(self, colour=1, width=1):
        """Wrap the matrix in a border of given width
            and colour"""
        self.width += len(self.matrix) + (width * 2)
        self.height += len(self.matrix[0]) + (width * 2)

        self.matrix = \
            [[colour] * self.width] * width + \
            [[colour] * width + self.matrix[i] + [colour] * width
                for i in range(0, self.height - (width * 2))] + \
            [[colour] * self.width] * width

    def add_handles(self):
        """Set up the edge handles"""
        # bottom solid border
        for posx in range(0, self.width):
            self.put_cell((posx, self.height - 1))

        # left solid border
        for posy in range(0, self.height):
            self.put_cell((0, posy))

        # top broken border
        for i in range(0, self.width - 1, 2):
            self.put_cell((i, 0))

        # right broken border
        for i in range(self.height - 1, 0, -2):
            self.put_cell((self.width - 1, i))

#if __name__ == "__main__":
