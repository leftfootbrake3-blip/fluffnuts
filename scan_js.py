import re

with open(r'D:\App DEVELOPMENT\FLUFFNUTS PRO\FluffnutsPro.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

results = []
results.append(f"Total lines: {len(lines)}")
results.append("\n=== Searching for unescaped apostrophes in JS single-quoted strings ===")

issues_found = 0
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith('#'):
        continue
    contractions = ["n't", "'s ", "'t ", "'re ", "'ve ", "'ll ", "'m ", "'d "]
    for c in contractions:
        if c in line:
            js_indicators = ['function', 'const ', 'let ', 'var ', 'document.', 'addEventListener',
                           'textContent', 'innerHTML', 'alert(', 'addAIMsg(', 'getElementById',
                           'classList', 'querySelector', 'onclick', 'fetch(']
            if any(ind in line for ind in js_indicators):
                results.append(f"LINE {i}: {line.rstrip()[:300]}")
                issues_found += 1
                break

results.append(f"\nTotal potential issues: {issues_found}")

with open(r'D:\App DEVELOPMENT\FLUFFNUTS PRO\scan_output.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))
