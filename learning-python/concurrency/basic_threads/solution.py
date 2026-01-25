import concurrent.futures
import os
import os.path
import argparse

class DirectoryTree:
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    paths: dict[str, dict] = {}
    futures: list[concurrent.futures.Future] = []

    def __init__(self, initial_path: str)->None:
        self.read(os.path.abspath(initial_path), self.paths)
        self.display(self.paths)

    @classmethod
    def read(cls, directory: str, node: dict)->None:
        try:
            with os.scandir(directory) as entries:
                for entry in entries:
                    name = entry.name
                    path = entry.path

                    if entry.is_file():
                        node[name] = name

                    if entry.is_dir(follow_symlinks=False):
                        node[name] = {}

                        future = cls.executor.submit(cls.read, path, node[name])

                        cls.futures.append(future)

        except FileNotFoundError:
            print(f'Directory {directory} not found.')
        except PermissionError:
            print(f'{directory} Permission denied.')

    @classmethod
    def display(cls, node: dict, depth: int = 0)->None:
        should_list = True

        if cls.futures:
            result = concurrent.futures.wait(cls.futures)
            should_list = bool(result.done)

        if should_list:
            for key in dict(sorted(node.items())):
                value = node[key]
                name = '  ' * depth + key

                if isinstance(value, dict):
                    print(name + '/')
                    cls.display(value, depth + 1)
                else:
                    print(name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('path', type=str, help='Path to directory to display')

    args = parser.parse_args()

    DirectoryTree(args.path)