	create TABLE user(
	id INTEGER primary key autoincrement,
	username TEXT not null,
	password TEXT not null,
	);

	create TABLE document(
	 id INTEGER primary key autoincrement,
	 user_id TEXT not null,
	 file_path TEXT,
	 FOREIGN KEY (user_id)
	 REFERENCES user(id)
	 ON update CASCADE
	 ON delete CASCADE
	);

	create TABLE document_metadata(
	id INTEGER primary key autoincrement,
	document_id not null ,
	type TEXT,
	data TEXT,
	FOREIGN KEY (document_id)
	REFERENCES document(id)
	ON update CASCADE
	ON delete CASCADE
	);

	create TABLE visualization (
	id INTEGER primary key autoincrement,
	document_id int not null,
	type TEXT,
	data TEXT,
	FOREIGN KEY (document_id)
	REFERENCES document(id)
	ON update CASCADE
	ON delete CASCADE
	);

	create TABLE visualization_metadata (
	id INTEGER primary key autoincrement,
	visualization_id int not null,
	data TEXT,
	FOREIGN KEY (visualization_id)
	REFERENCES visualization(id)
	ON update CASCADE
	ON delete CASCADE
	);

