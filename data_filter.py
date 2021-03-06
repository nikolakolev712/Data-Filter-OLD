import csv
import json
import pandas as pd
from datetime import datetime

# For the get_volumes() function - This is the place where the values are to be changed: 
json_file = "volumes-test"
csv_file = "test_volumes"

# For the filter_active() function - This is the place where the values are to be changed: 
file_name = "snapshots_test"
owner_id_ = "086685601027"

# For the filter_date() function - This is the place where the values are to be changed: 
date_cvs = "snapshots_test"
start_date_time = "2021-12-01"

# Get Time object: 
def time_(stri, start_date):

    stri = stri.split("T")[0]

    date_dt = datetime.strptime(stri, '%Y-%m-%d')
    
    date_dt_ = datetime.strptime(start_date, '%Y-%m-%d')

    end_date = datetime.now()

    if date_dt_ <= date_dt <= end_date:
        return True


#Get Volume ID's:
def get_volumes(json_file, csv_file):

    with open(f"{json_file}.json", "r") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
    test_vols_volumeid = [i["VolumeId"] for i in jsonObject["Volumes"]]

    data = {
        "VolumeId": test_vols_volumeid
    }

    df = pd.DataFrame.from_dict(data)
    df.to_csv(f"{csv_file}.csv", index=False)


# Get Active volumes:
def filter_active(owner_id, snapshots_csv):

    with open(f"{snapshots_csv}.csv", "r") as f:
        data_v = csv.DictReader(f)
        data_v = [i for i in data_v]
        data_d = sum([[v for (k,v) in i.items()] for i in data_v], [])
        
    with open(f"{snapshots_csv}.csv", "r") as f:
        data = csv.DictReader(f)
        data_active = [i for i in data if i["Snapshots/OwnerId"] == owner_id and i["Snapshots/VolumeId"] in data_d]
        #data_inactive = [i for i in data if i["Snapshots/OwnerId"] == owner_id and i["Snapshots/VolumeId"] not in data_d]

    data_active_snapshots = pd.DataFrame(data_active)
    #data_inactive_snapshots = pd.DataFrame(data_inactive)

    data_active_snapshots.to_csv("active_volumes.csv", index=False)
    #data_inactive_snapshots.to_csv("inactive_volumes.csv", index=False)


# Get Inactive volumes:
def filter_inactive(owner_id, snapshots_csv):

    with open(f"{snapshots_csv}.csv", "r") as f:
        data_v = csv.DictReader(f)
        data_v = [i for i in data_v]
        data_d = sum([[v for (k,v) in i.items()] for i in data_v], [])
        
    # with open(f"{snapshots_csv}.csv", "r") as f:
    #     data = csv.DictReader(f)
        data_inactive = [i for i in data_v if i["Snapshots/OwnerId"] == owner_id and i["Snapshots/VolumeId"] not in data_d]

    data_inactive_snapshots = pd.DataFrame(data_inactive)
    data_inactive_snapshots.to_csv("inactive_volumes.csv", index=False)


# Filter entries by date: 
def filter_date(date_cvs, start_date_, owner_id):
    with open("test_volumes.csv", "r") as f:
        data_v = csv.DictReader(f)
        data_v = [i for i in data_v]
        
    with open(f"{date_cvs}.csv", "r") as f:
        data = csv.DictReader(f)
        data = [i for i in data if time_(i["Snapshots/StartTime"], start_date_) and i["Snapshots/OwnerId"] == owner_id]
        
    data_snapshots = pd.DataFrame(data)
    #print(data_snapshots)
    data_snapshots.to_csv("date_formated.csv", index=False)





#get_volumes(json_file=json_file, csv_file=csv_file)

#filter_active(owner_id=owner_id_, snapshots_csv=file_name)

filter_inactive(owner_id=owner_id_, snapshots_csv=file_name)

#filter_date(date_cvs=date_cvs, start_date_=start_date_time, owner_id=owner_id_)