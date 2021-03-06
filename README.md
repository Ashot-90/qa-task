## Solution for running test-cases
## -------------------------------------------------------------
### Docker Run (Working with Firefox ONLY)
##### You should already have below ones installed
 * 'docker'
#### Run
```
cd $ClonedDirectory
docker build -f Dockerfile -t qa-task .
docker run -it -v $(pwd):/app/ -w /app/ --env BROWSER=Firefox --env PORTAL='DE' --env PARALLEL=true qa-task
docker run -it -v $(pwd):/app/ -w /app/ --env BROWSER=Firefox --env PORTAL='UK' --env PARALLEL=false qa-task
```
## -------------------------------------------------------------
### Local Run
#### You should already have below ones installed
```
 * 'python3' and 'pip3' (python version >= 3.8)
 * 'google-chrome' and 'chromedriver'
 * 'firefox' and 'geckodriver'  
 * 'allure'
```
#### Install current project requirements
```
* pip3 install -r requirements.txt
```
#### Then run './run_tests.sh' with below parameters
#### Input parameters:
```
* [ -portal | -po ]
    *  Portal. Default : 'DE'.
    *  Enum 'DE | UK'.
* [ -parallel | -pa ]
    * Run Mode. Default : 'true'.
    * Enum 'true | false'.
* [ -browser | -b ]
    * Browser. Default : Chrome.
    * Enum 'Chrome | Firefox'. 
```
#### Run script:
Examples:
```
./run_tests.sh -portal 'UK' -browser 'Chrome' -parallel true
./run_tests.sh -portal 'DE' -browser 'Chrome' -parallel false
./run_tests.sh -portal 'UK' -browser 'Firefox' -parallel false
./run_tests.sh -portal 'DE' -browser 'Firefox' -parallel true
```
## -------------------------------------------------------------
#### Allure report will be generated under directory by pattern
```
AllureReport_*
```
## -------------------------------------------------------------
#### Below hierarchy of classes has been used to design code
![Diagram](https://github.com/Ashot-90/qa-task/blob/master/Diagram.jpg?raw=true)
## -------------------------------------------------------------
