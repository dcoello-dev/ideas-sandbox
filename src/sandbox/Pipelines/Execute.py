import os

from sandbox.Core.FzfHandler import fzf_handler, sniff_dir
from sandbox.Core.IPipeline import IPipeline
from sandbox.Core.RegisterPipeline import REGISTERPIPELINE
from sandbox.Core.ExecuteParentShell import write_on_parent_shell


@REGISTERPIPELINE("execute", "execute env on file")
class Execute(IPipeline):
    def __init__(self, env_namespace):
        self.env_namespace_ = env_namespace

    @staticmethod
    def declare_args(subparser):
        parser_upload = subparser.add_parser('execute')

        parser_upload.add_argument(
            '-p', '--path',
            default="",
            help='work file or ideas directory')

        parser_upload.add_argument(
            '-e', '--env',
            help='force specific env regardless file meta')

    def _execute_file(self, args, file_path):
        env = None

        if args.env and args.env in self.env_namespace_.keys():
            env = self.env_namespace_[args.env]["type"]()
        else:
            for e in self.env_namespace_.keys():
                if self.env_namespace_[e]["type"].is_file_env(file_path):
                    env = self.env_namespace_[e]["type"]()

        if env:
            os.system(env.format(file_path))
            write_on_parent_shell(env.execute(file_path))
            return 0
        return 1

    def run(self, args) -> int:
        if args.path == "":
            args.path = args.ideas
        if os.path.isfile(args.path):
            return self._execute_file(args, args.path)
        return self._execute_file(args, fzf_handler(sniff_dir(args.path)))
