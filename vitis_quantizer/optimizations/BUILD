load("@pip//:requirements.bzl", "requirement")

package(default_visibility = [
    "//vitis_quantizer:__subpackages__",
])

py_library(
    name = "vitis_bias_correction",
    srcs = [
        "vitis_bias_correction.py",
    ],
    deps = [
        requirement("tensorflow"),
        requirement("numpy"),
        "//vitis_quantizer/common:vitis_quantize_wrapper",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_equalization_transforms",
    srcs = [
        "vitis_equalization_transforms.py",
    ],
    deps = [
        requirement("tensorflow"),
        requirement("numpy"),
        "//vitis_quantizer/graph_transformations:transforms",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_fast_finetune",
    srcs = [
        "vitis_fast_finetune.py",
    ],
    deps = [
        requirement("tensorflow"),
        requirement("numpy"),
        "//vitis_quantizer/common:vitis_quantize_aware_activation",
        "//vitis_quantizer/common:vitis_quantize_wrapper",
        "//vitis_quantizer/utils:common_utils",
        "//vitis_quantizer/utils:model_utils",
    ],
)

py_library(
    name = "vitis_optimize_transforms",
    srcs = [
        "vitis_optimize_transforms.py",
    ],
    deps = [
        requirement("tensorflow"),
        requirement("numpy"),
        "//vitis_quantizer/graph_transformations:transforms",
        "//vitis_quantizer/layers:vitis_conv_bn",
        "//vitis_quantizer/utils:common_utils",
    ],
)
