#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from setuptools import setup, find_packages

# -- versioning ---------------------------------------------------------------
import versioneer
__version__ = versioneer.get_version()

# -- dependencies -------------------------------------------------------------
setup_requires = [
    'setuptools',
    'pytest-runner',
]

install_requires = [
    'gwpy',           # for Q-transform, LIGO/GW data processing
    'scipy',          # for signal processing
    'scikit-image',   # for image processing
    'matplotlib',     # for plotting
    'numpy',          # general array manipulation
]

# -- tests ----------------------------------------------------------
tests_require = [
    'pytest',
]

# -- run setup ----------------------------------------------------------------
setup(
    name='gravityspy',
    version=__version__,
    description='GravitySpy: A minimal package for plotting and utils',
    author='Gravity Spy Team',
    author_email='contact@gravityspy.org',
    packages=find_packages(),  # finds the gravityspy module itself
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Science/Research',
    ],
)
