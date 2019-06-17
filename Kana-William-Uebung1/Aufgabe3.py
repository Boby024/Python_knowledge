import sys
# enter_seconds= int (input("enter the number of seconds"))

enter_seconds= int( sys.argv[1])

# to find year
jahr= enter_seconds / 31536000
rest_Seconds_Jahr= enter_seconds %  31536000


#to find days
tag= rest_Seconds_Jahr / 86400
rest_tag= rest_Seconds_Jahr % 86400

#to find hour
stunde= rest_tag / 3600
rest_stunde= rest_tag % 3600

# to find minutes
minutes= rest_stunde / 60
rest_minutes= rest_stunde % 60

#to find secondes
seconds= rest_minutes

print(enter_seconds," Sekunden sind ", int(jahr)," jahr(e) ,"
      ,int(tag)," Tag(e), ",int(stunde)," Stunde(n), ",int(minutes)," Minute(n), "
      ,int(seconds)," Sekunde(n)."

      )
