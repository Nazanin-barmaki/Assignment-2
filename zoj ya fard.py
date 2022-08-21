number = int(input('enter number:'))
zoj = 0
fard = 0

while number > 0:
    number = number//10
    mod = number %10
     
if (mod %2 == 0):
         zoj +=1

 else:
      fard +=1

  if(zoj == fard):
      print('anha barabarand ')

 
     elif ( zoj > fard):
       print (' adad zoj bishtar az adad fard hastand')
       

  else:
      print ('adad fard bishtar az adad zoj hastand')
