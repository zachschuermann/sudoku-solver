import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sudoku-solve",
    version="0.1.0",
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
    install_requires=["z3-solver",
                     ],
    entry_points={
        'console_scripts': [
            'sudoku-solve=sudoku_solve.sudoku:main',
        ],
    },
)
