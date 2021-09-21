#include "gdal_priv.h"
#include "cpl_conv.h" // for CPLMalloc()
int main() {
    GDALDataset  *poDataset;
    GDALAllRegister();
    poDataset = (GDALDataset *) GDALOpen( "raster.tif", GA_ReadOnly );
}
