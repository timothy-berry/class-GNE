from os import path
import os

import pytest

from netmiko import ConnectHandler, FileTransfer, InLineTransfer, SSHDetect
from test_utils import parse_yaml
