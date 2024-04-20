from pathlib import Path
import sqlite3
import sys

class DB:
    @staticmethod
    def loadSqlScript(filepath: str) -> str:
        content = ""
        try:
            with open(filepath, 'r', encoding = 'utf-8') as fh:
                content = fh.read()
        except FileNotFoundError:
            print(f"Failed to read '{filepath}' file.")
            sys.exit(-1)
        return content
    
    @staticmethod
    def initialize() -> None:
        DB_FILEPATH1 = Path('./setup.sql')
        script = DB.loadSqlScript(DB_FILEPATH1)
        DB_FILEPATH2 = Path('./library.db')
        DB_CONN = sqlite3.connect(DB_FILEPATH2)
        cursor = DB_CONN.cursor()
        cursor.executescript(script)
        cursor.close()

if __name__ == "__main__":
    app = DB.initialize()