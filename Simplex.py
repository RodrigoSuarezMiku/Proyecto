# Proyecto
# Declaro las matices y arreglos que necesitare para poder utilizarlos
M=[]
M2=[]
Lx1=[]
Lx2=[]
Lsol=[]
#Agrego X1 y X2 al mismo tiempo las igualo a cero o las ago negativo
x1=float(input("Dame el valor de x1: "))
x1=x1*-1
Lx1.append(x1)
x2=float(input("Dame el valor de x2: "))
x2=x2*-1
Lx2.append(x2)

#Pedimos restricciones
rest=int(input("Cuantas restrincciones son: "))

#Pedimos y agregamos restricciones
for i in range(rest):
    x1 = float(input("Dame el valor de x1: "))
    Lx1.append(x1)
    x2 = float(input("Dame el valor de x2: "))
    Lx2.append(x2)
    sol = float(input("Dame el valor de sol: "))
    Lsol.append(sol)

#Definimos las filas y columnas, se le suman 4 a las columnas ya que sera Z, X1 ect de igual manera las filas
fil=rest+1
col=rest+4

#LLenamos las matrices con 0
for i in range(fil):
    M.append([0]*col)

for i in range(fil):
    M2.append([0] * col)

#Llenamos las matrices con los valores correspondientes

#Guardo Z
M[0][0]=1
f=fil-1
#cx1=0

#Guardamos lo que seria x1 y x2
for i in range(fil):
    M[i][1]=Lx1[i]
    M[i][2]=Lx2[i]

#Guardamos o le asignamos valor de 1 las variables de holgura en la matriz
cl=3
fl=1
c=col-1
while cl<c:
    M[fl][cl]=1
    fl=fl+1
    cl=cl+1

#Guardamos las soluciones
sl=0
f2=1
fn=fil-1
while f2<=fn:
    M[f2][c]=Lsol[sl]
    f2=f2+1
    sl=sl+1

print ".--.--.--.--.--.--.--.--.--.--.--."

#Imprimimos la Matriz
for i in range(fil):
    for j in range(col):
        print M[i][j],
    print " \n "
print "--------------------------------------------------"

# Entramos a hacer el simplex
repet=False
while repet==False:
    #Sacamos la variable mas negativa y menor la que entrara
    vare=0
    if M[0][1] < M[0][2]:
        vare=1
    if M[0][2] < M[0][1]:
        vare=2
    print ".-.-.-.-.-.-.-.-.-"
    print "vare", vare

    #Sacamos las variable saliente
    vars=0
    vm=0
    varm=9999
    d=1
    while d <= f:
        if M[d][vare] != 0 and M[d][vare]>0:
            r = M[d][c] / M[d][vare]
            if r<varm:
                varm=r
                vm=M[d][vare]
                vars=d
        d=d+1
    #Un print para verificar si esta tomando los datos correspondientes
    print ".-.-.-.-.-.-.-.-.-"
    print "vars", vars ,"varm", vm

    #Siguiente Sacamos el NRP
    for i in range(col):
        M2[vars][i]=M[vars][i]/vm

    #llenamos la segunda matriz
    for i in range(fil):
        div=M[i][vare]
        if i != vars:
            for j in range(col):
                M2[i][j] = M[i][j] - (div * M2[vars][j])

    #Rellenamos la matriz original
    for i in range(fil):
        for j in range(col):
            M[i][j]=M2[i][j]

    print ".-.-.-.-.-.-.-.-.-"
    # Imprimimos la Matriz
    for i in range(fil):
        for j in range(col):
            print M[i][j],
        print " \n "
    print "======================================"

    # Comparacion para Ver si termina
    sx=0
    sxx=0
    sx1 =0
    sx2=0
    #Sumamos los valores de la colimna x1 y x2
    for i in range(fil):
        sx1=sx1+M[i][1]
        if M[i][1]==1:
            sx=i
        sx2=sx2+M[i][2]
        if M[i][2]==1:
            sxx=i
    #Se hace una comparacion si la suma de las columnas x1 y x2 da a 1 ademas de mandar los resultados a pantalla
    if sx1==1 and sx2==1:
        print "Soluccion"
        print "x1=", M[sx][c]
        print "X2=", M[sxx][c]
        print "sol=", M[0][c]
        repet=True
