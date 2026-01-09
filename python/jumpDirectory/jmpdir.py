import argparse as ap
import os

SOURCE_DIR = os.path.dirname(os.path.realpath(__file__))

parser = ap.ArgumentParser()
parser.add_argument("bookmark", nargs='?',default=None , help="bookmark name")
parser.add_argument("-c", "--create", help="used to create a bookmark", type=str)
parser.add_argument("-l", "--list", help="used to list all bookmarks", action="store_true")
parser.add_argument("-r", "--remove", help="used to delete a bookmark")

args = parser.parse_args()

if args.bookmark:
    with open(f"{SOURCE_DIR}/bookmarks", "r") as f:
        for line in f:
            if line.startswith(f"{args.bookmark}="):
                bkdir = line.split("=")[1][:-1]
                print(bkdir) 

if args.create:
    with open(f"{SOURCE_DIR}/bookmarks", "a") as f:
        f.write(f"{args.create}={os.environ['PWD']}")

if args.list:
    with open(f"{SOURCE_DIR}/bookmarks", "r") as f:
        for line in f:
            print(f"{line}")

if args.remove:
    bookmark=args.remove
    with open(f"{SOURCE_DIR}/bookmarks") as f:
        lines = f.readlines()
    
    lines = [line for line in lines if not line.startswith(f"{bookmark}=")]
    
    with open(f"{SOURCE_DIR}/bookmarks") as f:
        f.writelines(lines)


