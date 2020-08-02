cmake_minimum_required(VERSION 3.1.0 FATAL_ERROR)
# CMP0000: Call the cmake_minimum_required() command at the beginning of the top-level
# CMakeLists.txt file even before calling the project() command.
# The cmake_minimum_required(VERSION) command implicitly invokes the cmake_policy(VERSION)
# command to specify that the current project code is written for the given range of CMake
# versions.
project(qtermwidget)
find_package(Qt5Widgets "${QT_MINIMUM_VERSION}" REQUIRED)
set(QTERMWIDGET_LIBRARY_NAME qtermwidget5)
set(SRCS
        BlockArray.cpp
        ColorScheme.cpp
        Emulation.cpp
        Filter.cpp
        History.cpp
        HistorySearch.cpp
        KeyboardTranslator.cpp
        konsole_wcwidth.cpp
        kprocess.cpp
        kpty.cpp
        kptydevice.cpp
        kptyprocess.cpp
        Pty.cpp
        qtermwidget.cpp
        Screen.cpp
        ScreenWindow.cpp
        SearchBar.cpp
        Session.cpp
        ShellCommand.cpp
        TerminalCharacterDecoder.cpp
        TerminalDisplay.cpp
        tools.cpp
        Vt102Emulation.cpp
        )

# Only the Headers that need to be moc'd go here
set(HDRS
        Emulation.h
        Filter.h
        HistorySearch.h
        kprocess.h
        kptydevice.h
        kptyprocess.h
        Pty.h
        qtermwidget.h
        ScreenWindow.h
        SearchBar.h
        Session.h
        TerminalDisplay.h
        Vt102Emulation.h
        )

set(UI
        SearchBar.ui
        )

# for distribution
set(HDRS_DISTRIB
        qtermwidget.h
        Emulation.h
        Filter.h
        )
add_library(${QTERMWIDGET_LIBRARY_NAME} SHARED ${SRCS} ${HDRS} ${UI} ${QTERMWIDGET_QM})
target_link_libraries(${QTERMWIDGET_LIBRARY_NAME} Qt5::Widgets)
set_target_properties(${QTERMWIDGET_LIBRARY_NAME} PROPERTIES
        AUTOMOC ON
        AUTORCC ON
        AUTOUIC ON
        CXX_STANDARD 17
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS OFF
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
        )