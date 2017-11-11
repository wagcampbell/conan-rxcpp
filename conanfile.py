#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class RxcppConan(ConanFile):
    name = "rxcpp"
    version = "4.0.0"
    url = "https://github.com/bincrafters/conan-rxcpp"
    description = "Library for composing operations on streams of asynchronous events."
    license = "https://github.com/Reactive-Extensions/RxCpp/blob/master/license.md"
    root = "RxCpp-" + version

    def source(self):
        source_url = "https://github.com/Reactive-Extensions/RxCpp"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))

    def package(self):
        header_dir = os.path.join(self.root, "Rx", "v2", "src")
        self.copy(pattern="*", dst="include", src=header_dir)

    def package_id(self):
        self.info.header_only()
