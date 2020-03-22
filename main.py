import argparse
import os
import shutil
import sys
from collections import defaultdict

from bindings import extension_to_type


class ClutterManager:
    def __init__(self, root):
        self.root = root
        self.index = defaultdict(list)

    def sort(self):
        for item in os.listdir(self.root):
            path = os.path.join(self.root, item)
            if os.path.isdir(path):
                continue
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
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    sorter = ClutterManager(root)
    sorter.sort()
