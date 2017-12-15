#!/usr/bin/env python3

#-
# Copyright (c) 2017 Andrew Turner
# All rights reserved.
#
# This software was developed by SRI International and the University of
# Cambridge Computer Laboratory under DARPA/AFRL contract FA8750-10-C-0237
# ("CTSRD"), as part of the DARPA CRASH research programme.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

# A simple script to build a manifest for the FreeBSD makefs

import os
import os.path
import stat
import sys

try:
    path = sys.argv[1]
except IndexError:
    print("Usage: {0} <base path>".format(sys.argv[0]))
    sys.exit(1)

path_len = len(path)
for root, dirs, files in os.walk(path):
    sb = os.stat(root)
    print(os.path.join('.', root[path_len:]), "type=dir uname=root gname=wheel mode=0{0:o}".format(sb.st_mode & 0o777))
    for f in files:
        name = os.path.join(root, f)
        loc = os.path.abspath(name)
        sb = os.stat(name)
        print(os.path.join('.', name[path_len:]), "type=file uname=root gname=wheel mode=0{0:o} contents={1}".format(sb.st_mode & 0o777, loc))
        assert stat.S_ISREG(sb.st_mode)
