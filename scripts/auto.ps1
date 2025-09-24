# Start build process
Start-Process ./install/build.bat -Wait
# Start install process
Start-Process ./install/install.bat -Wait
# set PATH
Start-Process ./install/set_path_admin.bat -Wait -Verb RunAs
# Clean up
Start-Process ./install/clean.bat -Wait
# Finish
Write-Host "Installation complete. Please restart your terminal, IDE or Computer to apply changes."
# Pause to view any messages
Pause