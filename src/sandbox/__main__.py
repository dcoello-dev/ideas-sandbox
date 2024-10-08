import os
import argparse

from sandbox.Core.RegisterEnvironment import load_env_namespace
from sandbox.Core.RegisterPipeline import load_pipeline_namespace

parser = argparse.ArgumentParser(
    description="sandbox framework")

parser.add_argument(
    '-i', '--ideas',
    default=os.path.expandvars(f"{os.environ.get('SANDBOX_IDEAS', '').strip()}/"),
    help="ideas repo path")


def main():
    subparsers = parser.add_subparsers(dest='pipeline')
    subparsers.required = True
    pipelines = load_pipeline_namespace()
    for pip in pipelines:
        pipelines[pip]["type"].declare_args(subparsers)

    args = parser.parse_args()
    env = load_env_namespace()

    pip = pipelines[args.pipeline]["type"](env)
    pip.run(args)


if __name__ == "__main__":
    main()
