# TODO: not sure where to take this at the moment.

import setuptools

from textwrap import dedent

setuptools.setup(
    name='trello',
    version='0.9.7.3', # <-change this????
    packages=['trello'],
    license='3-Clause BSD License (https://opensource.org/licenses/BSD-3-Clause)', # <-change this????
    description='Python library for interacting with the Trello API',
    long_description_content_type='text/markdown',
    long_description="""Python Trello API Wrapper
=========================

This library is a Python wrapper around the [Trello](https://trello.com/) REST API.

Requires Python 3.6 or later.

Getting Started
---------------

Once you have set the user's token, all calls to the API will include that token, as if the user was logged in.""",
    author='',
    author_email='',
    url='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    install_requires = [
        "requests",
    ],
    python_requires='>=3.8',
)
