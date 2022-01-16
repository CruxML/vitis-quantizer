load("@pip//:requirements.bzl", "requirement")

package(default_visibility = [
    "//vitis_quantizer:__subpackages__",
])

py_library(
    name = "transforms",
    srcs = [
        "transforms.py",
    ],
    deps = [
        requirement("tensorflow"),
    ],
)

py_library(
    name = "transforms_pipeline",
    srcs = [
        "transforms_pipeline.py",
    ],
    deps = [
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_test(
    name = "transforms_test",
    srcs = [
        "transforms_test.py",
    ],
    deps = [
        requirement("tensorflow"),
        ":transforms",
    ],
)

py_library(
    name = "model_transformer",
    srcs = [
        "model_transformer.py",
    ],
    deps = [
        requirement("tensorflow"),
        ":transforms",
        "//vitis_quantizer/utils:common_utils",
    ],
)

py_test(
    name = "model_transformer_test",
    srcs = [
        "model_transformer_test.py",
    ],
    deps = [
        requirement("tensorflow"),
        requirement("numpy"),
        ":model_transformer",
        ":transforms",
    ],
)
