from smart_repo.parser.ast_parser import ASTParser
from smart_repo.parser.models import FileInfo


def main():

    file = FileInfo(
        name="app.py",
        relative_path="app.py",
        absolute_path="src/smart_repo/app.py",
        extension=".py",
        size=0,
    )

    parser = ASTParser(file)

    parsed = parser.parse()

    print("=" * 60)
    print("IMPORTS")
    print("=" * 60)

    for imp in parsed.imports:
        print(imp)

    print()

    print("=" * 60)
    print("FUNCTIONS")
    print("=" * 60)

    for function in parsed.functions:
        print(function)

    print()

    print("=" * 60)
    print("CLASSES")
    print("=" * 60)

    if parsed.classes:
        for cls in parsed.classes:
            print(cls)
    else:
        print("No classes found.")

    print()

    print("=" * 60)
    print("CALLS")
    print("=" * 60)

    if parsed.calls:
        for call in parsed.calls:
            print(call)
    else:
        print("No function calls found.")

if __name__ == "__main__":
    main()