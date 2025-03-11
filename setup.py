from setuptools import setup, find_packages

setup(
    name="simple-calc",
    version="0.1.0",
    description="A simple command-line calculator",
    author="Your Name",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calc=cli:main',
        ],
    },
)