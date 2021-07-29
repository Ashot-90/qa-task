## Solution for running test-case on 'www.vinted.de' and 'www.vinted.co.uk' portals
## -------------------------------------------------------------

### Local Run
#### You should already have below ones installed
 * 'python3' and 'pip3'
 * 'google-chrome' and 'chromedriver'
 * 'firefox' and 'geckodriver'  
 * 'allure'

#### Install current project requirements
* pip3 install -r requirements.txt
#### Then run './run_tests.sh' with below parameters
#### Input parameters:
* [ -portal | -po ]
    *  Portal. Default : 'DE'.
    *  Enum 'DE | UK'.
* [ -parallel | -pa ]
    * Run Mode. Default : 'true'.
    * Enum 'true | false'.
* [ -browser | -b ]
    * Browser. Default : Chrome.
    * Enum 'Chrome | Firefox'. 
#### Run script:
Examples:
```
./run_tests.sh -portal 'UK' -browser 'Chrome' -parallel true
./run_tests.sh -portal 'UK' -browser 'Firefox' -parallel false
```
## -------------------------------------------------------------
### Docker RUN
##### You should already have below ones installed
 * 'docker'
#### Run
```
docker run -it -v --env BROWSER=Firefox --env PORTAL='DE' --env PARALLEL=true ashot90docker/qa-task
```
## -------------------------------------------------------------