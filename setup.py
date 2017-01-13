""" Module setup
"""


import os
import setuptools


NAME = 'business'

VERSION = '0.0.0'

REQUIRES = [
    'celery[redis]',
]

ENTRY_POINTS = """\
[paste.app_factory]
main = {}:main
""".format(NAME)


setuptools.setup(
    name=NAME,
    version=VERSION,
    packages=setuptools.find_packages(),
    install_requires=REQUIRES,
)


# EOF
