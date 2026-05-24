import subprocess
import sys


def test_hello_outputs_green_ansi():
    """hello.py must emit 'Hello, World!' wrapped in ANSI green (\\033[32m ... \\033[0m)."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        check=True,
    )
    stdout = result.stdout
    assert b"\x1b[32m" in stdout, f"missing green ANSI start; got {stdout!r}"
    assert b"Hello, World!" in stdout, f"missing greeting; got {stdout!r}"
    assert b"\x1b[0m" in stdout, f"missing ANSI reset; got {stdout!r}"
    # Ensure no other color codes (e.g., 31 red, 33 yellow, 34 blue, etc.)
    for bad in (b"\x1b[31m", b"\x1b[33m", b"\x1b[34m", b"\x1b[35m", b"\x1b[36m", b"\x1b[37m"):
        assert bad not in stdout, f"unexpected color code {bad!r} in output {stdout!r}"
