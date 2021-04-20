# [OpenM++](http://www.openmpp.org/) integration with Python

This repository is a part of [OpenM++](http://www.openmpp.org/) open source microsimulation platform. It contain examples how to prepare input data, run the model and process results using Python.

Please keep in mind, it is an examples only and some important details, like error handling, intentionally omitted. It is highly recommended to use `try ... except` in production code.

For more information visit our [wiki](https://github.com/openmpp/openmpp.github.io/wiki) or e-mail to: _openmpp dot org at gmail dot com_.

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
As result `oms` web-service will start to listen incoming requests on `http://localhost:4040` and Python script will
do all actions using [oms web-service API](https://github.com/openmpp/openmpp.github.io/wiki/Oms-web-service-API).

## Screenshots

**NewCaseBased** model:  loop over MortalityHazard parameter to analyze DurationOfLife output value.

![Example of NewCaseBased model run.](/images/openmpp_Python_life_vs_mortality_20200505.png "Example of NewCaseBased model run.")

**RiskPaths** model: analyze contribution of delayed union formations versus decreased fertility on childlessness.

![Example of RiskPaths model run.](/images/openmpp_Python_riskpaths_childlessness_20200505.png "Example of RiskPaths model run.")

**License:** MIT.
