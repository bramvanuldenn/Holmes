from setuptools import setup, find_packages

REQUIRED = ['bson==0.5.10']
setup(
    name='Holmes',
    version='0',
    modules=find_packages(include=['Holmes']),
    url='https://github.com/bramvanuldenn/Holmes',
    license='Apache',
    author='bramv',
    author_email='bram@whatson.nl',
    description='Small package for defining data and their relations within the Whatson workspace'
)
