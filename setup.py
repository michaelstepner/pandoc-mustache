"""Pandoc filter for variable substitution using Mustache syntax

See:
https://github.com/michaelstepner/pandoc-mustache/
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except (IOError):
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

# Import version number
version = {}
with open("pandoc_mustache/version.py") as fp:
    exec(fp.read(), version)
version = version['__version__']

setup(
    name='pandoc-mustache',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='Pandoc filter for variable substitution using Mustache syntax',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/michaelstepner/pandoc-mustache/',

    # Author details
    author="Michael Stepner",
    author_email='stepner@mit.edu',

    # Choose your license
    license='CC0-1.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Text Processing :: Filters',
        'Operating System :: OS Independent',

        # Pick your license as you wish (should match "license" above)
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    # What does your project relate to?
    keywords='pandoc pandocfilters panflute markdown latex mustache',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["pandoc_mustache"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'panflute',
        'pystache',
        'pyyaml',
        'future'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['pandocfilters', 'configparser', 'pytest-cov', 'future'],
        'pypi': ['docutils']
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pandoc-mustache=pandoc_mustache.pandoc_mustache:main',
        ],
    },
)
