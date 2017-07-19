# DAS Event Simulator Python Client
Python Client for WSO2 DAS 4.0 (In Development Version)

This repository is part of the project [Siddhi CEP Python API](https://github.com/madhawav/SiddhiCEPPythonAPI). For more details on complete scope of the project, visit the main project repository at link above.

This is currently a work in progress, as a project for Google Summer of Code 2017 Program.

Note: Currently, the event simulator of WSO2 DAS 4.0 has been wrapped.

# Current Progress
- [x] Python Client on DAS 4.0 Event Simulator.
- [ ] Python Client on DAS 4.0 via REST API.
- [ ] Python Client on DAS 3.1 via SOAP API.

# Prerequisites
- WSO2 Data Analytics Server 4.0 (see `Running the Tests` section for installation instructions)
- Python3 (Python2.7 will be supported in future)
- Requests for Python3 (`pip3 install requests`)

# Running the Tests
Make sure all prerequisites are met before proceeding with tests.

1) Clone the DASPythonClient Repository (this repository) to a suitable location. (say `DASPythonClient`).
2) Clone and Compile WSO2 DAS 4.0 from Source
 - Clone WSO2 DAS 4.0 from [Github Repository](https://github.com/wso2/product-das).
 - Compile the code via Maven (`mvn install` from source root).
 - Extract `product-das/modules/distribution/target/wso2das-4.0.0-SNAPSHOT.zip` to a suitable location (say `DAS_HOME`).
3) Run WSO2 DAS 4.0 worker.
 - Navigate to `DAS_Home/bin/` and run `sh worker.sh`.
4) Run Tests.
 - Append `DASPythonClient` to `PYTHONPATH` environment variable. (`export PYTHONPATH=$PYTHONPATH:DASPythonClient`)
 - Run python scripts in `DASPythonClient/Tests/` from working directory as `DASPythonClient` (`python3 Tests/EventSimulatorTests.py`)
 
# Background

WSO2 Data Analytics Server (WSO2 DAS) is an Enterprise Grade Open Source Data Analytics Solution developed by WSO2 Inc. Siddhi is a Query Language and a Library for Realtime Complex Event Processing, which is used by WSO2 DAS for Streaming Event Processing.

Further information on above products are available in the links below.

* WSO2 Data Analytics Server 4.0 (In Development Version)
  - GitHub - https://github.com/wso2/product-das
  - Documentation - https://docs.wso2.com/display/DAS400/Quick+Start+Guide
* Siddhi 4.0 Library (In Development Version)
  - GitHub - https://github.com/wso2/siddhi

# Contact

Madhawa - madhawavidanapathirana@gmail.com

#GSoC2017 #WSO2
