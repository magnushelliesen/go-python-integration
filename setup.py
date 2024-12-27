from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import shutil
from pathlib import Path
import subprocess


class build_go_ext(build_ext):
    """Custom command to build Go shared library."""
    def run(self):
        # Run the `go build` command
        lib_path = Path(__file__).resolve().parent / "fibonacci/go/library.go"
        output_path = Path(__file__).resolve().parent / "fibonacci/go/library.so"
        command = ["go", "build", "-buildmode=c-shared", "-o", str(output_path), str(lib_path)]
        if subprocess.call(command) != 0:
            raise RuntimeError("Go build failed")
        # Proceed with normal build_ext
        super().run()


setup(
    name="fibonacci",
    version="0.1.0",
    packages=["fibonacci"],
    package_data={"fibonacci": ["go/library.so"]},  # Include library.so
    cmdclass={"build_ext": build_go_ext},
    zip_safe=False,
)
