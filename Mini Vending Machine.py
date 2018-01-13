from terminaltables import SingleTable
import subprocess as sp

def print_vending_machine():
    line1= '   1     2     3   '  
    line2= '                   '
    line3= '  ^-^ | T-T  | @-@ '
    line4= '   4     5     6   '
    line5= '                   '
    line6= '  @.@ | *-*  | :P  '
    line7= '                   '
    line8= '       OUTPUT      '
    line9= '                   '
    line10='   _______________ ' 
    
    newlist=[]
    newlist.append([line1+"\n"+line2+"\n"+line3])
    newlist.append([line4+"\n"+line5+"\n"+line6])
    newlist.append([line8+"\n"+line9+"\n"+line10])
    #print(newlist)
    
    table=SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border=False
    table.title="Emoji Vending Machine"
    sp.call("clear",shell=True)
    print(table.table)

