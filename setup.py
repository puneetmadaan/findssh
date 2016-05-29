#!/usr/bin/env python
from setuptools import setup
import subprocess

try:
    subprocess.run(['conda','install','--yes','--file','requirements.txt'])
except Exception as e:
    pass


with open('README.rst','r') as f:
    long_description = f.read()


setup(name='findssh',
      description='find servers with open ports without nmap',
	  long_description=long_description,
	  author='Michael Hirsch',
	  url='https://github.com/scienceopen/findssh',
      dependency_links = [],
	  install_requires = [],
	  )
