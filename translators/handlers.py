#
# This source file is part of appleseed.
# Visit http://appleseedhq.net/ for additional information and resources.
#
# This software is released under the MIT license.
#
# Copyright (c) 2014-2018 The appleseedhq Organization
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import bpy
import os

from ..util import image_extensions

TEXTURE_ASSET = 1


class AssetHandler(object):

    def __init__(self):
        self.__searchpaths = []

    @property
    def searchpaths(self):
        return self.__searchpaths

    def set_searchpath(self, path):
        self.__searchpaths.append(path)

    def resolve_path(self, filename, sub_texture=False):
        directory, file = os.path.split(bpy.path.abspath(filename))
        self.__searchpaths.append(directory)
        if sub_texture:
            base_filename = os.path.splitext(file)[0]
            return "{0}.tx".format(base_filename)
        else:
            return file

    @staticmethod
    def substitute_texture(parameter):
        if parameter.endswith(image_extensions):
            base_filename = os.path.splitext(parameter)[0]
            return "{0}.tx".format(base_filename)

        return parameter


class CopyAssetsAssetHandler(object):

    def __init__(self):
        pass

    @staticmethod
    def resolve_path(filename):
        raise NotImplementedError()
