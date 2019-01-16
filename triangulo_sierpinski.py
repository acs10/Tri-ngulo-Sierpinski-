
def fatorial(x):
    cont = 1
    for i in range(1,x+1):
        if x==1 or x==0:
            return cont
        else:
            cont = cont*i
    return cont
arq = open("codigo.html", "w")
def pascal(x):
    linha = 0
    while linha < x:
        arq.write('<table align="center">')
        arq.write("<tr>")
        for i in range(linha+1):
            
            line = (round(fatorial(linha)/(fatorial(i)*(fatorial(linha-i)))))
            if line %2 == 0:
                arq.write("<th>" + str(line) + "</th>")
            else:
                arq.write('<th bgcolor="orange">' + str(line) + "</th>")
            
        linha+=1
        arq.write("</tr>")
        arq.write('</table>')
            

pascal(9)

arq.close()
