import pathlib
from setuptools import find_packages, setup

# reading the README file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='parflow',
    version="1.0.1",
    description='A package to run ParFlow via a Python interface.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/grapp1/kw-intern/tree/master/parflow-integration',
    author='Kitware, Inc.',
    license='###',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=['parflow','parflow.tools','parflow.tools.database'],
    package_dir={'':'pftools/python'},
    install_requires=[
        'pyyaml',
        'sphinx_rtd_theme'
    ]
)
