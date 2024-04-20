-- Create table Books, Borrows, Members

CREATE TABLE IF NOT EXISTS Books (
	book_id INTEGER PRIMARY KEY AUTOINCREMENT,
	book_name TEXT,
	book_author TEXT,
	book_page TEXT,
	book_language TEXT,
	book_status INTEGER DEFAULT (0)
);

CREATE TABLE IF NOT EXISTS Borrows (
	borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
	bbook_id TEXT,
	bmember_id TEXT
);

CREATE TABLE IF NOT EXISTS Members (
	member_id INTEGER PRIMARY KEY AUTOINCREMENT,
	member_name TEXT,
	member_phone TEXT,
	member_email TEXT
);