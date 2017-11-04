from conans import ConanFile, tools
import os

class RxcppConan(ConanFile):
    name = "rxcpp"
    version = "4.0.0"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url = "https://github.com/bincrafters/conan-rxcpp"
    description = "Library for composing operations on streams of asynchronous events."
    license = "https://github.com/Reactive-Extensions/RxCpp/blob/master/license.md"
    root = name + "-" + version
    #use static org/channel for libs in conan-center
    #use dynamic org/channel for libs in bincrafters
    
    def source(self):
        source_url = "https://github.com/Reactive-Extensions/RxCpp"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*", dst="include", src="include")
        self.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        tools.collect_libs(self)
