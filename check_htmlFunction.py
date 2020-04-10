def check_html():
	html_text = str(input("enter your html text"))
	errors = []
	open_tag = "<"
	close_tag = ">"
	slash = "/"
        #slash = count_open  / 2 or count_close / 2 else there error
	tag = "<" + ">"
	count_open = html_text.count(open_tag)
	count_close = html_text.count(close_tag)
	count_slash = html_text.count(slash)
	count_tag = html_text.count(tag)
	check = 0
	problem = None
	missing_numbero = None
	missing_numberc = None
	missing_number_slash = None
	ishtml = False
	if count_open > count_close:
		missing_numberc = count_open - count_close
		problem = "close"
		errors.append("!missing : " + str(missing_numberc) + " [ > ] closing tags")
		check -= 1
	else:
		check += 1
	if count_close > count_open:
		missing_numbero = count_close - count_open
		problem = "open"
		errors.append("!missing : " + str(missing_numbero) + " [ < ] open tags")
		check -= 1
	else:
		check += 1
	if (count_slash != count_open // 2) and (count_slash != count_close // 2):
		problem = "slash"
		missing_number_slash = (count_close + count_open) // 4
		if missing_number_slash == 0:
			check += 1			
		else:
			errors.append("!missing : " + str(missing_number_slash) + " [ / ] Slash before clossing tag")
			check -= 1	
	else:
		check += 1
	if count_open == 0 and 	count_close == 0 and count_slash == 0:		
		print("Please enter html codes")
		check_html()
	else:
		ishtml = True	
		
	if check == 3 and ishtml == True:		
		message = "You Have Write clean code Passed all test.. 4 tests"
		error = []
		return(message)	
	for error in errors:
		print(error)
