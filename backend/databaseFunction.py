from dataBase import Access

def store(databaseName: str, location: str, barcode):
    database = Access(databaseName)
    data = {"barcode" : [barcode], "price" : [10], "reserved": ["false"]}
    database.store(data, location)
    database.printDf(location)