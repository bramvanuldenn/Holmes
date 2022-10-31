from setuptools import setup

setup(
    name='Holmes',
    version='0.1',
    packages=['src', 'src.jobs', 'src.objects', 'src.objects.relation', 'src.objects.data_objects',
              'src.objects.data_objects.exceptions'],
    url='https://github.com/bramvanuldenn/Holmes',
    license='Apache',
    author='bramv',
    author_email='bram@whatson.nl',
    description='Lightweight module for data structure and relations within Whatson workspace'
)
