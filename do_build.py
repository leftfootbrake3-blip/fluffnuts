import subprocess, sys, os

os.chdir(r'D:\App DEVELOPMENT\FLUFFNUTS PRO')

# Clean old build artifacts
import shutil
for d in ['dist', 'build']:
    if os.path.exists(d):
        shutil.rmtree(d)

result = subprocess.run(
    [sys.executable, 'setup.py', 'build'],
    capture_output=True, text=True, timeout=300
)

with open(r'D:\App DEVELOPMENT\FLUFFNUTS PRO\build_log.txt', 'w', encoding='utf-8') as f:
    f.write(f"RETURN CODE: {result.returncode}\n\n")
    f.write(f"=== STDOUT ===\n{result.stdout}\n\n")
    f.write(f"=== STDERR ===\n{result.stderr}\n\n")
    
    # Check result
    exe_path = r'D:\App DEVELOPMENT\FLUFFNUTS PRO\dist\FluffnutsPro.exe'
    if os.path.exists(exe_path):
        size = os.path.getsize(exe_path)
        f.write(f"EXE EXISTS: {exe_path} ({size:,} bytes)\n")
        # Count all files in dist
        total = 0
        for root, dirs, files in os.walk('dist'):
            for fn in files:
                fp = os.path.join(root, fn)
                total += os.path.getsize(fp)
        f.write(f"DIST FOLDER TOTAL SIZE: {total:,} bytes\n")
    else:
        f.write("EXE NOT FOUND!\n")
