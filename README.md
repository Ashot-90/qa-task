### Solution for running test-case on 'www.vinted.de' and 'www.vinted.co.uk' portals
#### You should already have below ones installed
 * python3
 * pip3
 * chromedriver
 * allure

#### Install current project requirements
* pip3 install -r requirements.txt
#### Then run './run_tests.sh' with below parameters
#### Input parameters:
* [ -portal | -po ]
    *  Portal. Default : 'DE'
    *  Enum 'DE | UK'.
* [ -parallel | -pa ]
    * Run Mode. Default : sequential
    * Parallel mode will be used if mentioned.
  
#### Run script:
Examples:
```
./run_tests.sh
./run_tests.sh -portal 'DE'
./run_tests.sh -portal 'DE' -parallel
./run_tests.sh -portal 'UK'
./run_tests.sh -portal 'UK' -parallel
```