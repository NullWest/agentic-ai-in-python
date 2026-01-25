import concurrent.futures
import os
import os.path
import argparse

class DirectoryTree:
    def __init__(self, initial_path: str, only_directories = False, show_summary_line = False)->None:
        self.initial_path = initial_path
        self.only_directories = only_directories
        self.show_summary_line = show_summary_line

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        self.paths = {}
        self.futures = []

    def handle(self):
        self.__read(os.path.abspath(self.initial_path), self.paths)
        self.__display(self.paths)

    def __read(self, directory_path: str, node: dict)->None:
        try:
            with os.scandir(directory_path) as entries:
                for entry in entries:
                    name = entry.name
                    path = entry.path

                    if entry.is_file():
                        node[name] = name

                    if entry.is_dir(follow_symlinks=False):
                        node[name] = {}

                        future = self.executor.submit(self.__read, path, node[name])

                        self.futures.append(future)

        except FileNotFoundError:
            print(f'Directory {directory} not found.')
        except PermissionError:
            print(f'{directory} Permission denied.')

    def __display(self, node: dict, depth: int = 0)->None:
        should_list = True

        if self.futures:
            result = concurrent.futures.wait(self.futures)
            should_list = bool(result.done)

        if should_list:
            for key in dict(sorted(node.items())):
                value = node[key]
                name = '  ' * depth + key

                if isinstance(value, dict):
                    print(name + '/')
                    self.__display(value, depth + 1)
                else:
                    print(name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('path', type=str, help='Path to directory to display')
    parser.add_argument('--only-directories', type=bool, default=False, help='Only display directories')
    parser.add_argument('--show-summary-line', type=bool, default=False, help='Show summary line')

    args = parser.parse_args()

    directory = DirectoryTree(initial_path=args.path, only_directories=args.only_directories)
    directory.handle()