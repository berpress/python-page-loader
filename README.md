[![Build Status](https://travis-ci.org/berpress/python-project-lvl3.svg?branch=master)](https://travis-ci.org/berpress/python-project-lvl3)

[![Test Coverage](https://api.codeclimate.com/v1/badges/af2c5b1f166e9bf74575/test_coverage)](https://codeclimate.com/github/berpress/python-project-lvl3/test_coverage)

[![Maintainability](https://api.codeclimate.com/v1/badges/af2c5b1f166e9bf74575/maintainability)](https://codeclimate.com/github/berpress/python-project-lvl3/maintainability)


### Page loader

1. Install
``` sh
python3 -m pip install --user --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple litovsky-page-loader

```
2. How to use. 

The utility accepts one required parameter as an input - the url of the page to download. As a result, the page is downloaded and local resources are saved, if any.
Example
``` sh
    loader https://hexlet.io/courses
```
To save the page to a specific folder, you must specify the --output parameter. If the --output option is not specified, a temporary folder will be created.

To manage the logs, the --level option is provided. You must specify the value 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'. The default value is INFO


For example, run the log output utility INFO
``` sh
    loader --output=/var/tmp https://hexlet.io/courses --l=INFO
```
Result
``` sh
2020-03-03 21:35:38,897 - root - INFO - Get file name hexlet-io-courses from https://hexlet.io/courses
2020-03-03 21:35:39,003 - root - INFO - Get download link https://hexlet.io/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js
2020-03-03 21:35:39,249 - root - INFO - Get file name cdn-cgi-scripts-5c5dd728-cloudflare-static-email-decode-min from /cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js
2020-03-03 21:35:39,249 - root - INFO - Create /var/tmp/hexlet-io-courses_files folder
2020-03-03 21:35:39,250 - root - INFO - Write data to /var/tmp/hexlet-io-courses_files/cdn-cgi-scripts-5c5dd728-cloudflare-static-email-decode-min.js file
2020-03-03 21:35:39,250 - root - INFO - Change link to /var/tmp/hexlet-io-courses_files/cdn-cgi-scripts-5c5dd728-cloudflare-static-email-decode-min.js
2020-03-03 21:35:39,294 - root - INFO - Write data to /var/tmp/hexlet-io-courses.html file
2020-03-03 21:35:39,294 - root - INFO - Finish write data to hexlet-io-courses file in /var/tmp folder

```
If the logging level is above DEBUG and INFO, the progress of the download will be displayed. For more information see https://docs.python.org/3/library/logging.html#logging-levels

The utility has return codes

- execution was successful **0**
- incorrect logging level **1**
- execution was interrupted by the user **2**
- execution was aborted due to a file error **3**
- execution was aborted due to a network error **4**

[![asciicast](https://asciinema.org/a/XYE7IARob3mkXYvxawLk7u1QA.svg)](https://asciinema.org/a/XYE7IARob3mkXYvxawLk7u1QA)

