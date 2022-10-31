from setuptools import setup

setup(
    name='Holmes',
    version='0',
    packages=['jobs', 'objects', 'objects.relation', 'objects.data_objects', 'objects.data_objects.exceptions'],
    url='https://github.com/bramvanuldenn/Holmes',
    license='Apache',
    author='bramv',
    author_email='bram@whatson.nl',
    description='Small package for defining data and their relations within the Whatson workspace'
)
