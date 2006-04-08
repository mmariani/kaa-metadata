# -*- coding: iso-8859-1 -*-
# -----------------------------------------------------------------------------
# bmpinfo.py - bmp file parsing
# -----------------------------------------------------------------------------
# $Id$
#
# -----------------------------------------------------------------------------
# kaa-Metadata - Media Metadata for Python
# Copyright (C) 2003-2005 Thomas Schueppel, Dirk Meyer
#
# First Edition: Dirk Meyer <dmeyer@tzi.de>
# Maintainer:    Dirk Meyer <dmeyer@tzi.de>
#
# Please see the file AUTHORS for a complete list of authors.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MER-
# CHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# -----------------------------------------------------------------------------

# python imports
import struct
import logging

# kaa imports
from kaa.metadata import mediainfo
from kaa.metadata import factory

import core

# get logging object
log = logging.getLogger('metadata')

# interesting file format info:
# http://www.fortunecity.com/skyscraper/windows/364/bmpffrmt.html

class BMPInfo(core.ImageInfo):

    def __init__(self,file):
        core.ImageInfo.__init__(self)
        self.mime = 'image/bmp'
        self.type = 'windows bitmap image'

        (bfType, bfSize, bfZero, bfOffset, biSize, self.width, self.height) = \
                 struct.unpack('<2sIIIIII', file.read(26))
        # seek to the end to test length
        file.seek(0, 2)

        if bfType != 'BM' or bfSize != file.tell():
            raise mediainfo.KaaMetadataParseError()


factory.register( 'image/bmp', ('bmp', ), mediainfo.TYPE_IMAGE, BMPInfo )