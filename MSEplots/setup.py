import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MSEplots_pkg",
    version="1.0.14",
    author="Wei-Ming Tsai",
    author_email="wxt108@rsmas.miami.edu",
    description="A package for static energy analysis and relevant plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weiming9115/Working-Space/tree/master/MSEplots",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['metpy']
)
