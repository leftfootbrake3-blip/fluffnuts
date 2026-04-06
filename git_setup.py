import subprocess, os
os.chdir(r"D:\App DEVELOPMENT\FLUFFNUTS PRO")
git = r"C:\Program Files\Git\cmd\git.exe"
results = []

def run(cmd, label):
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = f"=== {label} ===\nOUT: {r.stdout.strip()}\nERR: {r.stderr.strip()}\nRC: {r.returncode}\n"
    results.append(out)
    return r

# Check existing history
run([git, "log", "--oneline", "-10"], "LOG")

# Remove tracked files that should be gitignored
run([git, "rm", "-r", "--cached", "dist/"], "RM DIST")
run([git, "rm", "-r", "--cached", "FluffnutsPro.egg-info/"], "RM EGG")
run([git, "rm", "-r", "--cached", "Fluffnuts_Pro.egg-info/"], "RM EGG2")
run([git, "rm", "--cached", "build_stdout.txt"], "RM BUILD_STDOUT")

# Remove other junk that was tracked
for f in ["run_err2.txt", "run_out2.txt", "git_setup.py",
          "git_setup_log.txt"]:
    run([git, "rm", "--cached", "-f", f], f"RM {f}")

# Re-add everything (gitignore will filter)
run([git, "add", "."], "ADD ALL")
run([git, "status"], "FINAL STATUS")

with open("git_setup_log.txt", "w") as f:
    f.write("\n".join(results))
