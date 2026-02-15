import sys
import psutil 
import os
import time
import schedule
from datetime import datetime
import smtplib
from email.message import EmailMessage

def CreateLog(FolderName, receiver):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory for log file created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)
    print("Log file gets created with name : ", FileName)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("---------- Platform Surveillance System ----------\n\n")
    fobj.write("Log Created at : " + time.ctime()+ "\n")
    fobj.write(Border+"\n")

    fobj.write("---------------- System Report -------------------\n\n")

    Data = ProcessScan()

    total_processes = len(Data)

    TopCPU = sorted(Data, key=lambda x: x.get("cpu", 0), reverse=True)[:5]
    TopMemory = sorted(Data, key=lambda x: x.get("rss", 0), reverse=True)[:10]
    TopThreads = sorted(Data, key=lambda x: x.get("thread_count", 0), reverse=True)[:5]
    TopOpenFiles = sorted(Data, key=lambda x: x.get("Open_files") if isinstance(x.get("Open_files"), int) else 0, reverse=True)[:5]

    # TopMemory = sorted(Data, key=lambda x : x.get("rss", 0), reverse=True)[:10]

    fobj.write("Top 10 memory consuming Processes\n")
    fobj.write(Border + "\n")

    for info in TopMemory:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Process Name : %s\n" %info.get("name"))
        fobj.write("Memory (RSS in MB) : %.2f\n" %info.get("rss"))
        fobj.write("Memory (VMS in MB) : %.2f\n" %info.get("vms"))
        fobj.write("Memory percentage : %.2f\n" %info.get("memory_percent"))
        fobj.write(Border + "\n")

    fobj.write("\n\nComplete Process Report\n")
    fobj.write(Border + "\n")

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Process Name : %s\n" %info.get("name"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu"))
        fobj.write("Memory (RSS MB) : %.2f\n" % info.get("rss"))
        fobj.write("Memory (VMS MB) : %.2f\n" % info.get("vms"))
        fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
        fobj.write("Thread Count : %s\n" %info.get("thread_count"))
        fobj.write("Open file count : %s\n" %info.get("Open_files"))
        fobj.write("Timestamp : %s\n" % datetime.now())
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("------------- End of File -----------------\n")
    fobj.write(Border+"\n")


    fobj.close()

    sender = "sudarshanahire12@gmail.com"
    app_password = "cptx asnq bbdz bptd"
    subject = "Platform serveillance system Automation Mail"
    body = f"""
    Platform Surveillance System Report
    ------------------------------------

    Total Running Processes : {total_processes}

    Top 5 CPU Usage Processes:
    """

    for p in TopCPU:
        body += f"{p['name']} (PID: {p['pid']}) - CPU: {p['cpu']:.2f}%\n"

    body += "\nTop 5 Memory Usage Processes:\n"
    for p in TopMemory[:5]:
        body += f"{p['name']} (PID: {p['pid']}) - RSS: {p['rss']:.2f} MB\n"

    body += "\nTop 5 Thread Count Processes:\n"
    for p in TopThreads:
        body += f"{p['name']} (PID: {p['pid']}) - Threads: {p['thread_count']}\n"

    body += "\nTop 5 Open File Processes:\n"
    for p in TopOpenFiles:
        open_files = p['Open_files'] if isinstance(p['Open_files'], int) else 0
        body += f"{p['name']} (PID: {p['pid']}) - Open Files: {open_files}\n"

    SendEmail(sender, app_password, receiver, subject, body, FileName)

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass 

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name"])

            mem = proc.memory_info()
            info["rss"] = mem.rss / (1024 * 1024)
            info["vms"] = mem.vms / (1024 * 1024)
            info["memory_percent"] = proc.memory_percent()

            info["cpu"] = proc.cpu_percent()
            info["thread_count"] = proc.num_threads()

            try:
                files = proc.open_files()
                info["Open_files"] = len(files)

            except psutil.AccessDenied:
                info["Open_files"] = "Access Denied"

            except:
                info["Open_files"] = "NA"



            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(proc.create_time()))

            except:
                info["create_time"] = "NA"

            
            listprocess.append(info)
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass 
    
    return listprocess

def SendEmail(sender, app_password, receiver, subject, body, FileName):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    with open(FileName, "rb") as eobj:
        file_data = eobj.read()
        file_name = os.path.basename(FileName)

    msg.add_attachment(file_data, 
                       maintype ="application",
                       subtype="octet-stream",
                       filename = file_name)

    try:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        smtp.login(sender, app_password)

        smtp.send_message(msg)
        
        smtp.quit()
    
        print("Log File emailed Successfully")
    
    except Exception as e:
        print("Error sending email ", e)



def main():
    Border = "-"*50
    print(Border)
    print("---------- Platform Surveillance System ----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print(Border+"\n")
            print("This script is used for platform surveillance")
            print("1 : Thread Monitoring")
            print("2 : Open File Monitoring")
            print("3 : Memory Monitoring")
            print("4 : Top 10 Memory Processes")
            print("5 : Periodic Log Generation")
            print(Border+"\n")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py DirectoryName ReceiverMail, TimeInterval")
            print("DirectoryName : Log Folder Name")
            print("ReceiverEMail : Receivers Email Address")
            print("Timeinterval : The time in minutes for periodic shceduling")
           

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    elif(len(sys.argv) == 4):
        print("Inside projects logic")
        print("DirectoryName :", sys.argv[1])
        print("Receiver Email :", sys.argv[2])
        print("Time interval :", sys.argv[3])
        

        schedule.every(int(sys.argv[3])).minutes.do(CreateLog, sys.argv[1], sys.argv[2])

        while True:
           schedule.run_pending()
           time.sleep(1)


    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("-------- Thank you for using our script -----------")
    print(Border)

     

if __name__ == "__main__":
    main()