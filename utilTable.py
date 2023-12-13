import random  
import string
"""
Module description: implement class utilTable.
Purpose: for python table tests, provide some handy methods to: 
--- table_gen_randam(self, rows, cols, width_range=(1,6) )
--- 
Terms :table, rows, columns, cell, cellWidth, rowWidth
table headers (column headers), row headers
"""

class utilTable():
    def __init__(self) -> None:
        pass    
    
    def cell_jusify(self, cellStr, width, mode="Right"):
        ll = len(cellStr)
        rcStr = ''
        if mode.lower() == "right" :
            rcStr = ' ' * ( width - ll) + cellStr;
        elif mode.lower() == "left" :
            rcStr = cellStr + ' ' * ( width - ll )
        else :
            head = int ( ( width - ll ) / 2 )
            tail = width - ll - head
            rcStr = ' ' * head + cellStr + " " * tail
        
        return rcStr;
            

    def row_output(self, lstCell, lstCellWidth, mode="Right"):
        rcRow =''
        for i in range(len(lstCell)) :
            item = lstCell[i]
            wid = lstCellWidth[i]
            rcRow += self.cell_jusify(item, wid, mode)
        
        return rcRow
        
    def table_output(self, lstRows, lstColumnWidth, mode="Right") :
        rcStr = ''
        for r in lstRows:
            rcStr += self.row_output(r, lstColumnWidth, mode) + '\n';   
        
        return rcStr

    def getIdealLstColumnWidth(self, table):
            """
            return: list of width of each column
            how to set the ideal width of each column? the answer is to find thd MAX width of all cell in the column, then add 2,
            so that the interval of two consecutive columns is assured in some extreme conditions
            """
            lstWid = [0] * len(table[0]) 
            
            for r in table:
                for i, pair in enumerate(list(zip(lstWid, r))):
                    w, cell = pair
                    lstWid[i] = max(w, len(cell))
            for i in range(len(lstWid)):
                lstWid[i] += 2;  
        
            return lstWid
        
    def table_gen_randam(self, rows, cols, width_range=(1,6) ):
        lst_tab = []
        ascii = string.ascii_letters
        for row in range(rows):
            lst_row =[]
            for col in range(cols):
                cell =''
                wid = random.randint(width_range[0], width_range[1])   
                for i in range(wid):
                    idx = random.randint(0,len(ascii)-1)
                    cell += ascii[idx]
                lst_row.append(cell)
            lst_tab.append(lst_row)
        return lst_tab


if __name__ == "__main__":
    """
    default to generate a 10-row 6-col table
    the cell contents are randomly generation
    then determine the ideal width for each column by finding the maximun width of all cells in this column, plus 2
    finally print the table
    """
    
    usage ="""
    Usage: python utilTable.py 15 8
    Here means 15-row 8-column
    if not specified, the table will be 10-row 6-column
    
    """
    print(usage)
    
    import sys
    
    rows, cols = 10, 6
    
    if(len(sys.argv)==3):
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
    
    if rows > 20 :
        rows = 10
        print(f" row number out of limit, rows is {rows}")
    if cols > 20 or cols < 2 :
        cols = 6
        print(f" column number out of limit, columns will be {cols}")
        
    ut = utilTable()

    tab = ut.table_gen_randam(rows, cols)
    lstWid = ut.getIdealLstColumnWidth(tab)
    print( ut.table_output(tab, lstWid, 'right') )
