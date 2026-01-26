import argparse

def parse_arguments()->argparse.Namespace:
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
        default=False,
    )

    return parser.parse_args()