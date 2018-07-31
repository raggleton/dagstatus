#!/usr/bin/env python

from distutils.core import setup
from glob import glob

setup(
    name='dagstatus',
    version='0.1',
    description="Turn HTCondor DAG status files into more useful summary output",
    author='Robin Aggleton',
    author_email='',
    url='https://github.com/raggleton/dagstatus',
    scripts=glob('bin/*'),
)