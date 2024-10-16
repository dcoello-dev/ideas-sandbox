import os
import json
import logging

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
            env = self.env_namespace_[args.env]
            if args.output == "":
                args.output = args.ideas
            os.system(f"rm {args.output}/main.*")
            filename = f"{args.output}/{env.work_filename()}"
            with open(filename, 'w+') as output_file:
                output_file.write(env.template())
                logging.info(f"created {filename} using env {args.env}")
                return 0
        else:
            logging.error(f"{args.env} not in namespace: {json.dumps(list(self.env_namespace_.keys()))}")
        return 1
