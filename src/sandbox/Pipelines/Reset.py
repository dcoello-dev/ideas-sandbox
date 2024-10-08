import os

from sandbox.Core.IPipeline import IPipeline
from sandbox.Core.RegisterPipeline import REGISTERPIPELINE


@REGISTERPIPELINE("reset", "reset work dir using specific env")
class Reset(IPipeline):
    def __init__(self, env_namespace):
        self.env_namespace_ = env_namespace

    @staticmethod
    def declare_args(subparser):
        parser_upload = subparser.add_parser('reset')

        parser_upload.add_argument(
            '-e', '--env',
            required=True,
            help='environment to use')

        parser_upload.add_argument(
            '-o', '--output',
            default="",
            help='output work file')

    def run(self, args) -> int:
        if args.env in self.env_namespace_.keys():
            env = self.env_namespace_[args.env]["type"]()
            if args.output == "":
                args.output = args.ideas
            os.system(f"rm {args.output}/main.*")
            with open(f"{args.output}/{env.work_filename()}", 'w+') as output_file:
                output_file.write(env.template())
                return 0
        return 1
