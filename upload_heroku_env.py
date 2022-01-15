from argparse import ArgumentParser
import subprocess as sp

parser = ArgumentParser(
    description="Upload environmental variables from file to heroku."
)
parser.add_argument(
    "-f", help="Bash filename containing env variables", default=".env.heroku"
)
parser.add_argument(
    "-u", help="unset env vars in bash file", action="store_true", default=False
)
args = parser.parse_args()


def register_env_var_to_heroku():
    with open(args.f) as f:
        env_vars = [
            var.split("=")[0] if args.u else var for var in f.read().splitlines()
        ]
        action = "set" if not args.u else "unset"
        sp.run(f"heroku config:{action}".split() + env_vars)


if __name__ == "__main__":
    register_env_var_to_heroku()
