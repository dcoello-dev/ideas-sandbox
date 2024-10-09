from sandbox.Core.IEnvironment import IEnvironment
from sandbox.Core.RegisterEnvironment import REGISTERENV


@REGISTERENV("markdown", "default markdown environment")
class Markdown(IEnvironment):

    def __init__(self):
        self.template_ = """[//]: # (sandbox_idea: )
[//]: # (sandbox_name: )
[//]: # (sandbox_description: )
[//]: # (sandbox_env: markdown)

# IDEA
"""

    def template(self) -> str:
        return self.template_

    def execute(self, file_path) -> str:
        return f"glow {file_path}"

    def format(self, file_path) -> str:
        return f"echo \"nothing\""

    @staticmethod
    def is_file_env(file_path) -> bool:
        with open(file_path, "r") as file:
            for line in file:
                if line.strip() == "[//]: # (sandbox_env: markdown)".strip():
                    return True
        return False

    def extract_meta(self, file_path) -> dict:
        ret = dict(
            sandbox_idea="",
            sandbox_name="",
            sandbox_description="",
            sandbox_env="markdown")
        with open(file_path, "r") as file:
            for line in file:
                term = line.split(":")[1].replace(" # (", "")
                if term in ret.keys():
                    ret[term] = line.split(":")[2].replace(")", "").strip()
        return ret

    def work_filename(self) -> str:
        return "main.md"
