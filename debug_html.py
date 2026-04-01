import urllib.request
import sys

with open(r'D:\App DEVELOPMENT\FLUFFNUTS PRO\debug_output.txt', 'w', encoding='utf-8') as f:
    try:
        html = urllib.request.urlopen('http://localhost:5127/').read().decode()
        lines = html.split('\n')
        f.write(f"Total lines in served HTML: {len(lines)}\n")
        f.write(f"Total chars: {len(html)}\n\n")
        start = max(0, 550)
        end = min(len(lines), 575)
        f.write(f"Showing lines {start+1} to {end}:\n")
        for i in range(start, end):
            f.write(f"LINE {i+1}: {lines[i][:400]}\n")
        f.write("\n--- Searching for potential apostrophe issues ---\n")
        for i, line in enumerate(lines):
            low = line.lower()
            if any(w in low for w in ["don't", "can't", "won't", "it's", "that's", "let's", "doesn't", "isn't", "aren't"]):
                f.write(f"LINE {i+1}: {line[:400]}\n")
        f.write("\n--- Lines around any single-quote followed by s or t ---\n")
        for i, line in enumerate(lines):
            if "'s " in line or "'t " in line or "'s)" in line or "'t)" in line:
                f.write(f"LINE {i+1}: {line[:400]}\n")
    except Exception as e:
        f.write(f"Error: {e}\n")
