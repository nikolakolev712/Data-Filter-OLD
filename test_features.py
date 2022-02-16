    #OLD CODE:
    # test_snaps_shapshotid = [i["SnapshotId"] for i in jsonObject["Snapshots"] if "086685601027" in i['OwnerId']]
    # test_snaps_ownerid = [i["OwnerId"] for i in jsonObject["Snapshots"] if "086685601027" in i['OwnerId']]
    # test_snaps_volumeid = [i["VolumeId"] for i in jsonObject["Snapshots"] if "086685601027" in i['OwnerId']]

    # data = {
    #     "SnapshotId": test_snaps_shapshotid,
    #     "OwnerId": test_snaps_ownerid,
    #     "VolumeId": test_snaps_volumeid
    # }

    #IF only 3 way filtering is needed: 
    # data = [
    #     {
    #     "SnapshotId": i["SnapshotId"],
    #     "OwnerId": i['OwnerId'],
    #     'VolumeId': i['VolumeId'] 
    # } for i in jsonObject['Snapshots'] if '086685601027' in i['OwnerId']
    
    # ]
    # data_2 = {}
    # for i in jsonObject["Snapshots"]:
    #     if i['VolumeId'] not in list( data_2):
    #         data_2.update({i['VolumeId']: [i['SnapshotId']]})
    #     else:
    #         data_2.get(i['VolumeId']).append(i['SnapshotId'])




#    def get_snapshots():
#     """Takes all snapshot ID's and matches them to the volume ID's"""

#     with open("snapshots-test.json", "r") as jsonFile:
#         jsonObject = json.load(jsonFile)
#         jsonFile.close()

#     #Match snapshotID to volumeID's:
#     volume_ids = [i['VolumeId'] for i in jsonObject['Snapshots'] if i['OwnerId'] == "086685601027"]
#     data_2 = [{i['VolumeId']: i['SnapshotId']} for i in jsonObject['Snapshots'] if i['VolumeId'] in volume_ids]
#     header = [i for i in volume_ids]
#     header_clean=[]
#     for i in header:
#         if i not in header_clean:
#             header_clean.append(i)

#     with open('test_filtered.csv','w', newline='') as f:
#         writer = csv.DictWriter(f,header_clean)
#         writer.writeheader()
#         writer.writerows(data_2)