from sandbox.Core.IEnvironment import IEnvironment
from sandbox.Core.RegisterEnvironment import REGISTERENV


@REGISTERENV("python", "default python environment")
class Cpp(IEnvironment):

    def __init__(self):
        self.template_ = """# sandbox_idea:
# sandbox_name:
# sandbox_description:
# sandbox_env: cpp

if __name__ == "__main__":
    print("Hello World!")
"""

    def template(self) -> str:
        return self.template_

    def execute(self, file_path) -> str:
        return f"python3 {file_path}"

    def format(self, file_path) -> str:
        return f"autopep8 -i {file_path}"

    @staticmethod
    def is_file_env(file_path) -> bool:
        with open(file_path, "r") as file:
            for line in file:
                if line.strip() == "# sandbox_env: python".strip():
                    return True
        return False

    def extract_meta(self, file_path) -> dict:
        ret = dict(
            sandbox_idea="",
            sandbox_name="",
            sandbox_description="",
            sandbox_env="python")
        with open(file_path, "r") as file:
            for line in file:
                term = line.split(":")[0].replace("# ", "")
                if term in ret.keys():
                    ret[term] = line.split(":")[1].strip()
        return ret

    def work_filename(self) -> str:
        return "main.py"
