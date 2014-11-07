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
    result = 'Test SeLinux: {status}'
    response = sudo('getenforce')
    return_value = False
    status = 'FAIL'
    if response == 'Enforcing':
        status = 'SUCCESS'
        return_value = True
    print result.format(status=status)
    return return_value


def systemlogging():
    'Gets the system logging status'
    result = 'Test system logging: {status}'
    response = sudo(
        'journalctl -a --no-pager -r --since=$(date +%Y-%m-%d) -n1')
    return_value = False
    status = 'FAIL'
    if response.splitlines() == 2:
        status = 'SUCCESS'
        return_value = True
    print result.format(status=status)
    return return_value


def service_status():
    'No service should fail in the startup'
    result = 'Test service: {status}'
    response = sudo('systemctl --all --failed')
    status = 'FAIL'
    return_value = False
    if '0 loaded units listed' in response:
        status = 'SUCCESS'
        return_value = True
    print result.format(status=status)
    return return_value

def install_pss():
    "This will install pss to test yum/dnf and network of the system."
    result = 'Yum installation: {status}'
    response = sudo('yum install pss -y')
    response = sudo('ls -l /usr/bin/pss')
    status = 'FAIL'
    return_value = False
    if not  'No such file or directory' in response:
        status = 'PASS'
        return_value = False
    print result.format(status=status)
    return return_value

def all():
    print "\n\n\n"
    selinux()
    systemlogging()
    service_status()
