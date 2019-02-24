import hashlib
from ast import literal_eval


#this function encrypt the text using a substitution chiper
def enc_text(p_text):
	mapping = { 'A': 'R','B': 'W','C' : 'H','D': 'Z', 'E': 'B','F': 'Q','G': 'M','H' : 'U','I' : 'S','J': 'Y','K': 'T','L': 'X','M' : 'I','N' : 'A','O': 'J','P' : 'V','Q': 'D','R': 'G','S' : 'F','T' : 'P','U' : 'C','V': 'N','W' : 'E','X' : 'L','Y'  :'O','Z' : 'K','a': 'r','b': 'w','c' : 'h','d': 'z', 'e': 'b','f': 'q','g': 'm','h' : 'u','i' : 's','j': 'y','k': 't','l': 'x','m' : 'i','n' : 'a','o': 'j','p' : 'v','q': 'd','r': 'g','s' : 'f','t' : 'p','u' : 'c','v': 'n','w' : 'e','x' : 'l','y'  :'o','z' : 'k'}
	chiper = ""
	for i in p_text:
		if i in mapping:
			i = mapping[i]
		chiper+= i
	return chiper

#decrypt the given chiper text
def dict_chip(chiper):
	mapping = {  'R':"A",'W':'B','H':'C' , 'Z':'D', 'B':'E', 'Q':'F','M':'G', 'U':'H', 'S':'I' ,'Y':'J', 'T':'K','X':'L','I':'M' ,'A':'N' ,'J':'O', 'V':'P' ,'D':'Q', 'G':'R', 'F':'S' , 'P':'T', 'C':'U' , 'N':'V', 'E':'W' , 'L':'X' ,'O':'Y'  , 'K':'Z' , 'r':'a', 'w':'b', 'h':'c' , 'z':'d',  'b':'e', 'q':'f', 'm':'g', 'u':'h' , 's':'i' , 'y':'j', 't':'k', 'x':'l', 'i':'m' , 'a':'n' , 'j':'o', 'v':'p' , 'd':'q', 'g':'r', 'f':'s' , 'p':'t' , 'c':'u' , 'n':'v', 'e':'w' , 'l':'x' ,'o':'y'  , 'k':'z' }
	p_text = ""
	for i in chiper:
		if i in mapping:
			i = mapping[i]
		p_text+= i
	return p_text


#Write to the config file
def writeConfig(name , password , usertype , privilagelev):
	z = hashlib.md5(password.encode())
	y = z.digest()
	det_dic = {"name" : name , "password" : y , "usertype": usertype,"privilagelev":privilagelev}
	fo = open("config.txt","a")
	fo.write(str(det_dic)+"\n")
	fo.close()
	return True


#read from config file
def readConfig( name ):
	fo = open("config.txt","r")
	while True:
		l = fo.readline()
		if(len(l)==0):
			break
		dic = literal_eval(l)
		if dic["name"]==name:
			fo.close()
			return (dic["name"] , dic["usertype"] )


#write to the data file
def writeData(name , DoB , blodgroup , drugprescriptions , labtestprescriptions ):
	data_dic = {}
	data_dic['name'] = enc_text(name)
	data_dic['DoB'] = enc_text(DoB)
	data_dic["blodgroup"] = enc_text(blodgroup)
	data_dic["drugprescriptions"] = enc_text(drugprescriptions)
	data_dic["labtestprescriptions"] = enc_text(labtestprescriptions)
	fo = open("data.txt","a")
	fo.write(str(data_dic)+"\n")
	fo.close()
	return True


#read from data file
def readData(name):
	fo = open("data.txt","r")
	while True:
		l = fo.readline()
		if(len(l)==0):
			break
		dic = literal_eval(l)
		if dict_chip(dic["name"])==name:
			fo.close()
			return (dict_chip(dic["name"]) , dict_chip(dic["DoB"]) , dict_chip(dic["blodgroup"]) , dict_chip(dic["drugprescriptions"]), dict_chip(dic["labtestprescriptions"]))

# login to the account and write to the config file if account has privilage
def prevbasewrite(myname , password , w_name , w_password , usertype , privilagelev):
	pass_w = hashlib.md5(password.encode())
	w = pass_w.digest()
	fo = open("config.txt","r")
	while True:
		l = fo.readline()
		if(len(l)==0):
			break
		dic = literal_eval(l)
		if dic["name"]==myname and dic["password"]==w :
			if  int(dic["privilagelev"])>=2:
				fo.close()
				writeConfig(w_name , w_password , usertype , privilagelev)
				return "Success" 
			else:
				return "Don't have privilage to write"

	return "Check the username or password"

#login to the account and read the config file if account has privilage
def prevbaseread(myname , password , r_name):
	pass_w = hashlib.md5(password.encode())
	w = pass_w.digest()
	fo = open("config.txt","r")
	while True:
		l = fo.readline()
		if(len(l)==0):
			break
		dic = literal_eval(l)
		if dic["name"]==myname and dic["password"]==w :
			if  int(dic["privilagelev"])>=1:
				fo.close()
				return readConfig(r_name) 
			else:
				return "Don't have privilage to write"

	return "Check the username or password"


#login to the account and write the data file if account has privilage
def prevbaseDatawrite(myname , password ,name , DoB , blodgroup , drugprescriptions , labtestprescriptions):
	pass_w = hashlib.md5(password.encode())
	w = pass_w.digest()
	fo = open("config.txt","r")
	while True:
		l = fo.readline()
		if(len(l)==0):
			break
		dic = literal_eval(l)
		if dic["name"]==myname and dic["password"]==w :
			if  int(dic["privilagelev"])>=3:
				fo.close()
				return writeData(name , DoB , blodgroup , drugprescriptions , labtestprescriptions) 
			else:
				return "Don't have privilage to write"

	return "Check the username or password"


#login to the account and read the data file if account has privilage
def prevbaseDataRead(myname , password ,name):
	pass_w = hashlib.md5(password.encode())
	w = pass_w.digest()
	fo = open("config.txt","r")
	while True:
		l = fo.readline()
		if(len(l)==0):
			break
		dic = literal_eval(l)
		if dic["name"]==myname and dic["password"]==w :
			if  int(dic["privilagelev"])>=2:
				fo.close()
				return readData(name) 
			else:
				return "Don't have privilage to write"

	return "Check the username or password"


#let's we create high privilage account by directly calling the writeConfig
writeConfig("Sulhi","Sulhi123","staff",4)

#level 4 write
print (prevbasewrite("Sulhi" , "Sulhi123" , "Sahan" , "Sahan123" , "staff" , 2))
#level 4 read
print (prevbaseread("Sulhi","Sulhi123","Sahan"))
#level 2 write
print (prevbasewrite("Sahan" , "Sahan123" , "Muaz" , "Muaz123" , "staff" , 1))
# level 1 read
print (prevbaseread("Muaz","Muaz123","Sahan"))
#level 4 write
print (prevbasewrite("Sulhi" , "Sulhi123" , "Nimsara" , "Nimsara123" , "patient" , 3))

print (prevbaseDatawrite("Sulhi","Sulhi123" , "Nimsara" , "1996-Nov-08" , "AB+" , "No Alergi" , "blodtest-possitive"))

# level 4 data read
print (prevbaseDataRead("Sulhi","Sulhi123" , "Nimsara"))

# level 3 data read
print (prevbaseDataRead("Nimsara","Nimsara123" , "Nimsara"))

# level 2 data read
print (prevbaseDataRead("Sahan","Sahan123" , "Nimsara"))

# level 1 data read
print (prevbaseDataRead("Muaz" , "Muaz123" , "Nimsara"))

# wrong password
print (prevbaseDataRead("Sulhi","Sulhi12" , "Nimsara"))
