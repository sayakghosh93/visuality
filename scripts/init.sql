	CREATE TABLE user(
	id int not null,
	username TEXT not null,
	password TEXT not null
	);

	CREATE TABLE document(
	 id int not null,
	 user_id TEXT not null,
	 file_path TEXT,
	 PRIMARY KEY (id),
	 FOREIGN KEY (user_id)
	 REFERENCES user(id)
	 ON UPDATE CASCADE
	 ON DELETE CASCADE
	);

	CREATE TABLE document_metadata(
	id int not null,
	document_id not null ,
	type TEXT,
	metadata TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (document_id)
	REFERENCES document(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE
	);

	CREATE TABLE visualization (
	id int not null,
	document_id int not null,
	type TEXT,
	metadata TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (document_id)
	REFERENCES document(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE
	);

	CREATE TABLE visualization_metadata (
	id int not null,
	visualization_id int not null,
	data TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY (visualization_id)
	REFERENCES visualization(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE
	);

