###### Q1#########
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
    
##שיטת המיתר
def secant(f,start_point,end_point ,N):
    if f(start_point) * f(end_point) >= 0:
        print("Secant method fails.")
        return None
    a_n = start_point
    b_n = end_point
    for n in range(1, N + 1):
        m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))



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
    for i in range(-31, 10, 1):
        if(F(i/10)*F(i/10+0.15)<0):
            print('soultuin by bisection')
            bisection(F,i/10,i/10+0.15)
            print('soultuin by secant')
            print(secant(F,1,i/10,10))
    print("simpson with question 1 function between 0 to 1 = " , simpson(0,1,5,F))
    print("Romberg with question 1 function between 0 to 1 = " , romberg(F,0,1,1))

##main

F = lambda x: (math.sin(x**2+5*x+6)/2*math.e**-x)
DF = lambda x: (0.5*math.e**x)*(math.cos(x**2+6+5*x)*(5+2*x))+(math.sin(x**2+6+5*x))
play()




