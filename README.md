# PyLArG

Python GDML handling and VTK visualization for LArTPC Experiments
-----------------------------------------------------------------

## Installation

Download the source code with:

~~~ bash
git clone https://github.com/kwierman/PyLArG
~~~

### Requirements

* VTK>7.0
    * Please reference the documentation at [the official website](http://www.vtk.org/Wiki/VTK/Configure_and_Build) for installation instructions
    * Make sure that vtk is compiled with "PYTHON_WRAPPER" enabled
    * Make sure that vtk is accessible from Python by testing `python -m vtk`
* Python-level requirements
    * The user requirements can be installed with `pip install -r requirements.txt`
    * The developer requirements can be installed with `pip install -r requirements-dev.txt`

### Setup

If you downloaded the source, you can issue:

~~~ bash
python setup.py install
~~~

If you skipped this step, you can install with:

~~~ bash
pip install git+https://github.com/kwierman/PyLArG
~~~


## Usage

### Creating the GDML

This can be done by issuing the following command in the base directory



## Known Issues

## TODOs

* Break out the geometry
