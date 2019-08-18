import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="affnine_deltaleaf",
    version="0.2",
    author="Biswanath Saha",
    author_email="biswanathamz@gmail.com",
    description="Easy way to create MAP (Undirected Graph)and find shortest path from one Node to another.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/biswanathamz/affnine_deltaleaf",
    packages=['affnine_deltaleaf'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

