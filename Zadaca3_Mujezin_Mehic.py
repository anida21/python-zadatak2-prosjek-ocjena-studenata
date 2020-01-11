def lista():
  nesto = True
  imena=['Marko','Ahmed','Merisa']

  print("U listi se nalaze sljedeci studenti: ")

  print("'" + imena[0] + "', " + "'" + imena[1] + "', " + "'" + imena[2] + "'")

  while(nesto == True):

    a = input("Da li zelite unijeti jos nekog studenta? da/ne: ")

    if(a == "da"):

      imestudenta = input("Unesite ime studenta: ")

      imena.append(imestudenta)
    elif(a == "ne"):
      nesto = False
  print( ", ".join( repr(e) for e in imena ) )


  class Student():
    def __init__(self,usmeni,pismeni,prosjek):
      self.usmeni=usmeni
      self.pismeni=pismeni
      self.prosjek=prosjek
    def Prosjeci(self):
      print("{0}" .format(self.prosjek))

  prosjek = {}
  nesto = True
  usmeniIspit = 0
  pismeniIspit = 0
  a = len(imena)
  for i in range (a):
    print("Unesite ocjenu koju je student",imena[i],"ostvario na usmenom ispitu: ")
    while nesto:
      usmeni = int(input())
      if int(usmeni) < 5 or int(usmeni) > 10:
        print("Morate unijeti broj od 5-10 za vrijednost ocijene!")
      else:
        nesto = False
        usmeniIspit = usmeni
    nesto = True

    print("Unesite ocjenu koju je student",imena[i],"ostvario na pismenom ispitu: ")
    while nesto:

      pismeni = int(input())
      if int(pismeni) < 5 or int(pismeni) > 10:
        print("Morate unijeti broj od 5-10 za vrijednost ocijene!")
      else:
        nesto = False
        pismeniIspit = pismeni
    nesto = True

    if int(usmeniIspit) == 5 or int(pismeniIspit) == 5:
      p = 5.0
      prosjek.update({imena[i]: p})
    else:
      p = (usmeni+pismeni)/2
      prosjek.update({imena[i]: p})

  b=len(imena)
  print("Lista studenata sa ocjenama:")
  for i in range (b):
    print(imena[i],":",end=" ")
    print(prosjek.get(imena[i]))
