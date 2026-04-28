import subprocess
import sys
import os
from datetime import datetime

os.chdir(os.path.expanduser('~/Desktop/ClaudeWork/mydcacalc'))

message = sys.argv[1] if len(sys.argv) > 1 else f"update {datetime.now().strftime('%Y-%m-%d %H:%M')}"

commands = [
    ['git', 'add', '.'],
    ['git', 'commit', '-m', message],
    ['git', 'push'],
]

for cmd in commands:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout: print(result.stdout)
    if result.stderr: print(result.stderr)
    if result.returncode != 0 and 'nothing to commit' not in result.stderr:
        print(f"Failed at: {' '.join(cmd)}")
        sys.exit(1)

print("Deployed successfully to mydcacalc.com")
