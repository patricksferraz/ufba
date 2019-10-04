import setuptools

from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="string_handling",
    version="1.0.dev2",
    author="Patrick Silva Ferraz",
    author_email="patrick.ferraz@outlook.com",
    description="Package python for string handling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patricksferraz/string_handling",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
