#from distutils.core import setup
from setuptools import setup, find_packages, Extension
import os 
#from distutils.extension import Extension
from Cython.Distutils import build_ext

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'pyshoal', # Y
    version = '0.1.1', # Y
    #packages=['pyshoal', 'pyshoal.test'],
    packages = find_packages(),

    install_requires = [
        "numpy >= 1.5.1",
        "matplotlib >= 1.0.1",
    ],

    author = 'Will Furnass',
    author_email = 'will@thearete.co.uk',
    description='Particle Swarm Optimisation implementation.',
    license='GPL 3.0',
    keywords='particle swarm optimisation optimization',
    #url='http://pypi.python.org/pypi/PyShoal/',
    long_description=read('README.txt'),
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("pyshoal.similarity_metrics", ["pyshoal/similarity_metrics.pyx"])]
)
