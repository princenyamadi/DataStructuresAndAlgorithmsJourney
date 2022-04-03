from pathlib import Path
# Absolute path
print(Path.cwd())
# Relative path
print(Path.cwd().parent)


# path = Path("eccommerce")
# print(path.exists())


path = Path()
# print(path.glob('*.py'))

for file in path.glob('*.py'):
    print(file)
