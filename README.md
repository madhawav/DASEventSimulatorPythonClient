# WSO2 DAS 4.0 Python Client
Python Client for WSO2 DAS 4.0 (In Development Version)

This repository is part of the project [Python API for Siddhi CEP](https://gist.github.com/madhawav/195b7dc601d94c40958d88be1d56e705). For more details on complete scope of the project, visit the project gist at link above.

This repository is currently a work in progress, as a project for Google Summer of Code 2017 Program.

# Current Progress
- [x] Python Client on DAS 4.0 Event Simulator.
- [x] Python Client on DAS 4.0 via REST API.
- [ ] Python Client on DAS 3.1 via SOAP API.

Installing the Library from Source
-----
1. Install pre-requisites mentioned below.
    - WSO2 Data Analytics Server 4.0 (see `Running the Tests` section for installation instructions)
    - Python 2.7+ or Python 3.3+
    - Requests for Python (`pip install requests`)
    - Future for Python (`pip install future`)
    - Enum34 for Python if Python 3.3 is used (`pip install enum34`)
2. Install using Setup.py.
    - Clone the GitHub Repository.
    - Navigate to project root and run `sudo pip install .`
3. Run WSO2 DAS 4.0 worker.
    - Clone and Compile WSO2 DAS 4.0 from Source. (refer `Running the Tests` section for instructions)
    - Navigate to `DAS_Home/bin/` and run `sh worker.sh`.

4. Use the Library using Python.
    ```python
    from DAS4PythonAPI.DAS4PythonClient import DAS4PythonClient
    dasPythonClient = DAS4PythonClient('http://localhost:9090')
    siddhiAppManagerClient = dasPythonClient.getSiddhiAppManagementClient()

    status = siddhiAppManagerClient.retrieveStatusSiddhiApp("TestSiddhiApp")
    ```
    *Refer Tests to get more familiar with library functionality.

Creating deployment wheel (for Any Platform)
-----
1. Install pre-requisites mentioned in `Installing the Library from Source` section.
2. Delete directory `build` if exist. 
3. Goto source root and run `python setup.py bdist_wheel`

Installing deployment wheel 
-----
1. Make sure all pre-requisites are installed. 
2. Install python wheel using `pip install [path_to_wheel_file]`.

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

Contributors
-----
* __Madhawa Vidanapathirana__
   - Email: madhawavidanapathirana@gmail.com
   - Organization: University of Moratuwa

__Developer Mail Thread__: dev@wso2.org
