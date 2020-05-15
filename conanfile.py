# -*- coding: utf-8 -*-
from conans import ConanFile, Meson, tools
import os
import shutil


class curlasioConan(ConanFile):
    name = "curlasio"
    version = "0.1.1"
    sha1_revision="125091eb731dcaf0495f1a62ba4f36aa1bbfdf38"
    description = "Seamlessly integrate libcurl with Boost.Asi"
    topics = ("boost", "asio", "curl", "libcurl")
    url = "https://github.com/museghost/curl-asio"
    homepage = "https://github.com/mologie/curl-asio"
    author = "mologie"
    # license = "BSD 3-Clause"
    exports = ["CHANGES", "COPYING"]
    generators = "pkg_config"
    exports_sources = ["src/*", "examples/*", "include/*", "meson.build", "meson_options.txt"]
    
    # Options may need to change depending on the packaged library.
    # Default options can be specified as a dictionary only for Conan version >= 1.8.
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [False, True],
        "fPIC": [True, False],
        "with_example": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "with_example": True,
    }

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def build_requirements(self):
        pass
        
    def requirements(self):
        self.requires("OpenSSL/1.0.2s@conan/stable")
        self.requires("boost/1.71.0@conan/stable")
        self.requires("libcurl/7.68.0@aphrodite/testing")
        
    #def configure(self):
    #    self.options["asio"].with_openssl = True

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def _configure_meson(self):
        meson = Meson(self)
        meson.configure(
            defs={
                "with-example": self.options.with_example,
                "cpp_std": "c++17"
            },
            build_folder=self.build_subfolder)

        return meson

    def build(self):
        meson = self._configure_meson()
        meson.build()
        meson.install()

    def package(self):
        #self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy(pattern="COPYING", dst="licenses")
        #self.copy("*.h", dst="include", src=os.path.join(self.source_subfolder, "include"))
        self.copy("*.h", dst="include", src="include")
        self.copy("*.ipp", dst="include", src="include")
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.inl", dst="include", src="include")
        
        # TODO: think of below dll copying for Windows
        # self.copy("*.dll", dst="bin", keep_path=False)
        if self.options.shared:
            self.copy("*.so*", dst="lib", keep_path=False)
            self.copy("*.dylib*", dst="lib", keep_path=False)
        else:
            self.copy("*.a", dst="lib", keep_path=False)
        
        # TODO: 아래는 windows 에서 필요한데 실제로 msvc 에서 컴파일 해보고 정하자
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
    #    self.cpp_info.libs.reverse()
