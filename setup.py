import os
from setuptools import setup, find_packages

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mimic-fw",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "pyserial>=3.5",
        "click>=8.0.0",
    ],
    entry_points={
        'console_scripts': [
            'mimic=mimic.cli:main',
        ],
    },
    author="Antigravity",
    description="Cross-platform Python library for the Mimic STM32 Firmware",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Antigravity/Mimic",  # Update with your actual repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
