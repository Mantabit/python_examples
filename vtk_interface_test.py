import numpy
from vtk import vtkXMLUnstructuredGridReader
from vtk.util import numpy_support as VN

reader = vtkXMLUnstructuredGridReader()
reader.SetFileName("charged_wire.vtu")
reader.Update()
data = reader.GetOutput()
potential = data.GetPointData().GetScalars("potential")

print(type(potential))