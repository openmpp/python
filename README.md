# [OpenM++](http://www.openmpp.org/) integration with Python

This repository is a part of [OpenM++](http://www.openmpp.org/) open source microsimulation platform. It contain examples how to prepare input data, run the model and process results using Python.

Please keep in mind, it is an examples only and some important details, like error handling, intentionally omitted. It is necessary to add `try ... except` if want to use it in production.

For more information visit our [wiki](http://www.openmpp.org/wiki/) or e-mail to: _openmpp dot org at gmail dot com_.

## Prerequisites

Python scripts are using openM++ web-service in order to run the model, modify parameters and read output values. No installation required, just download [latest release of openM++](https://github.com/openmpp/main/releases/latest), unpack it into any directory and start `oms.exe`:

Windows:
```
cd C:\my-openmpp-release
bin\ompp_ui.bat
```
Linux / MacOS:
```
cd ~/my-openmpp-release
bin/oms
```
As result `oms` web-service will start to listen incoming requests on `http://localhost:4040` and Python script will do all actions using [oms web-service API](https://ompp.sourceforge.io/wiki/index.php/Oms_web_service_API).

## Screenshots

**NewCaseBased** model:  loop over MortalityHazard parameter to analyze DurationOfLife output value.

![Example of NewCaseBased model run.](https://github.com/openmpp/python/blob/master/images/openmpp_Python_life_vs_mortality_20200505.png "Example of NewCaseBased model run.")

**RiskPaths** model: analyze contribution of delayed union formations versus decreased fertility on childlessness.

![Example of RiskPaths model run.](/images/openmpp_Python_riskpaths_childlessness_20200505.png "Example of RiskPaths model run.")

