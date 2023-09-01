import re
def check(s):
	pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
	if re.match(pat,s):
		print("Valid Email")
	else:
		print("Invalid Email")

email = "ankitrai326@gmail.com"
check(email)