import sys
from data.config import DC
import requests
from app.utils_def import printSoftwareTitle, clearScreen


# Function to add new blocked objects to the selected client's Trend Vision One
def addObjectsToBlockList():
    for index, row in DC.client_df.iterrows():
        DC.client_name = row["client_name"]
        DC.client_token = row["token"]
        client_blocked_iocs_amount = 0
        client_skipped_objects = 0

        for index, row in DC.ioc_df.iterrows():
            clearScreen()
            printSoftwareTitle()
            print(f"{DC.lang_text["blocked_objects"]}: {client_blocked_iocs_amount}")
            print(f"{DC.lang_text["skipped_objects"]}: {client_skipped_objects}")
            
            go_to_next_ioc = False
            clients_already_blocked = str(row["blocked"]).split(',')

            for client in clients_already_blocked:
                if client == DC.client_name:
                    go_to_next_ioc = True
                    break
            
            if go_to_next_ioc == True:
                client_skipped_objects = client_skipped_objects + 1
                continue
            
            client_blocked_iocs_amount = client_blocked_iocs_amount + 1
            

            ioc_value = row["ioc"]
            type_value = row["type"]
            description_value = row["description"]

            url_base = "https://api.xdr.trendmicro.com"
            url_path = "/v3.0/response/suspiciousObjects"
            query_params = {}
            headers = {
                "Authorization": "Bearer " + DC.client_token,
                "Content-Type": "application/json;charset=utf-8",
            }

            body = []
            if str(type_value).lower() == "sha1":
                body = [{"description": description_value, "fileSha1": ioc_value}]
            elif str(type_value).lower() == "sha256":
                body = [{"description": description_value, "fileSha256": ioc_value}]
            elif str(type_value).lower() == "url":
                body = [{"description": description_value, "url": ioc_value}]
            elif str(type_value).lower() == "domain":
                body = [{"description": description_value, "domain": ioc_value}]
            elif str(type_value).lower() == "ip":
                body = [{"description": description_value, "ip": ioc_value}]
            elif str(type_value).lower() == "email":
                body = [{"description": description_value, "senderMailAddress": ioc_value}]

            r = requests.post(
                url_base + url_path, params=query_params, headers=headers, json=body
            )

    clearScreen()
    printSoftwareTitle()
    print(f"{DC.lang_text["blocked_objects"]}: {client_blocked_iocs_amount}")
    print(f"{DC.lang_text["skipped_objects"]}: {client_skipped_objects}")
    print()
    print(DC.lang_text["all_objects_have_been_blocked"])
    input(DC.lang_text["press_enter_to_exit"])
    sys.exit()
