from importlib.resources import files
import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import logging 
from datetime import datetime
import smtplib 
from email.message import EmailMessage

def BackupAndEmail(Source):
    log_file, zip_file = MarvellousDataSheildStart(Source)
    SendEmail(log_file, zip_file)

def SendEmail(log_file, zip_file):

    sender = "sudarshanahire12@gmail.com"
    receiver = "sudarshanahire4347@gmail.com"
    password = "cptx asnq bbdz bptd"

    msg = EmailMessage()
    msg["Subject"] = "Backup Completed"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Backup completed successfully.")

    with open(log_file, "r") as f:
        msg.add_attachment(
            f.read(),
            subtype="plain",
            filename=os.path.basename(log_file)
        )

    with open(zip_file, "rb") as zobj:
        msg.add_attachment(zobj.read(), maintype="application", subtype="octet-stream", filename=os.path.basename(zip_file))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
    
    except Exception as e:
        logging.error("Error sending email: %s", e)

def CreateLog():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = os.path.join("Logs", "BackupLog_" + timestamp + ".log")

    logging.basicConfig(filename=log_name, level=logging.INFO, format="%(asctime)s -%(levelname)s - %(message)s")

    return log_name

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    # open the zip file 
    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    
    for root , dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)

    zobj.close()

    return zip_name

def calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)

        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    copied_files = []

    logging.info("Creating backup folder")

    
    os.makedirs(Destination, exist_ok = True)

    for root, dirs, files in os.walk(Source):

        ignore_ext = [".tmp", ".log", ".exe"]

        for file in files:

            if any(file.endswith(ext) for ext in ignore_ext):
                continue 

            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)


            os.makedirs(os.path.dirname(dest_path), exist_ok = True)

            # Copy the files if its new 

            if(not os.path.exists(dest_path) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

  
    return copied_files


def MarvellousDataSheildStart(Source = "Data"):

    log_file = CreateLog()
    logging.info("Backup started")

    BackupName = "MarvellousBackup"
    logging.info("Backup started at %s", time.ctime())

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    logging.info("Backup completed")
    logging.info("Files copied : %d", len(files))
    logging.info("Zip file created : %s", zip_file)

    UpdateHistory(len(files), zip_file)

    logging.shutdown()

    logging.info("Backup completed successfully")
    logging.info("Files copied: %d", len(files))
    logging.info("Zip file created: %s", zip_file)

    for name in files:
        logging.info("Copied file: %s", name)

    return log_file, zip_file 

def UpdateHistory(file_count, zip_file):
    
    history_file = "BackupHistory.txt"

    size = os.path.getsize(zip_file)

    with open(history_file, "a") as fobj:
        fobj.write(f"{datetime.now()} | Files {file_count} | Size {size} bytes\n")

def ShowHistory():

    history_file = "BackupHistory.txt"

    if not os.path.exists(history_file):
        print("No backup history available.")
        return 
    
    print("----------- Backup History -----------")

    if os.path.exists(history_file):
        with open(history_file, "r") as hobj:
            content = hobj.read()
            print(content)
    else:
        print("No backup history available.")

def RestoreBackup(zip_file, destination):
    
    if not os.path.exists(zip_file):
        logging.error("Zip file not found")
        return 
    

    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zip_file, "r") as zobj:
        zobj.extractall(destination)

    logging.info("Restore completed successfully")

def main():

    Border = "-"*50
    print(Border)
    print("--------- Marvellous Data sheild System -----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("1 : Text auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create and archive of backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        elif(sys.argv[1] == "--history" or sys.argv[1] == "--HISTORY"):
            ShowHistory()

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        # print("Inside projects logic")
        # print("Time interval : ",sys.argv[1])
        # print("Directory name : ",sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(BackupAndEmail, sys.argv[2])

        print("Data sheild started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv) == 4 and sys.argv[1] == "--restore"):
        RestoreBackup(sys.argv[2], sys.argv[3])


    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
    
if __name__ == "__main__":
    main()