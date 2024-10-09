import os

from sandbox.Core.IPipeline import IPipeline
from sandbox.Core.RegisterPipeline import REGISTERPIPELINE


@REGISTERPIPELINE("save", "save work idea")
class Save(IPipeline):
    def __init__(self, env_namespace):
        self.env_namespace_ = env_namespace

    @staticmethod
    def declare_args(subparser):
        parser_upload = subparser.add_parser('save')

        parser_upload.add_argument(
            '-p', '--path',
            default="",
            help='work file')

    def _save_file(self, args, meta):
        os.system(f"mkdir -p {args.ideas}/{meta['sandbox_idea']}")
        idea_name = f'{args.ideas}/{meta["sandbox_idea"]}/{meta["sandbox_name"]}.{args.path.split(".")[-1]}'
        os.system(f"cp {args.path} {idea_name}")

    def _get_work_idea_path(self, path):
        for file in os.listdir(path):
            filename = os.fsdecode(file)
            if filename.startswith("main"):
                return f"{path}/{file}"
        return ""

    def run(self, args) -> int:
        if args.path == "":
            args.path = args.ideas
        if os.path.isdir(args.path):
            args.path = self._get_work_idea_path(args.path)
        if os.path.isfile(args.path):
            for env in self.env_namespace_:
                if self.env_namespace_[env]["type"].is_file_env(args.path):
                    env = self.env_namespace_[env]["type"]()
                    self._save_file(args, env.extract_meta(args.path))
                    return 1

        return 1
