from setuptools import setup, find_packages

setup(
    name='Holmes',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/bramvanuldenn/Holmes',
    license='Apache',
    author='bramv',
    author_email='bram@whatson.nl',
    description='Lightweight module for data structure and relations within Whatson workspace'
)
