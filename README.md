This simple script aims to notify me when Claude code has finished working on its tasks.
Notification is done by playing a sound and by sending a command on my Arduino Pro Micro.

## Installation

Linux:

```bash
virtualenv venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
virtualenv venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Usage

Use the following commands to test locally:

```bash
python main.py aiDone # to notify when AI is done
python main.py aiQuestion # to notify when AI is requesting something (permission, etc.)
```

## Configuration of Claude hooks

Go to settings.json and add the following:

```json
{
  "permissions": {
    "allow": [
      "Bash(path/to/your/.venv/bin/python)"
    ]
  },
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "path/to/your/.venv/bin/python path/to/this/project/main.py aiDone"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "path/to/your/.venv/bin/python path/to/this/project/main.py aiQuestion"
          }
        ]
      }
    ]
  }
}


```