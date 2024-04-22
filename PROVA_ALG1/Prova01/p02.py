a=8*10**4
b=2*10**5
anos=0
while (a<=b):
    a=(a*(3*10**-2))+a
    b=(b*(15*10**-3))+b
    anos+=1
print(f'Para que a população da Cidade A se iguale a da Cidade B, levara {anos}anos.\n'
      f'E para que a polulação da Cidade A ultrapasse a da Cidade B, levara {anos+1}anos.')