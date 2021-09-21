from osgeo import gdal
import numpy
import numpy.random

# Make a raster with a RAT on import.
driver = gdal.GetDriverByName('GTiff')
raster = driver.Create(
    'raster.tif', 5, 5, 1, gdal.GDT_Byte)

band = raster.GetRasterBand(1)
array = numpy.repeat(
    numpy.linspace(0, 4, 5), 5).reshape((5,5)).astype(numpy.int8)
band.WriteArray(array)
values = numpy.unique(array)
random_values = numpy.random.randint(0, 5)

# Create and populate the RAT
rat = gdal.RasterAttributeTable()
rat.CreateColumn('VALUE', gdal.GFT_Integer, gdal.GFU_Generic)
rat.CreateColumn('RANDOM', gdal.GFT_Integer, gdal.GFU_Generic)
for i, value in enumerate(values):
    rat.SetValueAsInt(i, 0, int(value))
    rat.SetValueAsInt(i, 1, numpy.random.randint(0, 5))

# Associate with the band
raster.FlushCache()
band.SetDefaultRAT(rat)
