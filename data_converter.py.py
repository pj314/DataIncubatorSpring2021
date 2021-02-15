from fixedwidth.fixedwidth import FixedWidth
from copy import deepcopy

SAMPLE_CONFIG = {
    "HRHHID": {
        "required": True,
        "type": "string",
        "start_pos": 1,
        "end_pos": 15,
        "alignment": "left",
        "padding": " "
    },
    "HRMONTH": {
        "required": True,
        "type": "string",
        "start_pos": 16,
        "end_pos": 17,
        "alignment": "left",
        "padding": " "
    },
    "HRYEAR": {
        "required": True,
        "type": "string",
        "start_pos": 18,
        "end_pos": 21,
        "alignment": "left",
        "padding": " "
    },
    "FILLER": {
        "required": True,
        "type": "string",
        "start_pos": 22,
        "end_pos": 431,
        "alignment": "left",
        "padding": " "
    },
    "WORKCODE": {
        "required": True,
        "type": "string",
        "start_pos": 432,
        "end_pos": 433,
        "alignment": "left",
        "padding": " "
    },
}

def convert(fread,fwrite,mode,month):
    fd=open(fread)
    fs=open(fwrite,mode)
    lines=[]
    line=""
    while True:
        c=fd.read(1)
        if not c:
            break
        line=line+c
        if c=='A':
            #consume the next line char
            c=fd.read(1)
            line=line+c
            lines.append(line)
            line=""

    if mode=="w":
        fs.write(str.format("{},{},{},{}\n","HRHHID","HRMONTH","HRYEAR","WORKCODE"))

    for line in lines:
        fw_config = deepcopy(SAMPLE_CONFIG)
        fw_obj = FixedWidth(fw_config)
        #fw_obj.line = (
        #    "000110107755856 42020 1201  -1 1 1-1 114-1-1-1  17968107 1 1 7 2 2 0 211011 1  2-1-1-1-1 36 01 338600001103000   -1-141-1720 4-1 2 2-1 246 1-1 9-1 1-1 0 0 2 2 5 2 57 57 57 1 0 0 1 1 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 2-140-1-1 40-1-1-1-1 2-1 2-140-1 40-1-1    2 5 5-1 2 3 5\r\n"
        #)
        fw_obj.line=line
        values = fw_obj.data
        assert(values["HRMONTH"]==month)
        fs.write(str.format("{},{},{},{}\n",values["HRHHID"],values["HRMONTH"],values["HRYEAR"],values["WORKCODE"]))

    fs.close()
    fd.close()


fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\jan20pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="w"
convert(fread,fwrite,mode,"1")

fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\feb20pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="a"
convert(fread,fwrite,mode,"2")

fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\mar20pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="a"
convert(fread,fwrite,mode,"3")

fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\apr20pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="a"
convert(fread,fwrite,mode,"4")


fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\may20pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="a"
convert(fread,fwrite,mode,"5")

fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\jun20pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="a"
convert(fread,fwrite,mode,"6")

fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\dec19pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="a"
convert(fread,fwrite,mode,"12")

fread="C:\\Users\\priya\\Downloads\\dataincubator_data\\jan19pub.dat"
fwrite="C:\\Users\\priya\\Downloads\\dataincubator_data\\hhid_month_workcode.csv"
mode="a"
convert(fread,fwrite,mode,"1")


#jan
#000004795110719 12020 1201  -1 1 1-1 1 7-1-1-1  16864805 1 2 1 6 1 1 209011 2  2-1-1-1-1 36 01 266200001103000   -1-140-1690 1 2 1 2-1 238 2-1 9-1 1-1 1 1 1 2 1 2 57 57 57 1 0 0 1 5 3-1-1 2-1-1-1 1-1 2-1-1-1-1-1-1-1-1-1-1-1 -1-1-1-1-1-1-1-1-1-1-1 -1-1-1   -1-1-1-1-1-1-1-1-1-1-1-1-1 -1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 -1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 2-1 0 4-1-1-1-1-1-1 -1-1-1 0 1 2-1-1-1-1-1-1-1-1      -1-1      -1-1-1 0-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 0-1-1-1-1  -1  -1  -1  -10-1      -10-1-1      -1      -10-1-1-1-1-1-1-1-1 2-1-1-1-1  16864805  25597552         0  17713809  17696998 0 0 0-1-1-1 0 0 1 0-1 0-1 0 0 0 0 1 0 0 0-1-1-1 0 0 0 0-1-1-1-1-1-1 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 1 1 1 1 1 1 1 1 1 1 1-1-1-1-1-1-1-1-1-1-1-1 0 0-1-1-1-1-1-1 1 1 1-1-1-121588 1-1-1-1-1-1-1 1 1 1-1-1-1  17347552  -1  -1  -1  -1-1-1-1-1-1-1 0-1-1-1-1-1 1 1 1 1 1 2 2 2 2 2 2 2 0 0 0 0 0 023-1-1-1-1-1 2-1-120 0 0                                            A

#apr
#000110107755856 42020 1201  -1 1 1-1 114-1-1-1  17968107 1 1 7 2 2 0 211011 1  2-1-1-1-1 36 01 338600001103000   -1-141-1720 4-1 2 2-1 246 1-1 9-1 1-1 0 0 2 2 5 2 57 57 57 1 0 0 1 1 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 2-140-1-1 40-1-1-1-1 2-1 2-140-1 40-1-1    2 5 5-1 2 3 5 2-1-1-1-1-1 -1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 -1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 1-118 1 1 1 4-1-1-1 -1-1-1 1 2-1-1-1-1 1 2 1 2 4      -1-1       4 3 3 1 2 2-1 2 8-140-1 8-1 110-1 2-1 1-1 1 1 0-1-1-1-1  -1  -1  -1  -10-1      -10-1-1      -1      -10-1-1-1-1-1-1-1-1-1-1-1-1-1  17968107  27553122         0  17968107  17383564 0 0 1-1-1-1 0 0 1 0-1 0-1 0 0 1 0 1 0 0 0-1-1-1 1 0 0-1 1 1 0 1 0 1 1 0 1 1 1 0 1 0 1 1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1 0 0 0-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-147911 1-1-1-1-1-1-1 1 1 1-1-1-1  1739501378702205  -1  -115-1-1-1-1-1 0-1-1-1-1-1 1 1 1 1 1 2 2 2 2 2 2 2 0 0 0 0 0 0 0-1-1-1-1-1 2-1-120 0 0                                            A