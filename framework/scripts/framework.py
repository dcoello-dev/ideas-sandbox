# TODO: save functionality
# TODO  reset functionality
# TODO  share functionality

import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--lang',
    default='cpp',
    help="target lang")

parser.add_argument(
    '--reset',
    action='store_true',
    help="reset main")

parser.add_argument(
    '--save',
    action='store_true',
    help="save idea")

args = parser.parse_args()


def reset_idea(lang):
    os.system(f"rm main.*")
    os.system(f"cp framework/templates/{lang}_main.template main.{lang}")


def get_main_file():
    matches = [f for f in os.listdir(".") if os.path.isfile(
        os.path.join(".", f)) and "main" in f]
    return matches[0] if len(matches) > 0 else None


def get_meta():
    main = get_main_file()
    if main is not None:
        with open(main, "r") as f:
            return (main, f.readline().split("idea:")[1].strip() + "." + main.split(".")[1])
    return None


def save_idea(meta):
    os.system(f"mkdir -p ideas/{meta[1].split('.')[0]}")
    os.system(f"cp {meta[0]} ideas/{meta[1].split('.')[0]}/{meta[1]}")


if __name__ == "__main__":
    if args.reset:
        reset_idea(args.lang)
    if args.save:
        save_idea(get_meta())
