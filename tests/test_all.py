#!/usr/bin/env python
import pytest
import subprocess
import ipaddress

import findssh
from findssh.runner import runner

PORT = 22
SERVICE = ""
TIMEOUT = 1.0


def test_script():
    subprocess.check_call(["findssh"])


def test_coroutine():
    net = findssh.netfromaddress(findssh.getLANip())
    hosts = runner(findssh.get_hosts, net, PORT, SERVICE, TIMEOUT)
    if len(hosts) > 0:
        host = hosts[0]
        assert isinstance(host[0], ipaddress.IPv4Address)
        assert isinstance(host[1], str)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
