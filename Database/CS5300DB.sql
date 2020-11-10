Drop Table Authors;
Drop Table BookCopies;
Drop Table GeneralCopyMiscellanious;
Drop Table PhysicalCopyQualities;
Drop Table BookInfo;

CREATE TABLE PhysicalCopyQualities (
	CopyID INT DEFAULT UUID_SHORT() NOT NULL PRIMARY KEY,	
	ConditionInfo char(20),
	Price char(20),
	Signed char(20),
	DustJacket char(20),
	Binding char(50),
	Description Text
);
	
	
CREATE TABLE GeneralCopyMiscellanious (
	CopyID INT DEFAULT UUID_SHORT() NOT NULL PRIMARY KEY,
	Edition char(30),
	About_Auth Text,
	Synopsis Text,
	Foreign Key (CopyID) References PhysicalCopyQualities(CopyID)
);

CREATE TABLE BookInfo (
	BookID INT DEFAULT UUID_SHORT() NOT NULL PRIMARY KEY,
	Title char(100),
	Publisher char(50),
	PubDate INT,
	Isbn10 INT,
	Isbn13 INT
);

CREATE TABLE BookCopies (
	CopyID INT DEFAULT UUID_SHORT() NOT NULL,
	BookID INT DEFAULT UUID_SHORT() NOT NULL,
	PRIMARY KEY (CopyID, BookID),
	Foreign Key (CopyID) References PhysicalCopyQualities(CopyID),
	Foreign Key (BookID) References BookInfo(BookID)
);

CREATE TABLE Authors (
	BookID INT DEFAULT UUID_SHORT() NOT NULL,
	AuthorID INT DEFAULT UUID_SHORT() NOT NULL,
	PRIMARY KEY (BookID, AuthorID),
	Foreign Key (BookID) References BookInfo(BookID)
);


