import random
from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.SPP import SPP
import numpy
import math

cell_cols = {0:[0,1.0,0], 1:[1.0,0,0]}
outfile = 'all.csv'

def setup(sim):
    sim.dt = 0.025
    # Set biophysics, signalling, and regulation models
    biophys = SPP(z_axis_c=False, dt_c=0.01)

    # use this file for reg too
    regul = ModuleRegulator(sim, sim.moduleName)
    # Only biophys and regulation
    sim.init(biophys, regul, None, None)
 
    # Specify the initial cell and its location in the simulation
    a = 1 / numpy.sqrt(2)
    sim.addCell(cellType=0, pos=(-3,0,0), dir=(a, a, 0))
    sim.addCell(cellType=1, pos=(3,0,0), dir=(-a, a, 0))
    sim.addCell(cellType=1, pos=(3,3,0), dir=(-0.1, numpy.sqrt(1-0.1**2), 0))
    sim.addCell(cellType=1, pos=(0,-3,0), dir=(0.1, numpy.sqrt(1-0.1**2), 0))
    sim.addCell(cellType=1, pos=(0,3,0), dir=(-0.5, numpy.sqrt(3/4), 0))
    biophys.addPlane(0, 5, 0, 0, -1, 0)

    # Add some objects to draw the models
    #if sim.is_gui:
    from CellModeller.GUI import Renderers
    therenderer = Renderers.GLSphereRenderer(sim)
    sim.addRenderer(therenderer)
    #else:
    #    print("Running in batch mode: no display will be output")

    sim.pickleSteps = 10
    sim.saveOutput = True

def init(cell):
    # Specify mean and distribution of initial cell size
    cell.targetVol = 3.5 + random.uniform(0.0,0.5)
    # Specify growth rate of cells
    cell.growthRate = 1. 
    cell.color = cell_cols[cell.cellType]

def update(cells):
    pass

def divide(parent, d1, d2):
    pass
# def update(cells):
#     #Iterate through each cell and flag cells that reach target size for division
#     for (id, cell) in cells.items():
#         if cell.volume > cell.targetVol:
#             cell.divideFlag = True
# 
#         gr = cell.strainRate/0.05
#         cgr = gr - 0.5
#         # Return value is tuple of colors, (fill, stroke)
#         #if cgr>0:
#         #    cell.color = [1, 1-cgr*2, 1-cgr*2]
#         #else:
#         #    cell.color = [1+cgr*2, 1+cgr*2, 1]
# 
# 
# def divide(parent, d1, d2):
#     # Specify target cell size that triggers cell division
#     d1.targetVol = 3.5 + random.uniform(0.0,0.5)
#     d2.targetVol = 3.5 + random.uniform(0.0,0.5)
# 