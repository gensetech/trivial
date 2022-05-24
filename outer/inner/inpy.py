if __package__ is None:
    import sys
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from outpy import outsider
else:
    from ..outpy import outsider


def in_call_out():
    return print(outsider())


if __name__ == "__main__":
    in_call_out()
