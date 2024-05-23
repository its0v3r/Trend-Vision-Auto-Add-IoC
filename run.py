# Main
if __name__ == "__main__":
    from app.general_def import (
        loadLanguage,
        loadClientList,
        selectClient,
        selectIocCsv,
        doProceedWithAction,
    )
    from app.trend_def import addObjectsToBlockList

    # Run
    loadLanguage()
    loadClientList()
    selectClient()
    selectIocCsv()
    doProceedWithAction()
    addObjectsToBlockList()
