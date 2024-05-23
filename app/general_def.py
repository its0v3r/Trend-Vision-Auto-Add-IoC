import sys
import pandas as pd
import json
from data.config import SC, DC
import os
from time import sleep
from app.utils_def import printSoftwareTitle, printWarningText, clearScreen


# Function to get the languague title from the .json lang file
def getLanguageFromFile(file_name):
    file_path = os.path.join(SC.LANG_PATH, file_name)
    with open(file_path, "r", encoding="utf-8") as infile:
        data = json.load(infile)
        return data.get("language")


# Function to print the list of available languages
def printLanguageList():
    for index, option in enumerate(SC.LANG_OPTIONS):
        file_name = getLanguageFromFile(option)
        print(f"[{index + 1}] - {file_name}")


# Function to load the software language
def loadLanguage():
    while True:
        clearScreen()
        printSoftwareTitle()
        printLanguageList()

        try:
            lang_code = int(input("\nChoose you language: ") or 1)
            if lang_code in range(1, len(SC.LANG_OPTIONS) + 1):
                language = ""
                for index, option in enumerate(SC.LANG_OPTIONS):
                    if lang_code == index + 1:
                        language = option

                language_path = os.path.join(SC.LANG_PATH + language)

                with open(language_path, "r", encoding="utf-8") as infile:
                    DC.lang_text = json.load(infile)

                print(f"You selected: {DC.lang_text["language"]}")
                sleep(1)
                break
            else:
                print("Invalid value. Try again.")
                sleep(1)
        except:
            print("Invalid value. Try again.")
            sleep(1)


# Function to load the client list csv
def loadClientList():
    DC.client_df = pd.read_csv(SC.CLIENT_DATA_CSV_PATH)


# Function to print the available clients in the csv
def printClientList():
    print(f"{DC.lang_text["available_client_list"]}:")
    print("")
    outside_index = 0
    for index, name in enumerate(DC.client_df["client_name"]):
        print(f"[{index + 1}] - {name}")
        outside_index = index
    print(f"[{outside_index + 2}] - {DC.lang_text["all_clients"]}")

# Function to select what client will be used
def selectClient():
    while True:
        clearScreen()
        printSoftwareTitle()
        printClientList()

        try:
            client = int(input(f"\n{DC.lang_text["select_the_client"]}: "))

            if client in range(1, len(DC.client_df["client_name"]) + 2):
                client = client - 1

                # If the user selects all clients
                if client == len(DC.client_df["client_name"]):
                    DC.all_clients = True
                    DC.client_name = DC.lang_text["all_clients"]
                    print(f"{DC.lang_text["you_selected"]}: {DC.lang_text["all_clients"]}")
                # If the user select a single client
                else:
                    selected_client = DC.client_df["client_name"][client]
                    print(f"{DC.lang_text["you_selected"]}: {selected_client}")
                    DC.client_df = DC.client_df[DC.client_df['client_name'] == selected_client]
                    DC.client_name = selected_client

                    
                sleep(1)
                break
            else:
                print(DC.lang_text["invalid_client_try_again"])
                sleep(1)
        except Exception as e:
            print(e)
            input("askjdaskjdha")
            print(DC.lang_text["invalid_value_try_again"])
            sleep(1)

    


# Function to load the IOC list csv
def selectIocCsv():
    DC.ioc_df = pd.read_csv(SC.IOC_DATA_CSV_PATH)


# Function to handle if the user will continue with the action or not
def doProceedWithAction():
    while True:
        clearScreen()
        printSoftwareTitle()
        printWarningText()

        print("")
        continue_operation = (
            input(f"{DC.lang_text["do_you_really_want_to_proceed_with_this_action"]}") or DC.lang_text["no"]
        )
        if continue_operation.lower() == DC.lang_text["yes"]:
            break
        elif continue_operation.lower() == DC.lang_text["no"]:
            print(DC.lang_text["operation_will_be_aborted_no_changes_will_be_done_in_the_ambient"])
            print(DC.lang_text["quitting_software"])
            sys.exit()
        else:
            print(DC.lang_text["invalid_value_try_again"])
            sleep(1)
