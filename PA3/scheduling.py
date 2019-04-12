import random
import pymysql.cursors  
 

try:
    connection = pymysql.connect(host="uvaclasses.martyhumphrey.info",user="JoeJackson",passwd="HitSingle1991",db="uvaclasses" )
    dbhandler = connection.cursor()
    #query = 'SELECT Description FROM CompSci1192Data WHERE Number = 2110 LIMIT 1'
    # SELECT Instructor FROM CompSci1192Data WHERE Number = 2110 LIMIT 1

    #query = 'SELECT id,sing_name,bir_yr FROM singers_list WHERE bir_yr = %s'
    #curs.execute(query, (year, ))
    #query = 'SELECT EnrollmentLimit - Enrollment as seats FROM CompSci1192Data WHERE Number = %s LIMIT 1'
    #query = 'SELECT Description FROM CompSci1192Data WHERE Number = %s LIMIT 1'
    query = 'SELECT Instructor FROM CompSci1192Data WHERE Number = %s LIMIT 1'
    num = 2110
    dbhandler.execute(query,(num,))
    print ("connect successful!!")
    result = dbhandler.fetchall()
    print(str(result[0]))

except Exception as e:
    print(e)

finally:
    connection.close()



def parseInt(value):
    try:
        return int(value)
    except ValueError:
        return 100

def lucky_number(event, context):
    #print(event)
    CourseNum = event['request']['intent']['slots']['coursenum']
    num = None
    if 'value' in CourseNum:
        num = parseInt(CourseNum['value'])
 
    res = ""
    if event['request']['intent']['name'] == "info":
        try:
            connection = pymysql.connect(host="uvaclasses.martyhumphrey.info",user="JoeJackson",passwd="HitSingle1991",db="uvaclasses" )
            dbhandler = connection.cursor()
            query = 'SELECT Description FROM CompSci1192Data WHERE Number = %s LIMIT 1'
            dbhandler.execute(query, (num, ))
            result = dbhandler.fetchall()
            #for item in result:
            #    print(item)

        except Exception:
            res = " No such course"

        finally:
            connection.close()
        
        res = "is " + str(result[0][0])

    if event['request']['intent']['name'] == "instructor":
        try:
            connection = pymysql.connect(host="uvaclasses.martyhumphrey.info",user="JoeJackson",passwd="HitSingle1991",db="uvaclasses" )
            dbhandler = connection.cursor()
            query = 'SELECT Instructor FROM CompSci1192Data WHERE Number = %s LIMIT 1'
            dbhandler.execute(query, (num, ))
            result = dbhandler.fetchall()
            #for item in result:
            #    print(item)

        except Exception:
            res = " No such course"

        finally:
            connection.close()
        
        res = "is taught by " + str(result[0][0])

    if event['request']['intent']['name'] == "seats":
        try:
            connection = pymysql.connect(host="uvaclasses.martyhumphrey.info",user="JoeJackson",passwd="HitSingle1991",db="uvaclasses" )
            dbhandler = connection.cursor()
            query = 'SELECT EnrollmentLimit - Enrollment as seats FROM CompSci1192Data WHERE Number = %s LIMIT 1'
            dbhandler.execute(query, (num, ))
            result = dbhandler.fetchall()
            #for item in result:
            #    print(item)

        except Exception:
            res = " No such course"

        finally:
            connection.close()
        
        res = "has " + str(result[0][0]) + " seats left"
    
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': "CS " + str(num) + " " + res,
            }
        }
    }

    return response