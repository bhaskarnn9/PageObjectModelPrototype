echo '****** Starting tests ******'
echo 'Clearing old reports'
rm -rf Results/*.html
echo 'Done clearing old reports'
echo 'installing required packages'
echo 'Tring to install: get-project-root'
yes | pip install get-project-root
echo 'Tring to install: html-testrunner'
yes | pip install html-testrunner
echo 'Tring to install: selenium'
yes | pip install selenium
echo 'Invoking UI Tests'
Sleep 2
python3 Test/TestSuite/TestRunner.py
echo 'Generating HTML report...'
sleep 3
echo 'Opening HTML report...'
sleep 1
echo 'Opening HTML report...'
echo '****** Tests Ended ******'
open Results/*.html