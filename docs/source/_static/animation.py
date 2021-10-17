from ase.build import molecule
from batoms import Batoms
atoms = molecule('C2H6SO')
images = []
for i in range(20):
    temp = atoms.copy()
    temp.rotate(18*i, 'z')
    images.append(temp)

c2h6so = Batoms(label = 'c2h6so', atoms = images)
c2h6so.load_frames()
c2h6so.render.run(animation = True)
