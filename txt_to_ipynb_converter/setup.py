from setuptools import setup, find_packages

setup(
    name='txt_to_ipynb_converter',
    version='0.1',
    packages=find_packages(),
    description='A simple utility to convert TXT files to IPython Notebooks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='tjh70@cam.ac.uk',
    url='https://github.com/comparativechrono/txt_to_ipynb_converter',
    install_requires=[
        'nbformat',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
