#!/usr/bin/env python3
import json
import platform
import socket
import sys
from datetime import datetime, timezone

print(json.dumps({
    "hostname": socket.gethostname(),
    "arch": platform.machine(),
    "python_version": sys.version,
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
}, indent=2))
