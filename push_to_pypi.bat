cd dist
del *.* /F /Q
cd ..

python -m build
python -m twine upload dist/*
PAUSE
