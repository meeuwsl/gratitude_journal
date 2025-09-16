## Initial behaviour (first run)

- **How to run**: `python main.py`
- **Note on encoding (Windows/PowerShell)**: The app prints emojis. If you see a UnicodeEncodeError, run with UTF-8: `$env:PYTHONIOENCODING='utf-8'; python main.py`.

### What the program displays on start
```
**********🙏 WELCOME TO GRATITUDE JOURNAL 🙏**********
Type:
1. To enter a new entry
2. To view all the entries
3. Search entries by date
4. Aanalyze journal
5. Check streak🔥
6. To exit

Enter your choice:
```

### Tried commands (first session)
- **Input**: `2` then `6`
- **Observed output**:
```
***************🥰 I AM GRATEFUL FOR 🥰***************
2025-09-16 15:55:00 || Today's AI workshop

Enter your choice: Thankyou, Have a good day!🤍
```
- **Effect**:
  - `2` reads and prints all entries from `entries.txt`.
  - `6` exits and prints a goodbye message.

### Files affected/used
- **Reads/Writes**: `entries.txt`
- **No code changes** were made during this run.
