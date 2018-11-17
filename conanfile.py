#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile, tools


class RxcppConan(ConanFile):
    name = "rxcpp"
    version = "4.1.0"
    url = "https://github.com/bincrafters/conan-rxcpp"
    homepage = "https://github.com/ReactiveX/RxCpp"
    author = "Bincrafters <bincrafters@gmail.com>"
    description = "Library for composing operations on streams of asynchronous events."
    license = "Apache-2.0"
    topics = ("conan", "rxcpp", "reactivex", "algorithms", "values-distributed-in-time")
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/Reactive-Extensions/RxCpp"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_folder = "RxCpp-" + self.version
        os.rename(extracted_folder, self._source_subfolder)

    def package(self):
        self.copy("license.md", dst="licenses", src=self._source_subfolder)
        header_dir = os.path.join(self._source_subfolder, "Rx", "v2", "src")
        self.copy(pattern="*", dst="include", src=header_dir)

    def package_id(self):
        self.info.header_only()
