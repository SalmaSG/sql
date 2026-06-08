"""File handling concepts demo for Python."""

from pathlib import Path


DEMO_FILE = Path("demofile3.txt")


def create_file():
    """Create a new file and write initial content."""
    DEMO_FILE.write_text(
        "First line\nSecond line\nThird line\n",
        encoding="utf-8",
    )
    print(f"Created {DEMO_FILE}")


def read_file():
    """Read the file using read()."""
    print("\n--- read() ---")
    content = DEMO_FILE.read_text(encoding="utf-8")
    print(content)


def read_lines():
    """Read the file line by line using splitlines()."""
    print("\n--- splitlines() ---")
    lines = DEMO_FILE.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines, start=1):
        print(f"{index}: {line}")


def append_file():
    """Append new content to the file."""
    with DEMO_FILE.open("a", encoding="utf-8") as file:
        file.write("Appended line\n")
    print("\nAppended a new line")


def overwrite_file():
    """Overwrite the file with new content."""
    with DEMO_FILE.open("w", encoding="utf-8") as file:
        file.write("Overwritten content\n")
        file.write("Another line\n")
    print("\nOverwrote the file")


def handle_missing_file():
    """Demonstrate handling a missing file safely."""
    missing_file = Path("missing_demo.txt")

    try:
        missing_file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"\n{missing_file} was not found. Handling the error safely.")


def show_file_exists():
    """Show whether the file exists."""
    print(f"\nFile exists? {DEMO_FILE.exists()}")


def main():
    create_file()
    show_file_exists()
    read_file()
    read_lines()
    append_file()
    read_file()
    overwrite_file()
    read_file()
    handle_missing_file()


if __name__ == "__main__":
    main()
