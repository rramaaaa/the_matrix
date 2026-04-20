import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_name() -> str | None:
    path = os.environ.get("VIRTUAL_ENV")
    if path:
        return os.path.basename(path)
    return None


def outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()

    print("To enter the construct, run:")
    print("python -m venv matrix_env")

    print("matrix_env\\Scripts\\activate # On Windows")
    print("source matrix_env/bin/activate # On Unix")
    print()

    print("Then run this program again.")


def inside_status() -> None:
    name = get_name()
    path = os.environ.get("VIRTUAL_ENV")

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {name}")
    print(f"Environment Path: {path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")

    packages_paths = site.getsitepackages()
    print(packages_paths[0])

try:
    if is_virtual_env():
        inside_status()
    else:
        outside_venv()

except Exception as e:
    print(f"ERROR: {e}")
