def filereading():
  from datetime import datetime

  current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
  str_current_datetime = str(current_datetime)

# Creating a File with current date and time added in the file name
  file =open('sample'+current_datetime+'.txt',"a")
  file.write("Hello"'\n')
#Adding the current date and time in the file
  file.write(current_datetime)
  file.close()
#printing the content of the file
  file =open('sample'+current_datetime+'.txt',"r")
  print(file.read())
  file.close()
filereading()