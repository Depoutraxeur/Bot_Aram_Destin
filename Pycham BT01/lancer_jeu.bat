@echo off
title Python Trainer - Lancement (Python direct)

:: === Taille du terminal ===
:: Ajuste les valeurs si tu veux plus large / plus haut
mode con: cols=180 lines=50

:: === Agrandissement de la fenêtre ===
:: Met la fenêtre en "agrandie" (pas plein écran, mais grande)
powershell -command "& {
    $hwnd = (Get-Process -Id $PID).MainWindowHandle
    Add-Type -Name Win -Namespace Console -MemberDefinition '[DllImport(\"user32.dll\")] public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);'
    [Console.Win]::ShowWindowAsync($hwnd, 3)
}"

:: === Se placer dans le dossier où se trouve ce .bat ===
cd /d "%~dp0"

:: === Chemin complet vers ton python.exe (venv PyCharm) ===
set "PY_EXE=C:/Users/Steve/PycharmProjects/PythonProject/.venv/Scripts/python.exe"

echo -----------------------------------------------
echo Dossier courant : %CD%
echo Utilisation de l'interprete Python :
echo   %PY_EXE%
echo -----------------------------------------------
echo.

:: === Vérification du fichier python.exe ===
if not exist "%PY_EXE%" (
    echo [ERREUR] python.exe introuvable :
    echo   %PY_EXE%
    echo.
    echo Verifie le chemin dans :
    echo   PyCharm > Settings > Python Interpreter
    echo.
    pause
    exit /b 1
)

:: === Lancement du jeu ===
echo Lancement du jeu...
echo.
"%PY_EXE%" BT01.py

echo.
echo -----------------------------------------------
echo Jeu termine.
echo -----------------------------------------------
pause
