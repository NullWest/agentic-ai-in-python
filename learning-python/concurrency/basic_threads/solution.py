import concurrent.futures
import os
import os.path
import argparse

class DirectoryTree:
    def __init__(self, initial_path: str, only_directories = False)->None:
        self.initial_path: str = initial_path
        self.only_directories: bool = only_directories

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        self.paths: dict[str, dict] = {}
        self.futures: list[concurrent.futures.Future] = []

    def handle(self)->None:
        self.__read(os.path.abspath(self.initial_path), self.paths)

        can_list = True

        if self.futures:
            result = concurrent.futures.wait(self.futures)
            can_list = bool(result.done)

        if can_list:
            self.__display(self.paths)

    def __read(self, directory_path: str, node: dict)->None:
        try:
            with os.scandir(directory_path) as entries:
                for entry in entries:
                    name = entry.name
                    path = entry.path

                    if entry.is_file() and not self.only_directories:
                        node[name] = name

                    if entry.is_dir(follow_symlinks=False):
                        node[name] = {}

                        future = self.executor.submit(self.__read, path, node[name])

                        self.futures.append(future)

        except FileNotFoundError:
            print(f'Directory {directory_path} not found.')
        except PermissionError:
            print(f'{directory_path} Permission denied.')
        except Exception as exception:
            print(f'An unexpected error occurred: {exception}.')

    def __display(self, node: dict, depth: int = 0)->None:
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

    parser.add_argument(
        'path',
        type=str,
        help='Path to directory to display'
    )

    parser.add_argument(
        '--only-directories',
        action='store_true',
        help='Only display directories',
        default = False,
    )

    args = parser.parse_args()

    directory = DirectoryTree(initial_path=args.path, only_directories=args.only_directories)
    directory.handle()