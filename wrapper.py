import os
import subprocess

_NEW_PYTHON_PATH = '/usr/bin/python'
_SPLUNK_PYTHON_PATH = os.environ['PYTHONPATH']

os.environ['PYTHONPATH'] = _NEW_PYTHON_PATH
os.unsetenv('LD_LIBRARY_PATH')

#my_process = os.path.join(os.getcwd(), 'amqp_ping_check.py')
my_process = os.path.join('/opt/splunk/bin/scripts', 'amqp_ping_check.py')

p = subprocess.Popen([os.environ['PYTHONPATH'], my_process, _SPLUNK_PYTHON_PATH], 
                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = p.communicate()[0]
print output
