from conan import ConanFile
from conan.tools.cmake import cmake_layout

class TestConanProject(ConanFile):
    name = "test_conan"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    # Cmakedeps создаст файлы, чтобы команда find_package() в cmake увидела библиотеку
    # проблема в том , что по стандарту cmake не заглядывает в conan , а ищет все в стандартных библиотеках
    # и поэтому в cmakedeps прописывается путь до библиотеки conan
    # CmakeToolchain создает файл настройки компилятора , чтобы cmake и conan синхронизировались

    def requirements(self):
        # Подключаем библиотеку fmt
        self.requires("fmt/10.1.1")

    def layout(self):
        cmake_layout(self)
        #использовать структуру cmake , в которой файлы будут лежать в build-e 