from sandbox.Core.IEnvironment import IEnvironment
from sandbox.Core.RegisterEnvironment import REGISTERENV


@REGISTERENV("echo", "echo idea content")
class Echo(IEnvironment):

    def __init__(self):
        self.template_ = """"""

    def template(self) -> str:
        return self.template_

    def execute(self, file_path) -> str:
        return f"batcat {file_path}"

    def format(self, file_path) -> str:
        return ""

    @staticmethod
    def is_file_env(file_path) -> bool:
        return False

    def extract_meta(self, file_path) -> dict:
        return {}

    def work_filename(self) -> str:
        return ""
