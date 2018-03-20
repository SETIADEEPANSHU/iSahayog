from gluon import *
import validate_email as ve
def check_mail(x):
	is_valid=ve.validate_email(x,verify=True)
	return is_valid
