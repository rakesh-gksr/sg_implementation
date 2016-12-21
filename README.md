# Selenium Grid Demo

This contains full demo on how to integrate Selenium grid in your python project. 

#Basic Information
Selenium-Grid allows you run your tests on different machines against different browsers in parallel.

#Assumption

1. selenium-server-standalone-3.0.1.jar

Java is installed and java executable is on your execution path. Check below command to see java is installed or not

$ java -version

java version "1.8.0_111"
Java(TM) SE Runtime Environment (build 1.8.0_111-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.111-b14, mixed mode)

2. ChromeDriver

Chromedriver is installed and it is available on your execution path. Check below command to see java is installed or not

$ chromedriver -version

ChromeDriver 2.26.436421 (6c1a3ab469ad86fd49c8d97ede4a6b96a49ca5f6)


#Documentation:

Please find the full documentation on google drive : https://docs.google.com/document/d/1csquRGiRWlasPpt0o73F6GJ5Z-SaSA6VZiJDJ_B1hwo/edit#

#Grid Demo Setup

Please download the shell script that will automatically install and configure Selenium grid demo environment.
https://drive.google.com/file/d/0BzlCuRVCDu-YSTh4Mmg3ekRjNkk/view?ts=585a5547

Run following command once you downloaded the shell script

$ sh PATH_TO_GIT_REPO/grid_implementation/selenium_grid_demo.sh

Once you successully setup the Demo then following are the steps to run the test cases on grid:

1. Start the Hub (Please see the command to start hub in the google sheet SurveyMonkey- Grid Implementation)
2. Registere the Nodes (Please see the command to register the node to hub in the google sheet SurveyMonkey- Grid Implementation)
3. $ cd ~/Grid_Demo/
4. $ source bin/activate
5. $ cd sg_implementation
6. Open the test_script.py file and replace the hub address as per hub address generated on your box. Save the file.
7. By default, following command run the test cases from test_script.py on firefox browser.
$ py.test -v -s test_script.py
8. Run test cases on google chrome
$ py.test -v -s test_script.py --browser=chrome
9. Run test cases on google chrome
$ py.test -v -s test_script.py --browser=firefox

Please let me know if you face any issues.

Thanks & Regards,

Rakesh jain
