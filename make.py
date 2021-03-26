from pip._vendor.distlib.scripts import ScriptMaker
maker = ScriptMaker("pip_wrapper/scripts", "pip_wrapper/bin")
maker.executable = r"python.exe"
maker.make("pip.py")