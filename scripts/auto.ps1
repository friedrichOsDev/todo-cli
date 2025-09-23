# Start build process
Start-Process ./build.bat -Wait
# Start install process
Start-Process ./install.bat -Wait
# set PATH
Start-Process ./set_path_admin.bat -Wait -Verb RunAs