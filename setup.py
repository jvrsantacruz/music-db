# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.dirname(os.path.realpath(__file__))
readme = os.path.join(here, 'README.rst')

setup(
    name='music-db',
    version='0.5',
    description='Banshee-Clementine playcount database importer/exporter',
    long_description=open(readme).read(),
    author='Javier Santacruz',
    author_email='javier.santacruz.lc@gmail.com',
    url='http://github.com/jvrsantacruz/playlists',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
    ],
    platforms=['Any'],
    scripts=['banshee-clementine.py']
)
