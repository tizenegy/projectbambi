# variables inside the xml elements
eID = "lBaa1Vh7"
groupID = "SMUTib8O"
groupName = ";groupname="+groupID


# available OaA xml elements (code copied from OaA 2018-03-24)
# to be completed (spacer, input, toggle,...)
pagesStart = "<?xml version=\"1.0\" encoding=\"utf-8\"?><pages>"
pageStart = "<page pageid=\"4\" caption=\"fourth\"><excelcontent id=\"2\"><items>"
outputElement = "<item caption=\"\" inputtype=\"output\" contenttype=\"string\" address=\"Tabelle1!B1\" id=\""+eID+"\"><itemdefinitions>usecellformat=true;backgroundcolor=#e6ffffff;buttonradius=8;captiontextcolor=#4c4c4c;elementcolor=#4c4c4c;valuetextcolor=#4c4c4c</itemdefinitions></item>"
groupElement = "<item id=\""+eID+"\" caption=\""+eID+"\" inputtype=\"output\" contenttype=\"grouplayout\"><itemdefinitions></itemdefinitions></item>"
groupedOutputElement = "<item caption=\"A number\" inputtype=\"output\" contenttype=\"integer\" address=\"Tabelle1!B2\" id=\""+eID+"\"><itemdefinitions>usecellformat=true;backgroundcolor=#e6ffffff;buttonradius=6;captiontextcolor=#4c4c4c;elementcolor=#4c4c4c;valuetextcolor=#4c4c4c"+groupName+"</itemdefinitions></item>"
groupedCheckBox = "<item caption=\"\" inputtype=\"input\" contenttype=\"checkbox\" address=\"Tabelle1!C4\" id=\""+eID+"\"><itemdefinitions>usecellformat=true;backgroundcolor=#e6ffffff;buttonradius=8;captiontextcolor=#4c4c4c;elementcolor=#4c4c4c;valuetextcolor=#4c4c4c"+groupName+";elementwidth=60</itemdefinitions></item>"
chartElement = "<item caption=\"two numbers\" inputtype=\"output\" contenttype=\"chart\" address=\"Tabelle1!A2:A3;Tabelle1!B2:B3\" id=\""+eID+"\"><itemdefinitions>backgroundcolor=#b3ffffff;charttype=pie;chartseriestypes=pie;showlegend=true;seriescaptions=Serie1;height=350;buttonradius=0;captiontextcolor=#4c4c4c;elementcolor=#4c4c4c;valuetextcolor=#4c4c4c;axiscolor=#4c4c4c;colorpalette=#d1dabe,#12ba98,#4c4c4c,#92aa9d,#537780,#323232,#1e6262,#2b2e4a;legendtextcolor=#4c4c4c;seriescolor=#09679b;titletextcolor=#4c4c4c</itemdefinitions></item>"
pageEnd = "</items></excelcontent></page>"
pagesEnd = "</pages>"

# maybe use xml spacer element?
error = ""

# TODO
# replace magic strings in xml elements by variables!

# switch translates numbers from shape recognition to element variables
def switch(xmlElement):
    return {
        0: groupElement,
        1: outputElement,
        2: groupedCheckBox,
        3: chartElement,
        4: groupedOutputElement,
        51: pagesStart,
        52: pageStart,
        53: pageEnd,
        54: pagesEnd
    }.get(xmlElement, error)    # "error" is default if xmlElement is not found



# expected data from shape recognition:
# index 0: type of shape
# index 1: group number
incomingArray = [[1, 1], [0, 2], [4, 2], [4, 2], [0, 3], [4, 3],[2, 3], [3, 4]]    # dummy data

# output file --> data to be sent to OaA API later on
file = open("XML_result.txt", "a")
file.truncate(0)

# Start of xml is always the same
file.write(switch(51))
file.write(switch(52))

# writing the actual xml
for x in incomingArray:
    print(switch(x[0])+"\n")
    file.write(switch(x[0]))
    print(str(x[1])+"\n")

# End of xml is always the same
file.write(switch(53))
file.write(switch(54))

file.close()
