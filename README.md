# Compute GC content of DNA sequences


The python module ``gc_content.py`` is a command-line script that for
calculating GC content of DNA strings in fasta files. It should work
with python 2.7+ or 3.4+.   

It prints the id and percent GC for each record of a fasta file.

**Example:**
![Example screenshot](https://github.com/pdueck/Bioinf/blob/master/example_screenshot.jpg "Example")
Bioinf/example_screenshot.jpg
It assumes each id has one space, and replaces that with an underscore.

The script wraps biopython code. http://biopython.org/wiki/Biopython

## Install the python requirements

Requires biopython, plac.

    ``pip install -r requirements.txt``


## Simple usage as a command-line script

You can simply run the script ``gc_content.py`` from a unix command-line (e.g. linux or mac os). 
Try

    ``$ .../Bioinf/bioinf/gc_content.py -h``

where the ... is the path to its location.

The output is text, and can be written to a CSV file:

    ``$ ./gc_content.py input_file.fa > output_file.csv``
    
## Install for use in python code

To make the code available as python import, type

    ``$ cd .../Bioinf/``

    ``$ python setup.py install``

    ``$ python``

    From the python command prompt,

    ``>>> import Bioinf``

    ``>>> Bioinf.gc_content('poplar-primers.fa')``
    
