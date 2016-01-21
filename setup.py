from os.path import join, dirname

from setuptools import setup, find_packages

import testmd

setup(
        name="testmd",
        # в __init__ пакета
        version=testmd.__version__,
        packages=find_packages(exclude=["*.exemple", "*.exemple.*", "exemple.*", "exemple"]),
        include_package_data=True,
        long_description=open(
            join(dirname(__file__), 'README.rst')).read(),
        install_requires=['pyyaml==3.11'],
        entry_points={
            'console_scripts':
                ['testmd = testmd.run:main']
        }

)
