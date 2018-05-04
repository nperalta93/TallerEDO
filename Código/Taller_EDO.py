import matplotlib.pyplot as plt

x=0.
y=1.
z=2.
h=0.1
print ('z', '\t', 'x', '\t', '\t', 'y', '\n')
print (z, '\t', '\t', x, '\t', '\t', y)

while(z<5):
  m1=(x)+(y)+(z)
  k1=-(x)+(y)-(z)
  fz2=z+(h/2.)
  fx2=x+(h/2.)*m1
  fy2=y+(h/2.)*k1
  m2=(fx2)+(fy2)+(fz2)
  gz2=z+(h/2.)
  gx2=x+(h/2.)*m1
  gy2=y+(h/2.)*k1
  k2=-(gx2)+(gy2)-(gz2)
  fz3=z+(h/2.)
  fx3=x+(h/2.)*m2
  fy3=y+(h/2.)*k2
  m3=(fx3)+(fy3)+(fz3)
  gz3=z+(h/2.)
  gx3=x+(h/2.)*m2
  gy3=y+(h/2.)*k2
  k3=-(gx3)+(gy3)-(gz3)
  fz4=z+h
  fx4=x+h*m3
  fy4=y+h*k3
  m4=(fx4)+(fy4)+(fz4)
  gz4=z+h
  gx4=x+h*m3
  gy4=y+h*k3
  k4=-(gx4)+(gy4)-(gz4)
  z=z+h
  x=x+(h/6.)*(m1+(2.*m2)+(2.*m3)+m4)
  y=y+(h/6.)*(k1+(2.*k2)+(2.*k3)+k4)
  print (z, '\t', '\t', x, '\t', y)
  plt.plot(z, x, 'rs')
  plt.plot(z, y, 'bs')

plt.show()