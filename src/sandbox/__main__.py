import argparse

parser = argparse.ArgumentParser(
    description="sandbox framework")

parser.add_argument(
    '-i', '--ideas',
    required=True,
    help="ideas repo path")

args = parser.parse_args()

if __name__ == "__main__":
    pass

