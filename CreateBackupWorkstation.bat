@echo off

rem For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
rem For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)

For /f %%a in ('date /t') do (set mydate=%%a)

For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)

set mydir="%mydate%_%mytime%"

mkdir %mydir%

copy *.pas %mydir%
copy *.bat %mydir%
copy *.exe %mydir% 
copy *.conf %mydir%
copy *.py %mydir%
