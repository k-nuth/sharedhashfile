# Copyright (c) 2016-2023 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import os
from conan import ConanFile
from conan.tools.build.cppstd import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy

required_conan_version = ">=2.0"

class SharedHashFileConan(ConanFile):
    name = "sharedhashfile"
    license = "http://www.boost.org/users/license.html"
    url = "https://github.com/k-nuth/sharedhashfile"
    settings = "os", "compiler", "build_type", "arch"

    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    exports_sources = "src/*", "CMakeLists.txt"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        # tc.variables["CMAKE_VERBOSE_MAKEFILE"] = True
        tc.generate()
        cmake_layout(self)


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["sharedhashfile"]
        # if self.package_folder:
        #     self.env_info.CPATH = os.path.join(self.package_folder, "include")
        #     self.env_info.C_INCLUDE_PATH = os.path.join(self.package_folder, "include")
        #     self.env_info.CPLUS_INCLUDE_PATH = os.path.join(self.package_folder, "include")
