CREATE TABLE IF NOT EXISTS Subject(
	subjectID integer PRIMARY KEY,
	height integer CHECK (height > 0),
	gender integer  CHECK(gender >= 0 AND gender <=3),
	handedness integer CHECK(handedness = 0 OR handedness =1),
	birthyear integer CHECK(birthyear < 2020)

);


CREATE TABLE IF NOT EXISTS Nausea (
nauseaID serial PRIMARY KEY,
subjectID int REFERENCES Subject (subjectID),
trains integer CHECK(trains >= 0 AND trains <=4),
airplanes integer CHECK(airplanes >= 0 AND airplanes <=4),
smallBoats integer CHECK(smallBoats >= 0 AND smallBoats <=4),
ships integer CHECK(ships >= 0 AND ships <=4),
swings integer CHECK(swings >= 0 AND swings <=4),
roundabout integer CHECK(roundabout >= 0 AND roundabout <=4),
funfair integer CHECK(funfair >= 0 AND funfair <=4),
busses integer CHECK(busses >= 0 AND busses <=4),
cars integer CHECK(cars >= 0 AND cars <=4)
);

CREATE TABLE IF NOT EXISTS MSGolden (
MSGoldenID serial PRIMARY KEY,
subjectID int REFERENCES Subject (subjectID),
type integer CHECK(type = 0 OR type =1),
dizziness integer CHECK(dizziness >= 0 AND dizziness <=3),
nausea integer CHECK(nausea >= 0 AND nausea <=3),
sweat integer CHECK(sweat >= 0 AND sweat <=3),
diffOfFocus integer CHECK(diffOfFocus >= 0 AND diffOfFocus <=3),
blurredVision integer CHECK(blurredVision >= 0 AND blurredVision <=3),
incrSalvation integer CHECK(incrSalvation >= 0 AND incrSalvation <=3),
eyestrain integer CHECK(eyestrain >= 0 AND eyestrain <=3),
headache integer CHECK(headache >= 0 AND headache <=3),
fatigue integer CHECK(fatigue >= 0 AND fatigue <=3),
genDiscomfort integer CHECK(genDiscomfort >= 0 AND genDiscomfort <=3)
);


CREATE TABLE IF NOT EXISTS GeneralInfo(
	genID serial PRIMARY KEY,
	subjectID int REFERENCES Subject (subjectID),
	foodTime integer CHECK(foodTime >= 0 AND foodTime <=3), 
caffeine integer CHECK(caffeine = 0 OR caffeine =1),
weight integer , 
healthyScale integer CHECK(healthyScale >= 1 AND healthyScale <=5), 
groups CHAR (20),
nicotine integer CHECK(nicotine = 0 OR nicotine =1), 
noExercise integer CHECK(noExercise >= 0 AND noExercise <=4), 
alcohol integer CHECK(alcohol >= 0 AND alcohol <=2),
MSDrugs integer CHECK(MSDrugs = 0 OR MSDrugs =1),
motionSickness integer CHECK(motionSickness >= 0 AND motionSickness <=4),
comments CHAR(100)
);


CREATE TABLE IF NOT EXISTS EMG (
	EMGID serial PRIMARY KEY,
subjectID int REFERENCES Subject (subjectID),
	sensor1 float, 
sensor2 float, 
sensor3 float, 
sensor4 float, 
sensor5 float, 
sensor6 float, 
time float
);


CREATE TABLE IF NOT EXISTS Platform (
	platformID serial PRIMARY KEY,
subjectID int REFERENCES Subject (subjectID),
roll float,
pitch float,
heave float,
AP float,
ML float,
time float
);


CREATE TABLE IF NOT EXISTS HR (
	HRID serial PRIMARY KEY,
    subjectID int REFERENCES Subject (subjectID),
	time Time,
	BPM integer
);


CREATE TABLE IF NOT EXISTS EEG (
	EEGID serial PRIMARY KEY,
subjectID int REFERENCES Subject (subjectID)
);


CREATE TABLE IF NOT EXISTS SpO2 (
SpO2ID serial PRIMARY KEY,
subjectID int REFERENCES Subject (subjectID),
oxigenation float,
time Time
);

SELECT * FROM Subject;
SELECT * FROM HR;
SELECT * FROM SpO2;
SELECT * FROM Platform;

SELECT AVG(BPM) FROM HR WHERE subjectID=4
SELECT AVG(BPM) FROM HR WHERE subjectID=13
SELECT AVG(BPM) FROM HR WHERE subjectID=18
SELECT AVG(BPM) FROM HR WHERE subjectID=44
SELECT AVG(BPM) FROM HR WHERE subjectID=80

DELETE FROM HR;

DROP TABLE HR;
DROP TABLE SpO2;
DROP TABLE EEG;
DROP TABLE Platform;
DROP TABLE EMG;
DROP TABLE GeneralInfo;
DROP TABLE MSGolden;
DROP TABLE Nausea;
DROP TABLE Subject;