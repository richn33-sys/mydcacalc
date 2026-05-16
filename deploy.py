import subprocess
import sys
import os
from datetime import datetime

os.chdir(os.path.expanduser('~/Desktop/ClaudeWork/mydcacalc'))

message = sys.argv[1] if len(sys.argv) > 1 else f"update {datetime.now().strftime('%Y-%m-%d %H:%M')}"

# Step 1 — git add, commit, push
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

print("✓ Pushed to GitHub")

# Step 2 — SSH into Hostinger and pull
print("Pulling to Hostinger...")
ssh_command = [
    'ssh', '-p', '65002', 'u877849432@145.79.4.163',
    'cd ~/domains/mydcacalc.com/public_html && git fetch origin && git reset --hard origin/main'
]

result = subprocess.run(ssh_command, capture_output=True, text=True)
if result.stdout: print(result.stdout)
if result.stderr: print(result.stderr)

if result.returncode != 0:
    print("SSH pull failed — log into Hostinger manually to deploy")
    sys.exit(1)

print("✓ Deployed to mydcacalc.com")
