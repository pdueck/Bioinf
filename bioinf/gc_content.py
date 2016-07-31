#!/usr/bin/env python

# For python 2/3 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from Bio import SeqIO
from Bio.SeqUtils import GC
import plac

"""
Prints id, GC% from the records of a SeqIO.parse (a SeqRecord object).
Assumes each id has one space, and replaces that with an underscore.
"""

def gc_content(file_):
    """Prints id, GC% from the records of a SeqIO.parse (a SeqRecord object).
       Assumes each id has one space, and replaces that with an underscore.
    """
    
    try:
        f = open(file_, 'Ur')
    except IOError:
        print(('cannot open file', file_))
        sys.exit(1)

    seq_record = SeqIO.parse(f, "fasta")

    # Fix space in name and compute GC
    for record in seq_record:

        # For each record id, correct the space with an underscore.
        record.id = record.id + '_' + str(record.description.split()[1])

        # Fraction of G and C is easy to compute,
        # but Bio.SeqUtils.GC() also handles ambiguous cases.
        gc_percent = GC(record.seq)

        # Print new id and GC percent, formatted for CSV.
        print(("%s %f" % (record.id + ',', gc_percent)))


@plac.annotations(
    filename = ("input file", 'positional', None, str))

def main(filename):

    """Prints id and percent GC for records of a fasta file.

    Assumes each id has one space, and replaces that with an underscore.
    The output is text, formatted as CSV.

    Example input:
    --------------
    >poplar 1 fwd primer for X
    GGACAGCTTATGCAGACCGGGAATGACGTGGGAGTCACATCTGTTAACCCTAA
    >poplar 2 rev primer for X
    CTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCTAAACCCT
    ...

    Output:
    --------------
    poplar_1, 50.943396
    poplar_2, 43.181818
    poplar_3, 46.268657
    ...

    To save output to file:

        $ python gc_content.py input_file.fa > output_file.csv
    or
        $ ./gc_content.py input_file.fa > output_file.csv
    
    """
    
    return gc_content(filename)


if __name__ == "__main__":
    plac.call(main)
