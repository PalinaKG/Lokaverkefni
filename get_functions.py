import psycopg2
conn = psycopg2.connect("host=localhost dbname=MSprufa user=postgres password=Pallur109")
cur = conn.cursor()

def getHR(id):
    HR=cur.execute( 
        "SELECT time,BPM FROM HR WHERE subjectID=%s", str(id)
                    )
    HR=cur.fetchall()
    return HR


def getPlatform(id):
    Platform=cur.execute( 
        "SELECT roll, pitch, heave, AP, ML, time FROM Platform WHERE subjectID=%s", str(id)
                    )
    Platform=cur.fetchall()
    return Platform

def getSpO2(id):
    SpO2=cur.execute( 
        "SELECT oxigenation,time FROM SpO2 WHERE subjectID=%s", str(id)
                    )
    SpO2=cur.fetchall()
    return SpO2


def getHR_age_gender(age1, age2, gender): #Takes all the HR from everyone and calculates the average of it 
    HR=cur.execute(
        """SELECT AVG(BPM) FROM HR h 
        INNER JOIN Subject s ON h.subjectID = s.subjectID 
        WHERE (s.birthyear >= %s AND s.birthyear <= %s) AND s.gender=%s""", (age1, age2, gender)
    )
    HR=cur.fetchall()
    return HR[0][0]

def getEMG_gender_age(gender, age1, age2):
    EMG = cur.execute(
        """SELECT AVG(sensor1) FROM EMG e
        INNER JOIN Subject s ON e.subjectID = s.subjectID
        WHERE (s.birthyear >= %s AND s.birthyear <= %s) AND s.gender = %s""", (age1, age2, gender)
    )
    EMG = cur.fetchall()
    return EMG[0][0]

conn.commit()

if __name__=="__main__":
    HR=getHR(4)
    Platform=getPlatform(4)
    SpO2=getSpO2(4)
    HR_age=getHR_age_gender(1980,1999,0)
    EMG_age = getEMG_gender_age(0,1980, 1999)
    print(HR_age)
    print(EMG_age)


