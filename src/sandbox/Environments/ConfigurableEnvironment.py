import re
from string import Template

from sandbox.Core.IEnvironment import IEnvironment

class GenericEnvironment(IEnvironment):

    def __init__(self, env):
        self.matcher_ = r"(sandbox_[a-z]+):\s*([a-z]*)"
        self.env_ = env

    def template(self) -> str:
        return self.env_["template"]

    def execute(self, file_path) -> str:
        return Template(self.env_["execution"]).safe_substitute(file_path=file_path)

    def format(self, file_path) -> str:
        return Template(self.env_["format"]).safe_substitute(file_path=file_path)

    def is_file_env(self, file_path) -> bool:
        with open(file_path, "r") as file:
            for line in file:
                find = re.findall(self.matcher_, line)
                for f in find:
                    if f[0] == "sandbox_env":
                        return (f[1] == self.env_["name"])
        return False

    def extract_meta(self, file_path) -> dict:
        ret = dict(
            sandbox_idea="",
            sandbox_name="",
            sandbox_description="",
            sandbox_env=self.env_["name"])
        with open(file_path, "r") as file:
            for line in file:
                find = re.findall(self.matcher_,line)
                for f in find:
                    if f[0] in ret.keys():
                        ret[f[0]] = f[1]
        return ret

    def work_filename(self) -> str:
        return f"main.{self.env_['ext']}"
