from pandas_ods_reader import read_ods

def excelRead():
    parth = "plates.ods"
    data = read_ods(parth)

    return data

