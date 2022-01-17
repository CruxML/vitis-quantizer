# Vitis Quantizer

**THIS IS NOT AN OFFICIAL XILINX PACKAGE**

A pip installable package to do the vitis model quantization for tensorflow 2.

This is a migration of the code [here](https://github.com/Xilinx/Vitis-AI/tree/master/tools/Vitis-AI-Quantizer/vai_q_tensorflow2.x/tensorflow_model_optimization/python/core/quantization/keras/vitis)
to a standalone pip package that won't conflict with the `tensorflow-model-optimization` package.

Working in the docker image is annoying and this code should be standalone.

## Install

```
python3 setup.py bdist_wheel
pip install dist/vitis_quantizer-0.1.0-py3-none-any.whl
```

## Usage

TODO



