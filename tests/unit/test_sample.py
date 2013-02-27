# $HeadURL$
import sys


def test_import():
    """ Test to make sure the project imports OK.
    """
    import pp.testing


def test_app():
    """ Test the command-line app runs OK.
    """
    from pp.testing.scripts import app
    sys.argv = []
    app.main()


if __name__ == '__main__':
    # Run this tet file through py.test if executed on the cmdline
    import pytest
    pytest.main(args=[sys.argv[0]])
