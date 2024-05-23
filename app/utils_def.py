from data.config import SC, DC
from os import system


# Function to print software title and it's version
def printSoftwareTitle():
    print(f"Trend Vision - Auto Add IoC {SC.VERSION}")
    if DC.lang_text != None:
        print("")
        print(f"{DC.lang_text["selected_client"]}: {DC.client_name}")
        print(f"{DC.lang_text["path_to_ioc_csv"]}: {SC.IOC_DATA_CSV_PATH}")
    print("")


# Function to clear the screen
def clearScreen():
    system("cls")


# Function to print if the user wants to continue with the action
def printWarningText():
    print(DC.lang_text["warning"])
    print(
        f"{DC.lang_text["warning_text_to_continue_with_action_01"]} {DC.client_name} {DC.lang_text["warning_text_to_continue_with_action_02"]} {DC.lang_text["dont_forget_to_change_the_objects_expiration_date"]}"
    )
