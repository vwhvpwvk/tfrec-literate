# import whatever library necessary

__version__ = "1.0.0"

import importlib 

_submodules = [
        "awesome_submodule"
]

lib_name = "awesome_lib"

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


