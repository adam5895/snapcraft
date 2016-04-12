# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2016 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import yaml


def _strip_state_constructor(loader, node):
    parameters = loader.construct_mapping(node)
    return StripState(**parameters)

yaml.add_constructor(u'!StripState', _strip_state_constructor)


class StripState(yaml.YAMLObject):
    yaml_tag = u'!StripState'

    def __init__(self, files, directories, dependency_paths=None):
        self.files = files
        self.directories = directories
        self.dependency_paths = set()

        if dependency_paths:
            self.dependency_paths = dependency_paths

    def __repr__(self):
        return ('{}(files: {}, directories: {}, dependency_paths: {})').format(
            self.__class__, self.files, self.directories,
            self.dependency_paths)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__

        return False