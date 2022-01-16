load("@pip//:requirements.bzl", "requirement")

package(default_visibility = [
    "//vitis_quantizer:__subpackages__",
])

py_library(
    name = "common_utils",
    srcs = ["common_utils.py"],
)

py_library(
    name = "model_utils",
    srcs = [
        "model_utils.py",
    ],
    deps = [
        requirement("tensorflow"),
        requirement("numpy"),
        ":common_utils",
        "//vitis_quantizer/common:vitis_quantize_aware_activation",
        "//vitis_quantizer/common:vitis_quantize_wrapper",
        "//vitis_quantizer/eight_bit:vitis_8bit_quantize_transforms",
        "//vitis_quantizer/graph_transformations:model_transformer",
        "//vitis_quantizer/layers:vitis_activation",
        "//vitis_quantizer/layers:vitis_quantize",
        "//vitis_quantizer/optimizations:vitis_optimize_transforms",
    ],
)
