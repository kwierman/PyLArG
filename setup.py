from setuptools import setup, find_packages
setup(
    name='PyLArG',
    version='0.1.0',
    description="Python GDML handling and VTK visualization for LArTPC Experiments",
    long_description="""Python GDML handling and VTK visualization for LArTPC Experiments""",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="VTK GDML Geometry",
    author="Kevin Wierman",
    author_email='kwierman@gmail.com',
    url="https://github.com/kwierman/PyLArG",
    license='BSD',
    #requires = [],
    packages=find_packages(exclude=[]),
    #ext_modules = cythonize("pyerman/*/*.pyx")
)
