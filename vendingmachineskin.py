from terminaltables import SingleTable
import subprocess as sp

def print_vending_machine():
    line1= '   1     2     3   '  
    line2= '                   '
    line3= '  ^_^ | T-T  | @_@ '
    line4= '  20  |  60  | 100 '
    line5= '   4     5     6   '
    line6= '                   '
    line7= '  @.@ | *-*  | :P  '
    line8= '  150 | 200  | 250 '
    line9= '                   '
    line10='       OUTPUT      '
    line11='                   '
    line12='   _______________ ' 
    
    newlist=[]
    newlist.append([line1+"\n"+line2+"\n"+line3+"\n"+line4])
    newlist.append([line5+"\n"+line6+"\n"+line7+"\n"+line8])
    newlist.append([line9+"\n"+line10+"\n"+line11+"\n"+line12])
    #print(newlist)
    
    table=SingleTable(newlist)
    table.inner_row_border = True
    table.inner_heading_row_border=False
    table.title="Emoji Vending Machine"
    sp.call("clear",shell=True)
    print(table.table)

