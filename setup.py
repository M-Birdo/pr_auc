#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages
from codecs import open
from os import path

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='pr_auc',
    version='0.1',
    description='Calculates the Area Under the Curve for Precision-Recall curves via non-linear interpolation',
    long_description=read_md('README.md'),
    url='https://github.com/weberkry/pr_auc',
    author='Christiane Weber',
    author_email='christiane.weber@web.de',
    keywords='classifier evaluation precision recall auc',
    packages=['pr_auc'],
    install_requires=['numpy','matplotlib.pyplot','pandas','scipy','sklearn','math'],
)

