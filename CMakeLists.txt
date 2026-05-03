cmake_minimum_required(VERSION 3.14)
project(sqlite3_universal LANGUAGES C)

# Создаем разделяемую библиотеку (SHARED)
add_library(sqlite3 SHARED sqlite3.c)

# --- Настройки для Linux (GCC) ---
if(UNIX AND NOT APPLE)
    target_link_libraries(sqlite3 PRIVATE dl pthread)
    # Позволяет запускать программу без export LD_LIBRARY_PATH
    set_target_properties(sqlite3 PROPERTIES 
        INSTALL_RPATH "$ORIGIN"
        BUILD_WITH_INSTALL_RPATH TRUE)
endif()

# --- Настройки для Windows (MSVC) ---
if(MSVC)
    # Автоматически создает .lib файл (файл импорта) для .dll
    set_target_properties(sqlite3 PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

