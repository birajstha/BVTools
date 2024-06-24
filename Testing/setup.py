from cx_Freeze import setup, Executable

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

include_files = []
for req in requirements:
    if req.startswith('file:'):
        path = req.replace('file:', '').strip()
        include_files.append(path)
include_files.append("settings.txt")
include_files.append("ReadMe.txt")

setup(
    name="BirajTools",
    version="1.0.0",
    options={"build_exe": {
        "include_files": include_files,
        }
    },
    description="Made For BrainVision Test Automation",
    author="Biraj Shrestha",
    executables=[Executable("BirajTools.py", icon="BTools.ico")]
)