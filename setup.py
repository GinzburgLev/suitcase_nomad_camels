from os import path
from setuptools import setup
import sys
import versioneer


# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (3, 6)
if sys.version_info < min_version:
    error = """
event-model does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(
        *(sys.version_info[:2] + min_version)
    )
    sys.exit(error)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open(path.join(here, "requirements.txt")) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [
        line
        for line in requirements_file.read().splitlines()
        if not line.startswith("#")
    ]


setup(
    name="suitcase-nomad-camels-hdf5",
    version="0.6.3",
    # cmdclass=versioneer.get_cmdclass(),
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["suitcase.nomad_camels_hdf5", "suitcase.nomad_camels_hdf5.tests"],
    entry_points={
        "console_scripts": [
            # 'some.module:some_function',
        ],
    },
    include_package_data=True,
    python_requires=">={}".format(".".join(str(n) for n in min_version)),
    package_data={
        "suitcase.nomad_camels_hdf5": [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file',
        ]
    },
    install_requires=requirements,
    license="BSD (3-clause)",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
)
