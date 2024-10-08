import os

ENV_NAMESPACE = dict()


def REGISTERPIPELINE(name: str, description: str):
    """Register implementation.

    Args:
        name (Type): type of registered entity.
        description (str): implementation description.
    """
    def wrapper(cls):
        ENV_NAMESPACE[name] = dict(type=(cls),
                                   description=description)
        return cls
    return wrapper


def load_pipeline_namespace() -> dict:
    module = None
    for module in os.listdir(os.path.dirname(
            f"{'/'.join(__file__.split('/')[:-1])}/../Pipelines/")):
        if module == '__init__.py' or module[-3:] != '.py':
            continue
        __import__(f"sandbox.Pipelines.{module[:-3]}", locals(), globals())
    del module
    return ENV_NAMESPACE
