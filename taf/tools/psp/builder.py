# -*- coding: utf-8 -*-

from . import *
from .. import builder
from ... import module
from ... import taf

import os.path

def eboot(
    _context,
    _TARGET_DIR,
    _TARGET_NAME,
    _SOURCE,
    _LIB,
    _USE,
    _USER_DATA,
):
    TARGET_ELF = builder.generateTarget(
        module.tmp(),
        _TARGET_NAME + '.elf',
    )
    _buildElf(
        _context,
        TARGET_ELF,
        _SOURCE,
        _LIB,
        _USE,
        [ 'EBOOT' ],
    )

    _context.add_group()

    TARGET_ELF_FIXUP = TARGET_ELF + '.fixup'
    _fixupImports(
        _context,
        TARGET_ELF_FIXUP,
        TARGET_ELF,
    )

    _context.add_group()

    TARGET_ELF_STRIP = TARGET_ELF + '.strip'
    _stripElf(
        _context,
        TARGET_ELF_STRIP,
        TARGET_ELF_FIXUP,
    )

    TARGET_SFO = os.path.join(
        module.tmp(),
        _TARGET_NAME,
        'PARAM.SFO',
    )
    _makeSfo(
        _context,
        TARGET_SFO,
        _USER_DATA,
    )

    _context.add_group()

    TARGET_EBOOT = os.path.join(
        _TARGET_DIR,
        _TARGET_NAME,
        'EBOOT.PBP',
    )
    _packPbp(
        _context,
        TARGET_EBOOT,
        TARGET_ELF_STRIP,
        TARGET_SFO,
    )

def prx(
    _context,
    _TARGET_DIR,
    _TARGET_NAME,
    _SOURCE,
    _LIB,
    _USE,
    _USER_DATA,
):
    TARGET_ELF = builder.generateTarget(
        module.tmp(),
        _TARGET_NAME + '.elf',
    )
    _buildElf(
        _context,
        TARGET_ELF,
        _SOURCE,
        _LIB,
        _USE,
        [ 'PRX' ],
    )

    _context.add_group()

    TARGET_ELF_FIXUP = TARGET_ELF + '.fixup'
    _fixupImports(
        _context,
        TARGET_ELF_FIXUP,
        TARGET_ELF,
    )

    _context.add_group()

    TARGET_PRX = builder.generateTarget(
        _TARGET_DIR,
        _TARGET_NAME + '.prx',
    )
    _genPrx(
        _context,
        TARGET_PRX,
        TARGET_ELF_FIXUP,
    )

def _buildElf(
    _context,
    _TARGET,
    _SOURCE,
    _LIB,
    _USE,
    _APPEND_USE = [],
):
    lib = []
    if _LIB is not None:
        lib.extend( _LIB )

    use = []
    if _USE is not None:
        use.extend( _USE )

    use.extend( _APPEND_USE )

    _context(
        features = [
            'cxx',
            'cxxprogram',
        ],
        target = _TARGET,
        source = builder.generateSource(
            _SOURCE,
            os.path.join(
                getSourceDir(),
                taf.PACKAGE_NAME,
            ),
        ),
        lib = lib,
        use = use,
    )

def _stripElf(
    _context,
    _TARGET,
    _TARGET_ELF_FIXUP,
):
    _context(
        rule = _stripElfRule,
        target = _TARGET,
        source = _TARGET_ELF_FIXUP,
    )

def _stripElfRule(
    _task,
):
    ELF_FIXUP = _task.inputs[ 0 ].abspath()
    TARGET = _task.outputs[ 0 ].abspath()

    _task.exec_command(
        '%s/bin/psp-strip %s -o %s'
        % (
            _task.env.PSPDEV,
            ELF_FIXUP,
            TARGET,
        )
    )

def _makeSfo(
    _context,
    _TARGET,
    _USER_DATA,
):
    _context(
        rule = _makeSfoRule,
        target = _TARGET,
        userData = _USER_DATA,
    )

def _makeSfoRule(
    _task,
):
    TARGET = _task.outputs[ 0 ].abspath()
    USER_DATA = _task.generator.userData

    TITLE = USER_DATA[ 'TITLE' ]

    _task.exec_command(
        '%s/bin/mksfo %s %s'
        % (
            _task.env.PSPDEV,
            TITLE,
            TARGET,
        )
    )

def _packPbp(
    _context,
    _TARGET,
    _TARGET_ELF_STRIP,
    _TARGET_SFO,
):
    _context(
        rule = _packPbpRule,
        target = _TARGET,
        source = [
            _TARGET_ELF_STRIP,
            _TARGET_SFO,
        ],
    )

def _packPbpRule(
    _task,
):
    TARGET = _task.outputs[ 0 ].abspath()
    ELF_STRIP = _task.inputs[ 0 ].abspath()
    SFO = _task.inputs[ 1 ].abspath()

    #TODO ユーザー定義データで設定できるようにする
    _task.exec_command(
        '%s/bin/pack-pbp %s %s NULL NULL NULL NULL NULL %s NULL'
        % (
            _task.env.PSPDEV,
            TARGET,
            SFO,
            ELF_STRIP,
        )
    )

def _fixupImports(
    _context,
    _TARGET,
    _TARGET_ELF,
):
    _context(
        rule = _fixupImportsRule,
        target = _TARGET,
        source = _TARGET_ELF,
    )

def _fixupImportsRule(
    _task,
):
    ELF = _task.inputs[ 0 ].abspath()
    TARGET = _task.outputs[ 0 ].abspath()

    _task.exec_command(
        '%s/bin/psp-fixup-imports %s -o %s'
        % (
            _task.env.PSPDEV,
            ELF,
            TARGET,
        )
    )

def _genPrx(
    _context,
    _TARGET,
    _TARGET_ELF_FIXUP,
):
    _context(
        rule = _genPrxRule,
        target = _TARGET,
        source = _TARGET_ELF_FIXUP,
    )

def _genPrxRule(
    _task,
):
    ELF_FIXUP = _task.inputs[ 0 ].abspath()
    TARGET = _task.outputs[ 0 ].abspath()

    _task.exec_command(
        '%s/bin/psp-prxgen %s %s'
        % (
            _task.env.PSPDEV,
            ELF_FIXUP,
            TARGET,
        )
    )
