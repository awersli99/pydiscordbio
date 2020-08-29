from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
import os


use_system_lib = True
if os.environ.get("BUILD_LIB") == "1":
    use_system_lib = False


base_dir = os.path.dirname(__file__)

__author__ = "awersli99 (Adam Worsley)"
__email__ = "adam@aworsley.me"

__title__ = "pydiscordbio"
__version__ = "1.1.1"
__summary__ = "An unoffical asynchronous wrapper for the discord.bio API."
__uri__ = "https://github.com/awersli99/pydiscordbio"

__requirements__ = [
    'aiohttp>=3.6.2',
    'python-dateutil>=2.8.0'
]

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    author=__author__,
    author_email=__email__,
    url=__uri__,
    zip_safe=False,
    install_requires=__requirements__,
    data_files=[
        ('', ['README.md']),
    ],
)