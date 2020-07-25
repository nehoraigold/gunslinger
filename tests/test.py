import unittest
from sys import exit


def main():
    loader = unittest.TestLoader()
    start_dir = "tests"
    suite = loader.discover(start_dir, pattern="*_tests.py")

    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    exit(0 if res.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
