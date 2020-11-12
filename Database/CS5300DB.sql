Drop Table Authors;
Drop Table BookCopies;
Drop Table GeneralCopyMiscellanious;
Drop Table PhysicalCopyQualities;
Drop Table BookInfo;

CREATE TABLE PhysicalCopyQualities (
	CopyID BIGINT DEFAULT UUID_SHORT() NOT NULL PRIMARY KEY,	
	ConditionInfo varchar(50),
	Price char(20),
	Signed varchar(50),
	DustJacket varchar(50),
	Binding char(50),
	Description Text
);

CREATE TABLE GeneralCopyMiscellanious (
	CopyID BIGINT DEFAULT UUID_SHORT() NOT NULL PRIMARY KEY,
	Edition varchar(100),
	About_Auth Text,
	Synopsis Text,
	Foreign Key (CopyID) References PhysicalCopyQualities(CopyID)
);

CREATE TABLE BookInfo (
	BookID BIGINT DEFAULT UUID_SHORT() NOT NULL PRIMARY KEY,
	Title varchar(1000),
	Publisher char(50),
	PubDate INT,
	Isbn10 BIGINT,
	Isbn13 BIGINT
);

CREATE TABLE BookCopies (
	CopyID BIGINT DEFAULT UUID_SHORT() NOT NULL,
	BookID BIGINT DEFAULT UUID_SHORT() NOT NULL,
	PRIMARY KEY (CopyID, BookID),
	Foreign Key (CopyID) References PhysicalCopyQualities(CopyID),
	Foreign Key (BookID) References BookInfo(BookID)
);

CREATE TABLE Authors (
	BookID BIGINT DEFAULT UUID_SHORT() NOT NULL,
	AuthorID INT DEFAULT UUID_SHORT() NOT NULL,
	AuthorName varchar(50),
	PRIMARY KEY (BookID, AuthorID),
	Foreign Key (BookID) References BookInfo(BookID)
);