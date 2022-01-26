#import packages
import os

#Vars
ses_list = []
ep_list = []
Season_num = '1'
ep_num = '1'
done = 0
ses = 'null'

while done == 0:
  path = input('Please enter the filepath to the show: ')
  name = input('Please enter the name of the show: ')

  #Change to folder
  try:
    os.chdir(path)
    ses = len(next(os.walk(path))[1])
    for folders in os.listdir(path):
      ses_list.append(os.path.join(path, folders))
  except:
    print('This path does not exist please enter 2 on the next question and try agian.')
  while True:
    #print(ses_list)
    res = input('We found ' + str(ses) + ' seasons for this show. Is this correct? (Y 1 /N 2): ')
    res = int(res)
    if res == 1:
      while ses_list:
        os.chdir(ses_list[0])
        print(os.getcwd())
        for files in os.listdir(ses_list[0]):
          ep_list.append(files)
        while ep_list:
          name_new = (name + ' - s0' + Season_num + 'e' + ep_num)
          target = ep_list.pop(0)
          os.rename(target, name_new)
          ep_num = str((int(ep_num)) + 1)
        Season_num = str((int(Season_num )) + 1)
        ep_num = '1'
        ses_list.pop(0)
      done = 1
      break

    if res == 2:
      print('Please check your filepath and try agian.')
      break

    else:
      print('We did not understand that input please insert 1 for yes, and 2 for no.')
      continue
input('Thanks for using the tool! Have a great day.')
