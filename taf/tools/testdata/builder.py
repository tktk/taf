# -*- coding: utf-8 -*-

from . import *
from .. import builder
from ... import taf

import os
import os.path
import shutil
import filecmp

def copy(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
):
    _context(
        rule = _copy,
        target = _generateTarget( _TARGET ),
        source = _generateSource(
            _SOURCE,
            _TARGET,
        ),
    )

#TODO 要テスト
def _copy(
    _task,
):
    TARGET = _task.outputs[ 0 ].abspath()

    if os.path.exists( TARGET ) == False:
        os.makedirs( TARGET )

    for input in _task.inputs:
        SOURCE = input.abspath()

        TARGET_FILE = os.path.join(
            TARGET,
            str( input ),
        )

        if _compareFile(
            TARGET_FILE,
            SOURCE,
        ) == True:
            continue

        shutil.copy(
            SOURCE,
            TARGET,
        )

def _compareFile(
    _target,
    _source,
):
    if os.path.exists( _target ) == False:
        return False

    if filecmp.cmp(
        _source,
        _target,
    ) == False:
        return False

    return True

def _generateTarget(
    _TARGET,
):
    return os.path.join(
        taf.TEST_DIR,
        _TARGET,
    )

def _generateSource(
    _SOURCE,
    _TARGET,
):
    return builder.generateSource(
        _SOURCE,
        os.path.join(
            getTestdataDir(),
            _TARGET,
        ),
    )
