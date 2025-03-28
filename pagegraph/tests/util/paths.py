from inspect import getsourcefile
from os.path import abspath
import pathlib


# Adapted from https://stackoverflow.com/a/18489147
THIS_FILE = pathlib.Path(abspath(str(getsourcefile(lambda: 0))))
TESTS_CODE_DIR = THIS_FILE.parent.parent
PROJECT_ROOT_DIR = TESTS_CODE_DIR.parent
TEST_ASSETS_DIR = PROJECT_ROOT_DIR / "tests/assets"


def testcases() -> pathlib.Path:
    return TEST_ASSETS_DIR / "html"


def graphs() -> pathlib.Path:
    return TEST_ASSETS_DIR / "graphs"


def generated_graphs() -> pathlib.Path:
    return graphs() / "gen"


def saved_graphs() -> pathlib.Path:
    return graphs() / "saved"


def unittests() -> pathlib.Path:
    return TESTS_CODE_DIR
