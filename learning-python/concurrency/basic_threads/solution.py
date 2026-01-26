import concurrent.futures
import os
import os.path
import argparse

class DirectoryTree:
    def __init__(self, initial_path: str, only_directories = False)->None:
        self.initial_path: str = os.path.abspath(initial_path)
        self.only_directories: bool = only_directories

        self.paths: dict[str, dict] = {}


    def handle(self)->None:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            executor.submit(self.__read, self.initial_path, self.paths)

        self.__display(self.paths)

        executor.shutdown(wait=True)

    def __read(self, directory_path: str, node: dict)->None:
        try:
            with os.scandir(directory_path) as entries:
                for entry in entries:
                    if entry.is_file() and not self.only_directories:
                        node[entry.name] = entry.name

                    if entry.is_dir(follow_symlinks=False):
                        node[entry.name] = {}

                        self.__read(entry.path, node[entry.name])

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