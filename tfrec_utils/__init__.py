import tensorflow as tf
#import cv2

__version__ = "0.2.10.0"

import importlib 

_submodules = [
        "reading",
	"writing"
]

lib_name = "tfrec_utils"

__all__ = _submodules # add non-modules, such as clone, get_config, set_config, show_versions 

def __dir__():
    return __all__

def __getattr__(name):
    if name in _submodules:
        return importlib.import_module(f"{lib_name}.{name}")
    else:
        try:
            return globals()[name]
        except KeyError:
            raise AttributeError(f"Module {lib_name} has no attribute '{name}', (yet).")


