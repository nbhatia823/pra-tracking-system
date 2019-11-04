drop table Pra;

CREATE TABLE Pra (
	-- General data
	id SERIAL PRIMARY KEY,
    	county varchar(30),
	lea varchar(50),
	isSheriffsDept bool,
	dateOfLastContact date,
	updates note,
	currentStatus varchar(50),
	comments text,
	
	-- Request data
	dateOfRequest date,
    	startDateRequested date,
    	endDateRequested date,
	variables variable ARRAY,
	initialContactMethod varchar(30),
	initialContactPerson varchar(30),
	initialContactInfo varchar(100),
	linkToPRARequest varchar(100),
	
	-- Received data
	startDateReturned date,
    	endDateReturned date,
	currentContact contact,
	variablesChecked bool,
	variablesComplete bool,
	dataQualityChecked bool,
	dataActionable bool,
	dataCleaned bool,
	dataGeocoded bool,
	dataAnalyzed bool,
	leadMember varchar(50)
);

CREATE TYPE note AS (
	date date,
    entry text 
);

CREATE TYPE variable AS (
	name varchar(50),
    wasRequested bool,
	wasReceived bool
);

CREATE TYPE contact AS (
	method varchar(30),
	person varchar(30),
	info varchar(100)
);

CREATE TYPE status AS (
	description varchar(50),
	setDate date,
	deadline date
);
