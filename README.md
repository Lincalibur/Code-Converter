# Code-Converter
A Py script to Copy the file structure of a C# project and convert it to Python.

## Overview
This project aims to create a tool to convert C# projects to Python projects. The conversion is split into two main steps: copying the project structure and converting the logic from C# to Python.

## Project Structure
```
project_converter/
│
├── scripts/
│   ├── copy_project_structure.py
│   ├── convert_logic.py
│   └── translate_code.py
│
├── projects/
│   ├── csharp_project/
│   └── python_project-Py/
│
├── tests/
│   └── test_project_converter.py
│
├── docs/
│   └── README.md
│
└── guide.txt
```

## Usage
1. **Copy Project Structure**: Run `copy_project_structure.py` to copy the C# project structure and create a guide file.
    ```sh
    python scripts/copy_project_structure.py
    ```

2. **Convert Logic**: Run `convert_logic.py` to convert the logic from C# to Python using the guide file.
    ```sh
    python scripts/convert_logic.py
    ```

3. **Translation Rules**: Modify `translate_code.py` to add detailed translation rules for converting C# constructs to Python.

## Testing
Run the unit tests to ensure the scripts work correctly.
```sh
python -m unittest discover -s tests
```

## Contributing
Feel free to submit issues or pull requests to improve the project.

## License
This project is licensed under the MIT License.
