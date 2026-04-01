import sqlite3, os
db = os.path.join(os.environ['APPDATA'], 'FluffnutsPro', 'fluffnuts.db')
with open(r'D:\App DEVELOPMENT\FLUFFNUTS PRO\db_check.txt', 'w') as f:
    f.write(f"DB path: {db}\n")
    f.write(f"Exists: {os.path.exists(db)}\n")
    if os.path.exists(db):
        c = sqlite3.connect(db)
        rows = c.execute("SELECT key, substr(value,1,15) FROM settings").fetchall()
        for r in rows:
            f.write(f"  {r[0]} = {r[1]}...\n")
        c.close()
