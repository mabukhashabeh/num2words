"""
Setup script for num2words package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="num2words",
    version="0.1.0",
    author="Mohammad Abu Khahsabeh",
    author_email="abukhashabehmohammad@gmail.com",
    description="A lightweight, performant number-to-words converter supporting English and Arabic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mabukhashabeh/num2words",
    packages=find_packages(),
    package_data={
        'num2words': ['data/*.json'],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    keywords="number words converter english arabic num2words text",
    zip_safe=True,
)

