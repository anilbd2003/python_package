from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    description="A sample Python package with modules",
    author="tom thom",
    author_email="tom@email.com",
    url="https://github.com/yourusername/mypackage",
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
