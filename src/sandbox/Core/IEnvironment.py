from abc import ABC, abstractmethod


class IEnvironment(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def template(self) -> str:
        pass

    @abstractmethod
    def execute(self, file_path) -> str:
        pass

    @abstractmethod
    def format(self, file_path) -> str:
        pass

    @staticmethod
    @abstractmethod
    def is_file_env(file_path) -> bool:
        pass

    @abstractmethod
    def extract_meta(self, file_path) -> dict:
        pass

    @abstractmethod
    def work_filename(self) -> str:
        pass
