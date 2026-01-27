import os
import os.path
import concurrent.futures
from threading import Lock
from queue import Queue
from arguments import parse_arguments

class DirectoryTree:
    def __init__(self, initial_path: str, only_directories = False)->None:
        self.initial_path: str = os.path.abspath(initial_path)
        self.only_directories: bool = only_directories

    def output(self)->None:
        self.__read(self.initial_path)

    def __scan(self, root_path: str)->dict:
        tree = {}

        queue = Queue()
        lock = Lock()

        queue.put((root_path, tree))

        def worker():
            while True:
                try:
                    path, node = queue.get(timeout=0.1)

                    with os.scandir(path) as entries:
                        for entry in entries:
                            if entry.is_file() and not self.only_directories:
                                with lock:
                                    node[entry.name] = entry.name

                            if entry.is_dir(follow_symlinks=False):
                                with lock:
                                    node[entry.name] = {}

                                queue.put((entry.path, node[entry.name]))

                except FileNotFoundError:
                    print(f'Directory {root_path} not found.')
                except PermissionError:
                    print(f'{root_path} Permission denied.')
                except Exception as exception:
                    print(f'An unexpected error occurred: {exception}.')
                finally:
                    queue.task_done()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            for _ in range(4):
                executor.submit(worker)

            queue.join()
            executor.shutdown(wait=True)

        return tree

    def __read(self, directory_path: str)->None:
        self.__display(self.__scan(directory_path))

    def __display(self, node: dict, depth: int = 0)->None:
        lexical_order = dict(sorted(node.items()))

        for key in lexical_order:
            value = node[key]
            name = '  ' * depth + key

            if isinstance(value, dict):
                print(name + '/')
                self.__display(value, depth + 1)
            else:
                print(name)

if __name__ == '__main__':
    args = parse_arguments()

    directory = DirectoryTree(initial_path=args.path, only_directories=args.only_directories)

    directory.output()
