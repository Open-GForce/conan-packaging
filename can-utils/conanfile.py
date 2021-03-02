from conans import ConanFile, CMake, tools

class PigpioConan(ConanFile):
    name = "can-utils"
    author = "cpp_redis"
    url = "https://github.com/linux-can/can-utils"
    description = "This repository contains some userspace utilities for Linux CAN subsystem (aka SocketCAN)"
    topics = ("CAN", "Linux")

    def source(self):
        self.run("git clone https://github.com/linux-can/can-utils")
        self.run("cd can-utils && git checkout " + self.version)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"] = "Release"
        cmake.configure(source_folder="can-utils")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.install()

    def package(self):
        cmake = self._configure_cmake()
        self.copy("*.a", "lib", "", keep_path=False)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["libcan.a"]

