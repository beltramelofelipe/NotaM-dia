not1 = float(input("Digite 1° nota: "))
not2 = float(input("Digite 2° nota: "))

media = (not1 + not2) / 2

if (media < 5):
   print("Você está reprovado estude mais! ")

elif (media >= 5 and media <= 6.9):
  print("Você está de recuperação! ")

else:
  print("Você foi aprovado, Parabéns!!!!")


