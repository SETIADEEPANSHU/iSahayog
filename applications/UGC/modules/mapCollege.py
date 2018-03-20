import send

def mapColleges(c_email_list,problem_id):
	for mail in c_email_list:
		send.send(mail,problem_id)

mapColleges(['r1s3k2@gmail.com'],'00000003')