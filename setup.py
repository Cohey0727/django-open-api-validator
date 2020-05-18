import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drf-open-api-validator",
    version="0.0.2",
    author="Kohei Okamoto",
    author_email="ohayousagi.ac.kook0727@gmail.com",
    description="drf-open-api-validator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cohey0727/drf_open_api_validator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)