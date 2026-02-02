import time

Border = "-"*50
timestamp = time.ctime()
LogFilename = "Demo%s.log" %(timestamp)
LogFilename = LogFilename.replace(" ", "_")
LogFilename = LogFilename.replace(":", "_")

fobj = open(LogFilename, "w")


