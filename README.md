# pip-wrapper

a trivial wrapper around [pip](https://github.com/pypa/pip) on Windows that lets you overwrite the path to `python.exe` that gets hardcoded in launcher `Scripts\<script>.exe` files that pip creates via distlib.

**<p align="center">⚠️ status: experimental</p>**

## installation

- (optional: rebuild the wrapper pip.exe: `make`)
- place the `pip_wrapper` dir somewhere on disk
- prepend the path to `pip_wrapper\bin` to the `PATH` env var (ensure it's positioned prior of any python installation path so it takes precedence over any other `pip.exe` on the system)

## usage

set env var `MAKER_EXECUTABLE` with the desired path to python.exe and run the wrapper `pip.exe` to install packages.

## example

Example: Installing a relocatable* `pip-sync.exe` via pip:

(* relocatable = runs with whatever `python.exe` the `PATH` env var points to)

in a `cmd.exe` shell:

```
$ where pip
C:\pip_wrapper\bin\pip.exe
$ where python
c:\py3-7\python.exe
$ set MAKER_EXECUTABLE=python.exe
$ set destdir=c:\destdir
$ mkdir %destdir%
$ pip install pip-tools --prefix=%destdir%
```

to run the generated `pip-sync.exe`:
```
$ set PYTHONPATH=%destdir%\Lib\site-packages
$ %destdir%\Scripts\pip-sync.exe --version
pip-sync, version 6.0.1
```

it uses the `python.exe` found via the  `PATH` env var. If we remove any Python install path from `PATH` it will stop working:

```
$ set PATH=c:\windows\system32;c:\windows
$ where python
INFO: Could not find files for the given pattern(s).
$ %destdir%\Scripts\pip-sync.exe --version
Fatal error in launcher: Unable to create process using '"python.exe"  "C:\destdir\Scripts\pip-sync.exe" --version': The system cannot find the file specified.
```

which means we could also run `pip-sync.exe` with any other python installation:

```
$ set PATH=c:\py3-9;%PATH%
$ where python
c:\py3-9\python.exe
$ %destdir%\pip-sync.exe --version
pip-sync, version 6.0.1
```

(Without this wrapper the `pip-sync.exe` would have to get rebuilt, i.e. by reinstalling the entire package, for this to work)

