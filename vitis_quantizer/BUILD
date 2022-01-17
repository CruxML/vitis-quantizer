load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "vitis_quantize",
    srcs = [
        "vitis_quantize.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":vitis_quantize_strategies",
        "//vitis_quantizer/base:quantize_annotate",
        "//vitis_quantizer/base:quantize_config",
        "//vitis_quantizer/common:vitis_quantize_aware_activation",
        "//vitis_quantizer/common:vitis_quantize_configs",
        "//vitis_quantizer/common:vitis_quantize_registry",
        "//vitis_quantizer/common:vitis_quantize_wrapper",
        "//vitis_quantizer/common:vitis_quantizers",
        "//vitis_quantizer/eight_bit:vitis_8bit_quantize_strategy",
        "//vitis_quantizer/eight_bit_fs:vitis_8bit_fs_quantize_strategy",
        "//vitis_quantizer/layers:vitis_activation",
        "//vitis_quantizer/layers:vitis_pooling",
        "//vitis_quantizer/layers:vitis_quantize",
        "//vitis_quantizer/optimizations:vitis_bias_correction",
        "//vitis_quantizer/optimizations:vitis_fast_finetune",
        "//vitis_quantizer/utils:common_utils",
        "//vitis_quantizer/utils:model_utils",
    ],
)

py_library(
    name = "vitis_quantize_strategies",
    srcs = [
        "vitis_quantize_strategies.py",
    ],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/eight_bit:vitis_8bit_quantize_strategy",
        "//vitis_quantizer/eight_bit:vitis_8bit_tqt_quantize_strategy",
        "//vitis_quantizer/eight_bit_fs:vitis_8bit_fs_quantize_strategy",
        "//vitis_quantizer/utils:common_utils",
    ],
)
