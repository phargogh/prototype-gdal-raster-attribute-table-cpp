CONDAENV := ./env38
PYTHON := $(CONDAENV)/bin/python

.PHONY: clean cleanall

clean:
	rm -rf  raster.tif showrat

cleanall: clean
	rm -rf $(CONDAENV)

env38:
	conda create -p $(CONDAENV) -c conda-forge -y
	conda env update -p $(CONDAENV) --file=environment.yml

raster.tif:
	$(PYTHON) makeraster.py

showrat:
	gcc -o showrat -I $$CONDA_PREFIX/include -std=c++11 showrat.cpp
