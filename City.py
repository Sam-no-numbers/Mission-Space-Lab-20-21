import reverse_geocoder as rg
from ephem import readtle, degree
def getCity():
  name = "ISS"
  line1 = "1 25544U 98067A   20316.41516162  .00001589  00000+0  36499-4 0  9995"
  line2 = "2 25544  51.6454 339.9628 0001882  94.8340 265.2864 15.49409479254842"

  iss = readtle(name, line1, line2)
  iss.compute()

  pos = (iss.sublat / degree, iss.sublong / degree)

  location = rg.search(pos)
  print(location)
