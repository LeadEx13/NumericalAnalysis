###### Q11#########
import math
epsilon = 0.0001
 ## חצייה
def bisection(f,start_point ,end_point):
    if f(start_point )*f(end_point ) >= 0:
        print("Bisection method fails.")
        return None
    a_n = start_point
    b_n = end_point
    while (b_n-a_n) > epsilon:
        m_n = (a_n + b_n)/2
        print(m_n)
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
        print(xn)
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
 r=[] # the list must be defined before elements can be added
 h = (b - a)
 # Insert R [0,0]
 r.append([(h/2.0)*(f(a)+f(b))])
 for i in range(1,n+1):
     h = h/2.
 sum = 0
 for k in range(1,2**i ,2):
    sum = sum + f(a+k*h)

 # Begin building the next row with R[i ,0]
 rowi = [0.5*r[ i-1][0] + sum*h]
 # Now calculate the rest of the row
 for j in range(1,i+1):
    rij = rowi[j-1] + (rowi[j-1]-r[i-1][j-1])/(4.**j-1.)
 # Add R[i,j ] to rowi
 rowi.append(rij)

 # Add R[i,j ] to r
 r.append(rowi)

 return r

## play
def play():
    for i in range(0, 15, 1):
        if(i<1):
            i+=0.0001
        if(F(i/10)*F(i/10+0.1)<0):
            print('soultuin by bisection')
            bisection(F,i/10,i/10+0.5)
            print('soultuin by Newton Rapson')
            print(newton(F,DF,i/10,55))
    print("simpson with question 11 function between 0.5 to 1 = " , simpson(0.5,1,20,F))
    print("Romberg with question 11 function between 0.5 to 1 = " , romberg(F,0.5,1,1))

##main

F = lambda x: (2*x*math.e**-x+math.log(2*x**2))*(2*x**3+2*x**2-3*x-5)
DF = lambda x: (2*(math.e**-x-math.e**-x+2/x))*(2*x**3+2*x**2-3*x-5)+\
               (6*x**2+4*x-3)*(2*x*math.e**-x+math.log(2*x**2))
play()




