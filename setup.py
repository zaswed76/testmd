
from setuptools import setup, find_packages
from os.path import join, dirname
import testmd

setup(
    name = "testmd",
    version=testmd.__version__,
    packages = find_packages(),
    include_package_data = True,
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=['pyyaml==3.11'],
    entry_points={
        'console_scripts':
            ['testmd = testmd.run:main']
        }

    )