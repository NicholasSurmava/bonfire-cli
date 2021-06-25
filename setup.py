from setuptools import setup, find_packages

setup(
    name='bonfire',
    version='0.1.0',
    author='Nicholas Surmava',
    author_email='nicholas.surmava@gmail.com',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'bonfire = cli:cli',
        ],
    },
)