
set timestamp=%date:~10,4%-%date:~4,2%-%date:~7,2%-%time:~0,2%%time:~3,2%%time:~6,2%
REM Replace spaces with underscores
set timestamp=%timestamp: =_%


copy /y test_links.txt ".\s3_link-checker\%timestamp%.txt"
call aws s3 sync .\s3_link-checker\ s3://link-checker/ 

type test_links.txt

cd