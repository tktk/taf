# -*- coding: utf-8 -*-

from . import *

import os.path

def configure(
    _context,
):
    PSPDEV = _getPspdev( _context )
    _context.env.PSPDEV = PSPDEV

    _context.env.CXX = _generateCxx(
        _context,
        PSPDEV,
    )
    _context.env.LINK_CXX = _generateLinkCxx(
        _context,
        PSPDEV,
    )
    _context.env.INCLUDES = _generateIncludes(
        _context,
        PSPDEV,
    )
    _context.env.LIBPATH = _generateLibpath(
        _context,
        PSPDEV,
    )
    _context.env.CXXFLAGS = _generateCxxflags( _context )
    _context.env.DEFINES = _generateDefines( _context )
    _context.env.LINKFLAGS = _generateLinkflags( _context )

    _context.env.LINKFLAGS_PRX = _generatePrxLinkflags(
        _context,
        PSPDEV,
    )

def _getPspdev(
    _context,
):
    pspdev = _context.options.pspdev

    _context.msg(
        'pspdev',
        pspdev,
    )

    return pspdev

def _generateCxx(
    _context,
    _PSPDEV,
):
    cxx = _PSPDEV + '/bin/psp-g++'

    _context.msg(
        'cxx',
        cxx,
    )

    return cxx

def _generateLinkCxx(
    _context,
    _PSPDEV,
):
    linkcxx = _PSPDEV + '/bin/psp-gcc'

    _context.msg(
        'linkcxx',
        linkcxx,
    )

    return linkcxx

def _generateIncludes(
    _context,
    _PSPDEV,
):
    includes = [
        _PSPDEV + '/psp/sdk/include',
        _PSPDEV + '/include',
        _PSPDEV + '/psp/include',
    ]

    includes.append( getHeaderDir() )

    includeOption = _context.options.include
    if includeOption is None:
        includeOption = getIncludes()

    if includeOption is not None:
        includes.extend( includeOption )

    includes = _generateAbspathList( includes )

    _context.msg(
        'includes',
        includes,
    )

    return includes

def _generateLibpath(
    _context,
    _PSPDEV,
):
    libpath = [
        _PSPDEV + '/psp/sdk/lib',
        _PSPDEV + '/lib',
    ]

    _context.msg(
        'libpath',
        libpath,
    )

    return libpath

def _generateCxxflags(
    _context,
):
    cxxflags = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        cxxflags = getCxxflagsDebug()
    elif BUILD == 'release':
        cxxflags = getCxxflagsRelease()

    _context.msg(
        'cxxflags',
        cxxflags,
    )

    return cxxflags

def _generateDefines(
    _context,
):
    defines = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        defines = getDefinesDebug()
    elif BUILD == 'release':
        defines = getDefinesRelease()

    _context.msg(
        'defines',
        defines,
    )

    return defines

def _generateLinkflags(
    _context,
):
    linkflags = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        linkflags = getLinkflagsDebug()
    elif BUILD == 'release':
        linkflags = getLinkflagsRelease()

    _context.msg(
        'linkflags',
        linkflags,
    )

    return linkflags

def _generateLinkflags(
    _context,
):
    linkflags = None

    BUILD = _context.env.taf[ 'BUILD' ]
    if BUILD == 'debug':
        linkflags = getLinkflagsDebug()
    elif BUILD == 'release':
        linkflags = getLinkflagsRelease()

    _context.msg(
        'linkflags',
        linkflags,
    )

    return linkflags

def _generatePrxLinkflags(
    _context,
    _PSPDEV,
):
    linkflags = getLinkflagsPrx()

    linkflags.append( '-Wl,-q,-T' + _PSPDEV + '/psp/sdk/lib/linkfile.prx' )

    _context.msg(
        'prx linkflags',
        linkflags,
    )

    return linkflags

def _generateAbspathList(
    _PATH_LIST,
):
    abspathList = []

    for PATH in _PATH_LIST:
        abspathList.append( os.path.abspath( PATH ) )

    return abspathList
