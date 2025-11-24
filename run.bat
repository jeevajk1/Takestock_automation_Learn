@echo off
echo Running PyTest Regression Suite...

pytest -s -v -m "regression" --html=Reports/report.html testCase/ --browser chrome

echo Test Execution Completed.
pause
