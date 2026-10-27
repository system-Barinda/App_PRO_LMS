# App_PRO_LMS

## Run a Python file on Windows

Open this repository folder in VS Code. The workspace is configured to use the
local `.venv` virtual environment.

Create the environment once from the repository root:

```powershell
py -3 -m venv .venv
```

Run a file directly, without activating the environment:

```powershell
.\.venv\Scripts\python.exe assignment_24rp08563\student_results.py
```

The project currently uses only Python's standard library, so no packages need
to be installed. To run another exercise, replace the file path with its path
from the repository root. For example:

```powershell
.\.venv\Scripts\python.exe assignment_24rp08563\student_registration.py
```

That registration exercise prompts for input in the terminal.
