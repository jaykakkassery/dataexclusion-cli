from setuptools import setup
setup(
    name = 'dataexclusion-cli',
    version = '0.1.0',
    packages = ['dataexclusion'],
    entry_points = {
        'console_scripts': [
            'dataexclusion = dataexclusion.__main__:main'
        ]
    })