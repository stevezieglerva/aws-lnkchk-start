set function_name=awk-lnkchk-start


call C:\Users\18589\Envs\pylambda\Scripts\activate
call del /q lambda_function.zip
call "c:\Program Files\7-Zip\7z.exe" a lambda_function.zip *.py


REM Upload the new code
call aws lambda update-function-code --function-name %function_name% --zip-file fileb://lambda_function.zip

REM Call the function
call aws lambda invoke --function-name %function_name% --payload file://test_payload.json test_result.txt
call type test_result.txt

