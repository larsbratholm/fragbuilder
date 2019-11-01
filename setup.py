import sys
from numpy.distutils.core import Extension, setup

def requirements():
    with open('requirements.txt') as f:
        return [line.rstrip() for line in f]

# use README.md as long description
def readme():
    with open('README.rst') as f:
        return f.read()

def setup_fragbuilder():

    setup(

        name="fragbuilder",
        packages=[
            'fragbuilder',
            'fragbuilder.basilisk_lib',
            'fragbuilder.basilisk_lib.Mocapy',
            'fragbuilder.residues',
            'fragbuilder.bio_pdb',
            'fragbuilder.bio_pdb.Alphabet',
            ],

        install_requires = requirements(),

        # set up package contents

        ext_package = 'fragbuilder',
)

if __name__ == '__main__':

    setup_fragbuilder()
