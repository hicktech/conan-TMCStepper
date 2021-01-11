from conans import ConanFile, tools


class ParticlePackage(ConanFile):
    name = 'TMCStepper'
    version = 'v0.5.2'
    url = 'https://github.com/hicktech/conan-TMCStepper'
    repo_url = 'https://github.com/teemuatlut/TMCStepper.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy("*.c*", dst="src", src='src', keep_path=False)
        self.copy("*.h*", dst="include", src='src')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')
        tools.patch(patch_file=f"../patch/0001-implement-transfer16.patch")
        tools.patch(patch_file=f"../patch/0001-undefine-conflicts.patch")

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
        self.cpp_info.includedirs = ['include', 'include/source']
