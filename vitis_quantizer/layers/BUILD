load("@pip//:requirements.bzl", "requirement")

package(default_visibility = [
    "//vitis_quantizer:__subpackages__",
])

py_library(
    name = "vitis_activation",
    srcs = [
        "vitis_activation.py",
    ],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_conv_bn",
    srcs = ["vitis_conv_bn.py"],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/base:quantizer",
        "//vitis_quantizer/common:vitis_quantize_aware_activation",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_pooling",
    srcs = ["vitis_pooling.py"],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_quantize",
    srcs = ["vitis_quantize.py"],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/base:quantizer",
        "//vitis_quantizer/utils:common_utils",
    ],
)
