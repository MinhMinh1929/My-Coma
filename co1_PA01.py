def roots ( a1,a2,a3,b1,b2,b3):
   # f(x) = a1*x^2 + a2*x + a3
   # g(x) = b1*x^2 + b2*x + b3
   # h(x) = x^5
   # f(x)*g(x)+h(x) = x^5 + c1x^4 + c2x^3 + c3x^2 + c4x + c5
   c1 = a1*b1
   c2 = a1*b2 + a2*b1
   c3 = a1*b3 + a2*b2 + a3*b1
   c4 = a2*b3 + a3*b2
   c5 = a3*b3
   polynome  = [1, c1,c2,c3,c4,c5]
   count = 0
   for i in range (len(polynome)):
      if polynome[i]<0:
         count =+ 1
   if count % 2== 0 :
      print("Das Polynom hat eine gerade Anzahl von positiven reellen Nullstellen")

   else:
      print("Das polynom hat eine ungerade Anzahl von positiven reellen Nullstellen")

# Beispielaufrufe:
roots(1,-2,-1,2,1,2)
roots(0,0,0,0,0,0)







