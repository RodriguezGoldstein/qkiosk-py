from setuptools import setup, find_packages

setup(
    name="qkiosk",
    version="0.1.0",
    description="Python client for QUANTkiosk API",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
    ],
    author="QUANTkiosk",
    url="https://github.com/quantkiosk/qkiosk-r",
)
