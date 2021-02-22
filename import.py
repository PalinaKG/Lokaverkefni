import psycopg2
import csv
import os, fnmatch
conn = psycopg2.connect("host=localhost dbname=MSprufa user=postgres password=Pallur109")
cur = conn.cursor()




def OpenFile(fileName, subID):

    fileDir = os.path.dirname(os.path.abspath(__file__))
    path = fileDir + "/DATA/" + str(subID)

    file = path + fileName
    return file




def find(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return name


with open(OpenFile('questionnaireTEST.csv',''), 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header
    for row in reader:
        cur.execute(
            "INSERT INTO Subject(subjectID, height, gender, handedness, birthyear) VALUES (%s, %s, %s, %s, %s)",
            (row[1], row[7], row[6], row[9], row[5])
        )
        cur.execute(
            "INSERT INTO GeneralInfo(subjectID, foodTime, caffeine, weight, groups, healthyScale, nicotine, noExercise, alcohol, MSDrugs, motionSickness, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
            (row[1], row[10], row[11], row[8], row[2], row[12], row[14], row[13], row[15], row[17], row[16], row[27])
        )
        cur.execute(
            "INSERT INTO Nausea(subjectID, cars, busses, trains, airplanes, smallBoats, ships, swings, roundabout, funfair) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[1], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26])
        )
        cur.execute(
            "INSERT INTO MSGolden(subjectID, types, genDiscomfort, fatigue, headache, eyestrain, diffOfFocus, incrSalvation, sweat, nausea, blurredVision, dizziness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[1], 0, row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37])
        )
        cur.execute(
            "INSERT INTO MSGolden(subjectID, types, genDiscomfort, fatigue, headache, eyestrain, diffOfFocus, incrSalvation, sweat, nausea, blurredVision, dizziness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (row[1], 1, row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47])
        )


subID = [4, 12, 13, 18, 44, 80]
for sub in subID:
    with open(OpenFile('/EMG_raw.csv',sub), 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header
        for row in reader:
            cur.execute(
                "INSERT INTO EMG(subjectID, time, sensor1, sensor2, sensor3, sensor4, sensor5, sensor6) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (sub, row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            )
for sub in subID:
    with open(OpenFile('/HR.CSV',sub)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        start=0
        for col in csv_reader:
            start=start+1
            if start >= 4:
                cur.execute( 
                    "INSERT INTO HR(subjectID, time ,BPM) VALUES(%s, %s,%s)", (sub, col[1], col[2]))

    file=find('O2Ring*', OpenFile('',sub))
    with open(OpenFile("/" + file,sub)) as csv_file2:
        csv_reader2 = csv.reader(csv_file2, delimiter=',')
        start=0
        for col in csv_reader2:
            start=start+1
            if start >= 2:
                time=col[0].split(' ')
                cur.execute( 
                    "INSERT INTO SpO2(subjectID, oxigenation, time) VALUES(%s, %s,%s)", (sub, col[1], time[0])
                    )

        with open(OpenFile("/new_platform.CSV",sub)) as csv_file1:
            csv_reader1 = csv.reader(csv_file1, delimiter=',')
            start=0
            stop=False
            for col in csv_reader1:
                start=start+1
                if col[1] == ' MotionVR pitch average':
                    stop=True
                if start >= 2 and stop==False:
                    cur.execute( 
                        "INSERT INTO Platform(subjectID, roll, pitch, heave, AP, ML, time) VALUES(%s, %s,%s, %s, %s,%s, %s)", (sub, col[2], col[1], col[3], col[5], col[4], col[0])
                        )

conn.commit()




# if __name__=="__main__":
