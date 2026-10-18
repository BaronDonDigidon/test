from pathlib import Path

script_dir = Path(__file__).parent
path = script_dir / "output_file.txt"

with path.open("r") as file:
    for line in file:
        print(line)