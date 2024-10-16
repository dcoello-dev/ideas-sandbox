import os
import toml

from sandbox.Environments.ConfigurableEnvironment import GenericEnvironment

def load_env_namespace(input_conf):
    ret = dict()
    with open(input_conf, "r") as conf:
        tml = toml.loads(conf.read())
        for k in tml:
            tml[k]["name"] = k
            ret[k] = GenericEnvironment(tml[k])
    return ret
