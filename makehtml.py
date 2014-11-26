import sys
import os.path
from operator import itemgetter
import csv



backgroundcoloring=0;


#read and open files
fo=open('index.html','w')
f=open('volumes.csv','rU')
lines=f.readlines()

letters='ABCDEFGH'


# write beginning of header
fo.write('<script language="JavaScript">\n<!--\n')


#find the order from lowest to highest 
values=[];
for r,line in enumerate(lines):
	row = line.split(',')
	for c,element in enumerate(row):
		values.append(float(element))
		wellorder=[i[0] for i in sorted(enumerate(values), key=lambda x:x[1])]


#record order as a variable which javascript will interact with
fo.write('var wellorder = [')
reversewellorder=wellorder[::-1]
for i in range(0,95):
	fo.write(str(reversewellorder[i])+',')
fo.write(str(reversewellorder[95])+'];\n')


# write rest of header by copying from old file
h=open('header.html','r')
lines=h.readlines()
for line in lines:
	fo.write(line)

# make top row of table
fo.write('<tr valign="top">\n')	
fo.write('<td class = "td" style="background-color:rgb(255,255,255)" >  </td>\n')
for c in range(0,12):
	fo.write('<td class = "column-label" style="background-color:rgb(255,255,255)" > %s  </td>\n'%(str(c+1)))

# make rest of table table
k=0;
for r in range(0,8):
	fo.write('<tr valign="top">\n')	
	fo.write('<td class = "row-label" style="background-color:rgb(255,255,255)" > %s   </td>\n'%(letters[r]))
	for c in range(0,12):
		value=values[k]
		order=wellorder.index(k);
		if backgroundcoloring==1:	
			rawcolor=int(255-(1.3*order))
			color=str(rawcolor)+','+str(rawcolor)+','+str(rawcolor)
		elif value < 0.01:
			color='0,0,0'
		else:
			color='255,255,255'
		if (c==4 or c==8) and r==3:
			fo.write('<td class = "border-both" style="background-color:rgb(%s);" > <a href="#" onClick="javascript:changeBGC(%s)">%s</a>   </td>\n'%(color,str(k),value))
		elif c==4 or c==8:
			fo.write('<td class = "border-side" style="background-color:rgb(%s);" > <a href="#" onClick="javascript:changeBGC(%s)">%s</a>   </td>\n'%(color,str(k),value))
		elif r==3:
			fo.write('<td class = "border-bottom" style="background-color:rgb(%s);" > <a href="#" onClick="javascript:changeBGC(%s)">%s</a>   </td>\n'%(color,str(k),value))
		else:
			fo.write('<td class = "td" style="background-color:rgb(%s);" > <a href="#" onClick="javascript:changeBGC(%s)">%s</a>   </td>\n'%(color,str(k),value))
		k=k+1
			
			
fo.write('</tr>\n </table>\n</div>\n</body>\n</html>')
