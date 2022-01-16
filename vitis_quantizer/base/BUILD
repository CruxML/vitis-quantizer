load("@pip//:requirements.bzl", "requirement")

package(default_visibility = [
    "//vitis_quantizer:__subpackages__",
])

py_library(
    name = "quantize_annotate",
    srcs = [
        "quantize_annotate.py",
    ],
    deps = [
        requirement("tensorflow"),
    ],
)

py_library(
    name = "quantize_config",
    srcs = [
        "quantize_config.py",
    ],
)

py_library(
    name = "quantize_registry",
    srcs = [
        "quantize_registry.py",
    ],
)

py_library(
    name = "quantize_strategy",
    srcs = [
        "quantize_strategy.py",
    ],
)

py_library(
    name = "quantizer",
    srcs = [
        "quantizer.py",
    ],
    deps = [
        requirement("tensorflow"),
    ],
)
