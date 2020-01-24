import numpy


def get_greeting():
    """Get a hello-dependency."""
    return f"Hello numpy=={numpy.version.version}!"
