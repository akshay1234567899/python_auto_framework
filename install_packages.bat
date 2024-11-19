@echo off
echo Installing required Python packages...

pip install pytest
pip install selenium
pip install pytest-html
pip install pytest-xdist
pip install openpyxl
pip install allure-pytest

echo All packages have been installed successfully.
pause
