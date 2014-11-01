# Copyright (C) 2014, Kushal Das <kushaldas@gmail.com>

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
from fabric.api import sudo


def selinux():
    'Gets the selinux status'
    return sudo('getenforce')

def systemlogging():
    'Gets the system logging status'
    return sudo('journalctl -a --no-pager -r --since=$(date +%Y-%m-%d) -n1')

def service_status():
    'No service should fail in the startup'
    return sudo('systemctl --all --failed')

def all():
    res = selinux()
    if res == 'Enforcing':
        selinux_result = "SeLinux passsed."
    res = systemlogging()
    if res.splitlines() == 2:
        system_logging_result = "System logging test passed."
    else:
        system_logging_result = "System logging test failed."
    res = service_status()
    if '0 loaded units listed' in res:
        status = True
        service_result = "Service tests passed."
    else:
        status = False
        service_result = res

    print "\n\n\n"
    print selinux_result
    print system_logging_result
    print service_result

