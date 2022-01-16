load("@pip//:requirements.bzl", "requirement")

package(default_visibility = [
    "//vitis_quantizer:__subpackages__",
])

py_library(
    name = "vitis_quantize_aware_activation",
    srcs = [
        "vitis_quantize_aware_activation.py",
    ],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_quantize_configs",
    srcs = [
        "vitis_quantize_configs.py",
    ],
    deps = [
        requirement("tensorflow"),
        ":vitis_quantizers",
        "//vitis_quantizer/base:quantize_config",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_quantize_ops",
    srcs = [
        "vitis_quantize_ops.py",
    ],
    deps = [
        requirement("tensorflow"),
        requirement("tensorflow-model-optimization"),
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_quantize_registry",
    srcs = [
        "vitis_quantize_registry.py",
    ],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/base:quantize_config",
        "//vitis_quantizer/base:quantize_registry",
        "//vitis_quantizer/common:vitis_quantize_configs",
        "//vitis_quantizer/layers:vitis_activation",
        "//vitis_quantizer/layers:vitis_pooling",
        "//vitis_quantizer/layers:vitis_quantize",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_quantize_strategy",
    srcs = [
        "vitis_quantize_strategy.py",
    ],
    deps = [
        "//vitis_quantizer/base:quantize_strategy",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_quantize_wrapper",
    srcs = [
        "vitis_quantize_wrapper.py",
    ],
    deps = [
        requirement("tensorflow"),
        "//vitis_quantizer/common:vitis_quantize_aware_activation",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_library(
    name = "vitis_quantizers",
    srcs = [
        "vitis_quantizers.py",
    ],
    deps = [
        requirement("tensorflow"),
        ":vitis_quantize_ops",
        "//vitis_quantizer/base:quantizer",
    ],
)
