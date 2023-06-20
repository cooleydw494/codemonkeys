import argparse
import sys
from install import install


def main():
    parser = argparse.ArgumentParser(prog='codemonkeys')
    parser.add_argument('command', help='The command to execute.')
    parser.add_argument('name', help='The name of the new project.')

    args = parser.parse_args()

    if args.command.lower() == 'new':
        install(args.name)
    else:
        print(f"Unknown command {args.command}", file=sys.stderr)


if __name__ == '__main__':
    main()
