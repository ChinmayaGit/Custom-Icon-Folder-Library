@echo off
setlocal

set "rootDirectory=D:\0Tools\New"
set "commandScript=D:\0Tools\New\icon_convert.bat"

for /D %%G in ("%rootDirectory%\*") do (
    echo Processing folder: %%G
    pushd "%%G"
    call "%commandScript%"
    popd
)

endlocal