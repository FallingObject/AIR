# imports

import os
import json
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

# Path to the settings file && CONFIG FILE
path = Path(__file__).parent.parent.absolute()
CONFIG = json.load(open(os.path.join(path,'config.json')))


