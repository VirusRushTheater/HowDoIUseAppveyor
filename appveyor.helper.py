#!/usr/bin/env python
# Build the project on AppVeyor.

import os
import sys
import argparse
from subprocess import check_call

argp = argparse.ArgumentParser(description="OS-agnostic Appveyor.py building/deploying script")
argp.add_argument("--step", help="Step name")
args = argp.parse_args()

assert(argp.step in ["configure", "build", "deploy"])

# Environment variables


if argp.step == "configure":
	# Make sure third-party dependencies are fulfilled.
	check_call(["git", "submodule", "update", "--init", "--recursive"])

	

elif argp.step == "build":
	pass
elif argp.step == "deploy":
	pass
else:
	print("The script will do nothing", file=sys.stderr)
	exit(-1)

config = os.environ['CONFIG']
path = os.environ['PATH']
cmake_command = ['cmake', '-DFMT_PEDANTIC=ON', f'-DCMAKE_BUILD_TYPE={}']

os.environ['PATH'] = r'C:\Program Files (x86)\MSBuild\14.0\Bin;' + path
build_command = ['msbuild', '/m:4', '/p:Config=' + config, 'foo.sln']
#test_command = ['msbuild', 'RUN_TESTS.vcxproj']

check_call(cmake_command)
check_call(build_command)
#check_call(test_command)