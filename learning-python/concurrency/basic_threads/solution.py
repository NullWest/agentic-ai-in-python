import concurrent.futures
import os
import os.path
import sys


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
        result = concurrent.futures.wait(cls.futures)

        if result.done:
            for key in dict(sorted(node.items())):
                value = node[key]
                name = ' ' * depth + key

                if isinstance(value, dict):
                    print(name + '/')
                    cls.display(value, depth + 1)
                else:
                    print(name)

if __name__ == '__main__':
    argument_path = sys.argv[1]

    DirectoryTree(argument_path)