from setuptools import setup, find_packages

# find_packages is used to find the paths of your packages and subpackages

setup(

    author='Jose Servin',
    description='A complete package to count number of word occurrences in a txt file.',
    name='mysimplepackage',
    version='0.1.0',  # version number (major number).(minor number).(patch)
    packages=find_packages(include=['mysimplepackage', 'mysimplepackage.*']),
    install_requires=['numpy', 'pandas']
)
