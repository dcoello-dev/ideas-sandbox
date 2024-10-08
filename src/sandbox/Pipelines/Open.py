import os

from sandbox.Core.ExecuteParentShell import write_on_parent_shell
from sandbox.Core.IPipeline import IPipeline
from sandbox.Core.RegisterPipeline import REGISTERPIPELINE
from sandbox.Core.FzfHandler import fzf_handler, sniff_dir


@REGISTERPIPELINE("open", "open idea on your text editor")
class Open(IPipeline):
    def __init__(self, env_namespace):
        self.env_namespace_ = env_namespace

    @staticmethod
    def declare_args(subparser):
        parser_upload = subparser.add_parser('open')

        parser_upload.add_argument(
            '-e', '--editor',
            default=os.environ.get('SANDBOX_EDITOR', 'vim'),
            help='editor to use')

        parser_upload.add_argument(
            '-p', '--path',
            default="",
            help='idea or directory path')

        parser_upload.add_argument(
            '-w', '--work_idea',
            action="store_true",
            help='open current work idea')

    def _open_file(self, path, args):
        write_on_parent_shell(f"{args.editor} {path}")
        return 0

    def run(self, args) -> int:
        if args.path == "":
            args.path = args.ideas

        if os.path.isfile(args.path):
            return self._open_file(args.path, args)
        if args.work_idea:
            return self._open_file(f"{args.path}/main*", args)
        else:
            return self._open_file(fzf_handler(sniff_dir(args.path)), args)
