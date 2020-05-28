cmake_minimum_required(VERSION 3.5)
project(ISAE ${VERSION_SHORT})

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt5 5.5 COMPONENTS Core Gui Widgets REQUIRED)
if(WIN32)
    find_package(Qt5 5.5 COMPONENTS AxContainer REQUIRED)
endif()
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(ISAE_SRCS
        main.cpp
        mainwindow.cpp
        mainwindow.h
        )
add_executable(ISAE WIN32 ${ISAE_SRCS})
target_include_directories(ISAE PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/Librarys/Qt-Advanced-Docking-System/src")
target_link_libraries(ISAE PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
if(WIN32)
    target_link_libraries(ISAE PUBLIC Qt5::AxContainer)
endif()
add_subdirectory(Librarys)
target_link_libraries(ISAE PRIVATE qtadvanceddocking)
#if(BUILD_STATIC)
#    target_compile_definitions(ISAE PRIVATE ADS_STATIC)
#endif()

