from setuptools import setup

setup(
   name='akaImageSearch',
   version='0.1.0',
   author='Jose A Cortes',
   author_email='cortesjoseandres@gmail.com',
   packages=['imsearch'],
   scripts=['bin/script1'],
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='Reverse image search engine with hot swappable backend models',
   long_description=open('README.txt').read(),
   install_requires=[
       "Django >= 1.1.1",
       "pytest",
   ],
)