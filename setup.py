from setuptools import setup
from setuptools_golang import GolangBuild, get_go_version

setup(
    name="my_package",
    version="0.1.0",
    description="Fibonacci function",
    author="Magnus Kvåle Helliesen",
    author_email="magnus.helliesen@gmail.com",
    url="https://github.com/magnushelliesen/go-python-integration",
    packages=["src"],  # Specify your package directory
    package_dir={"src": "."},
    include_package_data=True,  # Include all data files
    ext_modules=[
        GolangBuild(
            "src",
            go_mod="library.mod",  # Location of your Go module file
            build_tags=[],
        )
    ],
    cmdclass={
        "build_ext": GolangBuild,  # Use GolangBuild for extensions
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Go",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
