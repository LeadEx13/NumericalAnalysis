###### Q10#########
import math
from datetime import datetime
epsilon = 0.0001
calculation_time = f"{datetime.now().day}{datetime.now().time().hour}{datetime.now().time().minute}"
 ## חצייה
def bisection(f,start_point ,end_point):
    if f(start_point )*f(end_point ) >= 0:
        print("Bisection method fails.")
        return None
    a_n = start_point
    b_n = end_point
    while (b_n-a_n) > epsilon:
        m_n = (a_n + b_n)/2
        print(f"{m_n}00000{calculation_time}")
        f_m_n = f(m_n)

        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n

        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2
##ניוטון  רפסון
def newton(f,Df,x0,max_iter):

    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
        print(f"{xn}00000{calculation_time}")
    print('Exceeded maximum iterations. No solution found.')
    return None

def simpson(a, b, n, f):
   sum = 0
   inc = (b - a) / n
   for k in range(n + 1):
      x = a + (k * inc)
      summand = f(x)
      if (k != 0) and (k != n):
          summand *= (2 + (2 * (k % 2)))
      sum += summand
   return ((b - a) / (3 * n)) * sum


def romberg(f,a,b,n):
    r = []
    h = (b - a)
    r.append([(h/2.0)*(f(a)+f(b))])
    for i in range(1,n+1):
        h = h/2.
    sum = 0
    for k in range(1,2**i ,2):
       sum = sum + f(a+k*h)
    rowi = [0.5*r[ i-1][0] + sum*h]
    for j in range(1,i+1):
       rij = rowi[j-1] + (rowi[j-1]-r[i-1][j-1])/(4.**j-1.)
    rowi.append(rij)
    r.append(rowi)
    return rij

## play
def play():
    for i in range(0, 15, 1):
        if(i<1):
            i+=0.0001
        if(F(i/10)*F(i/10+0.1)<0):
            print('soultuin by bisection')
            bisection(F,i/10,i/10+0.5)
            print('soultuin by Newton Rapson')
            print(f"{newton(F,DF,i/10,55)}00000{calculation_time}")
    print(f"simpson with question 10 function between 0.5 to 1 = {simpson(0.5,1,20,F)}00000{calculation_time}")
    print(f"Romberg with question 10 function between 0.5 to 1 = {romberg(F,0.5,1,1)}00000{calculation_time}")

##main

F = lambda x: (x*math.e**-x+math.log(x**2))*(2*x**3+2*x**2-3*x-5)
DF = lambda x: (math.e**-x-math.e**-x+2/x)*(2*x**3+2*x**2-3*x-5)+\
               (6*x**2+4*x-3)*(x*math.e**-x+math.log(x**2))
play()



