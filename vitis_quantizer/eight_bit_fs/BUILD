load("@pip//:requirements.bzl", "requirement")

package(default_visibility = [
    "//vitis_quantizer:__subpackages__",
])

exports_files([
    "vitis_8bit_fs_quantize_strategy.json",
])

py_library(
    name = "vitis_8bit_fs_quantize_strategy",
    srcs = [
        "vitis_8bit_fs_quantize_strategy.py",
    ],
    data = [
        ":vitis_8bit_fs_quantize_strategy.json",
    ],
    deps = [
        requirement("tensorflow"),
        ":vitis_8bit_fs_transforms_pipeline",
        "//vitis_quantizer/common:vitis_quantize_registry",
        "//vitis_quantizer/common:vitis_quantize_strategy",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_8bit_fs_quantize_transforms",
    srcs = [
        "vitis_8bit_fs_quantize_transforms.py",
    ],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/common:vitis_quantize_aware_activation",
        "//vitis_quantizer/common:vitis_quantize_configs",
        "//vitis_quantizer/common:vitis_quantize_wrapper",
        "//vitis_quantizer/common:vitis_quantizers",
        "//vitis_quantizer/graph_transformations:transforms",
        "//vitis_quantizer/layers:vitis_activation",
        "//vitis_quantizer/layers:vitis_conv_bn",
        "//vitis_quantizer/layers:vitis_pooling",
        "//vitis_quantizer/layers:vitis_quantize",
        "//vitis_quantizer/optimizations:vitis_optimize_transforms",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_8bit_fs_transforms_pipeline",
    srcs = [
        "vitis_8bit_fs_transforms_pipeline.py",
    ],
    deps = [
        requirement("tensorflow"),
        ":vitis_8bit_fs_quantize_transforms",
        "//vitis_quantizer/graph_transformations:model_transformer",
        "//vitis_quantizer/graph_transformations:transforms_pipeline",
        "//vitis_quantizer/optimizations:vitis_equalization_transforms",
        "//vitis_quantizer/optimizations:vitis_optimize_transforms",
        "//vitis_quantizer/utils:common_utils",
        "//vitis_quantizer/utils:model_utils",
    ],
)
