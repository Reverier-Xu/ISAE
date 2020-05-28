# Install script for directory: /mnt/Data/ISAE/Qt-Advanced-Docking-System/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xheadersx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/linux/FloatingWidgetTitleBar.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/ads_globals.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockAreaTabBar.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockAreaTitleBar.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockAreaTitleBar_p.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockAreaWidget.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockContainerWidget.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockManager.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockOverlay.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockSplitter.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockWidget.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockWidgetTab.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockingStateReader.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/ElidingLabel.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/FloatingDockContainer.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/FloatingDragPreview.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/IconProvider.h"
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/DockComponentsFactory.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlicensex" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/license" TYPE FILE FILES
    "/mnt/Data/ISAE/LICENSE"
    "/mnt/Data/ISAE/gnu-lgpl-v2.1.md"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so.3.4.1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so.3.4.1")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so.3.4.1"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/mnt/Data/ISAE/cmake-build-debug/x64/lib/libqtadvanceddocking.so.3.4.1")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so.3.4.1" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so.3.4.1")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so.3.4.1")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/mnt/Data/ISAE/cmake-build-debug/x64/lib/libqtadvanceddocking.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libqtadvanceddocking.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/qtadvanceddocking/adsTargets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/qtadvanceddocking/adsTargets.cmake"
         "/mnt/Data/ISAE/cmake-build-debug/Qt-Advanced-Docking-System/src/CMakeFiles/Export/lib/cmake/qtadvanceddocking/adsTargets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/qtadvanceddocking/adsTargets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/qtadvanceddocking/adsTargets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/qtadvanceddocking" TYPE FILE FILES "/mnt/Data/ISAE/cmake-build-debug/Qt-Advanced-Docking-System/src/CMakeFiles/Export/lib/cmake/qtadvanceddocking/adsTargets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/qtadvanceddocking" TYPE FILE FILES "/mnt/Data/ISAE/cmake-build-debug/Qt-Advanced-Docking-System/src/CMakeFiles/Export/lib/cmake/qtadvanceddocking/adsTargets-debug.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/qtadvanceddocking" TYPE FILE FILES
    "/mnt/Data/ISAE/Qt-Advanced-Docking-System/src/qtadvanceddockingConfig.cmake"
    "/mnt/Data/ISAE/cmake-build-debug/Qt-Advanced-Docking-System/src/qtadvanceddockingConfigVersion.cmake"
    )
endif()

