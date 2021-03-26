#!/usr/bin/python
import re
import sys
import os

if __name__ == "__main__":
    maker_executable = os.getenv("MAKER_EXECUTABLE")
    if maker_executable:
        from pip._vendor.distlib.scripts import ScriptMaker
        ScriptMaker.executable = maker_executable

    from pip._internal.cli.main import main
    sys.exit(main())


