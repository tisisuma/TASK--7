def filecreation():

  from datetime import datetime

  current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
  str_current_datetime = str(current_datetime)

# Creating a File with current date and time added in the file name
  file =open('sample'+current_datetime+'.txt',"a")
  file.write("Hello"'\n')
#Adding the current date and time in the file
  file.write(current_datetime)
  print("Successfully Created")
  file.close()

filecreation()







