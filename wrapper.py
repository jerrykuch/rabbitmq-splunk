import os
import sys
import subprocess

# Capture where your system Python interpreter is (not Splunk's embedded one);
# This lets us add packages to a Python environment that isn't the embedded
# Splunk one, thereby letting them survive Splunk updates, not interfere with
# other Splunk-provided packages, etc.
_NEW_PYTHON_PATH = '/usr/bin/python'
_SPLUNK_PYTHON_PATH = os.environ['PYTHONPATH']
os.environ['PYTHONPATH'] = _NEW_PYTHON_PATH
os.unsetenv('LD_LIBRARY_PATH')   # Unset to stifle annoying log warnings

script_name  = sys.argv[1]
surplus_args = sys.argv[2:]

script_path = os.path.join('/opt/splunk/bin/scripts', script_name)
popen_args  = [os.environ['PYTHONPATH'], script_path] + surplus_args

p = subprocess.Popen(popen_args,
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

output = p.communicate()[0]

print output
