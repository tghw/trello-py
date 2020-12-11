import setuptools

from textwrap import dedent

setuptools.setup(
    name='trello',
    version='0.9.5',
    packages=['trello'],
    license=dedent("""
        Redistribution and use in source and binary forms, with or without modification,
        are permitted provided that the following conditions are met:

        Redistributions of source code must retain the above copyright notice, this list
        of conditions and the following disclaimer.  Redistributions in binary form must
        reproduce the above copyright notice, this list of conditions and the following
        disclaimer in the documentation and/or other materials provided with the
        distribution.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
        ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
        WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
        ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
        (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
        LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
        ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    """),
    description='Python library for interacting with the Trello API',
    long_description=dedent("""
        Python Trello API Wrapper

        This Python API is simply a wrapper around the Trello API

        Getting Started:

        To use the Trello API, install the package either by downloading the source and running

            $ python setup.py install

        or by using pip

            $ pip install trello

        Documentation:

        You can find documentation for the Python API at:

            http://packages.python.org/trello/

        And documentation for the Trello API at:

            https://trello.com/docs/api/
    """),
    author='tghw,kulikjak,waghanza,lukegb',
    author_email='ty@tghw.com',
    url='https://github.com/tghw/trello-py',
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
    python_requires='>=3.6',
)
