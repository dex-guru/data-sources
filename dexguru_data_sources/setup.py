#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Vitaly Vakhteev",
    author_email='vitaly.v@techusage.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="The DexGuru Data Sources package allows the importation of JSONs for API use",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='dexguru_data_sources',
    name='dexguru_data_sources',
    packages=find_packages(include=['dexguru_data_sources', 'dexguru_data_sources.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dex-guru/data-sources',
    version='0.1.0',
    zip_safe=False,
)
