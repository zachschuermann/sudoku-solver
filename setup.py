import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sudoku-solver-schuermannator",
    version="0.0.1",
    author="Zach Schuermann",
    author_email="zachary.schuermann@gmail.com",
    description="A small sudoku solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schuermannator/sudoku-solver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    scripts=["sudoku-solver/sudoku.py"],
)
