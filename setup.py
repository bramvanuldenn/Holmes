from setuptools import setup

setup(
    name='Holmes',
    version='0.1',
    packages=['Holmes', 'Holmes.jobs', 'Holmes.objects', 'Holmes.objects.relation', 'Holmes.data_objects',
              'Holmes.data_objects.exceptions'],
    url='https://github.com/bramvanuldenn/Holmes',
    license='Apache',
    author='bramv',
    author_email='bram@whatson.nl',
    description='Data and relationship defining for Whatson'
)
