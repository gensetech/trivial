# Trivial Project

This project is a trivial example to demonstrate how to use relative import.

You can run `main.py` to import function from file `inpy.py` which has a relative import from `outpy.py`

Additional, you can also run `inpy.py` in `outer/inner/` working directory.

## Example
```commandline
PS C:\Users\William\Documents\GitHub\trivial> python main.py
I am outsider
PS C:\Users\William\Documents\GitHub\trivial> cd outer/inner/
PS C:\Users\William\Documents\GitHub\trivial\outer\inner> python inpy.py 
I am outsider
```

Alternatively, you can call with `-m` as a package as following:
```
PS C:\Users\William\Documents\GitHub\trivial> python -m outer.inner.inpy
I am outsider
```