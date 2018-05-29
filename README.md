# aws-lnkchk-start
Detects S3 bucket updates to add a page to the queue


S3 -> 
	Lambda:aws-lnkchk-start 
		-> SQS:link-check-pages 
			-> Lambda:aws-lnkchk-links 
				-> SQS:link-check-links 
					-> Lamba:aws-lnkchk-verify-links
						-> SNS:bad-links



