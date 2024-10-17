import os
import logging
import argparse

from sandbox.Core.RegisterEnvironment import load_env_namespace
from sandbox.Core.RegisterPipeline import load_pipeline_namespace

parser = argparse.ArgumentParser(
    description="sandbox framework")

parser.add_argument(
    '-i', '--ideas',
    default=os.path.expandvars(
        f"{os.environ.get('SANDBOX_IDEAS', '').strip()}/"),
    help="ideas repo path")

parser.add_argument(
    '-c', '--configuration',
    default=os.path.expandvars(
        f"{os.environ.get('SANDBOX_CONF', '').strip()}"),
    help="environmet configuration file")

parser.add_argument(
    '-v', '--log_level',
    default="warning",
    help="app log level")


def main():
    subparsers = parser.add_subparsers(dest='pipeline')
    subparsers.required = True
    pipelines = load_pipeline_namespace()
    for pip in pipelines:
        pipelines[pip]["type"].declare_args(subparsers)

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(message)s',
        level=eval(f"logging.{args.log_level.upper()}"))
    logging.info(f"sandbox {args.pipeline}")

    env = load_env_namespace(args.configuration)

    pip = pipelines[args.pipeline]["type"](env)
    pip.run(args)


if __name__ == "__main__":
    main()
