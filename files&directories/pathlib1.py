from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin/apple
# Relative path
path = Path()
# __________
for file in path.glob('*.*'):
    print(file)
for file in path.glob('*.py'):
    print(file)
for file in path.glob('*.xls'):
    print(file)
# __________
path = Path("classes")
if path.exists():
    print(path.exists())
    path.rmdir()
else:
    print(path.exists())
    path.mkdir()
    print(path.exists())
    path.rmdir()
# pypi.org for pakages to access by the community
