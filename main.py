import argparse
import os
import shutil
import sys
from collections import defaultdict

from bindings import extension_to_type, extension_to_type_abstracted


class ClutterManager:
    def __init__(self, root, abstract):
        self.root = root
        self.index = defaultdict(list)
        self.abstract = abstract

    def sort(self):
        for item in os.listdir(self.root):
            path = os.path.join(self.root, item)
            if os.path.isdir(path):
                continue
            if self.abstract:
                self.index[item] = extension_to_type_abstracted[item.split(
                    '.')[-1]]
            else:
                self.index[item] = extension_to_type[item.split('.')[-1]]
            dest_path = os.path.join(
                self.root, self.index[item].capitalize(), item)
            try:
                if not os.path.isdir(os.path.dirname(dest_path)):
                    os.makedirs(os.path.dirname(dest_path))
                shutil.move(path, dest_path)
                print('{} -> {}'.format(path, dest_path))
            except NotADirectoryError:
                print('A file with name: {} is'.format(item), end='')
                print(' conflicting with directory name.')
                print('Please rename it and try again')
                sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", help="relative path to clumsy directory",
                        default=".")
    parser.add_argument("--abstract", help="abstracted folder names",
                        default=True)
    args = parser.parse_args()

    sorter = ClutterManager(os.path.abspath(args.root), args.abstract)
    sorter.sort()
