from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "A standalone package to do the vitis quantization step."

REQUIRED_PACKAGES = [
    "tensorflow>=2.7.0",
    "numpy>=1.22.1",
    "tensorflow-model-optimization>=0.7.0",
]


setup(
    name="vitis-quantizer",
    version=VERSION,
    description=DESCRIPTION,
    url="https://github.com/CruxML/vitis-quantizer",
    author="CruxML",
    author_email="stephen.tridgell@cruxml.com",
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(exclude=["*_test.py"]),
    license="Apache 2.0",
    include_package_data=True,
    keywords="vitis quantize machine learning xilinx",
)
