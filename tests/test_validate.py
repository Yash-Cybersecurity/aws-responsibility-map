import subprocess, sys

def test_validate_passes():
    r = subprocess.run([sys.executable, "scripts/validate.py"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr