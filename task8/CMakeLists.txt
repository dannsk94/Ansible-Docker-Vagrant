cmake_minimum_required(VERSION 3.15)
project(test_conan CXX)
#CXX это С++
# Позволяет CMake увидеть пакеты, которые скачал Conan
find_package(fmt CONFIG REQUIRED)
#CONFIG: заставляет CMake искать специальный файл конфигурации (обычно это fmtConfig.cmake), который Conan генерирует автоматически.
#REQUIRED: если библиотека не найдена, сборка прервется с ошибкой.
add_executable(test_conan main.cpp)

# добавляем fmt библиотеку к нашему файлу test_conan
target_link_libraries(test_conan fmt::fmt)
# За счет указания fmt::fmt не нужно будет указывать путь к хэдеру .h fmt в с++ программе
