import os


# StaticConfig
class SC:
    VERSION = "1.0"
    CLIENT_DATA_CSV_PATH = os.path.join(os.getcwd() + "\\csv\\client_data.csv")
    IOC_DATA_CSV_PATH = os.path.join(os.getcwd() + "\\csv\\ioc_list.csv")
    LANG_PATH = os.path.join(os.getcwd() + "\\lang\\")
    LANG_OPTIONS = os.listdir(LANG_PATH)


# DynamicConfig
class DC:
    lang_text = None
    client_df = None
    all_clients = False
    client_name = ""
    client_token = ""
    ioc_df = None
