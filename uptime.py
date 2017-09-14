#ProactiveNode
#Purpose: To get the uptime of a Windows machine using Python and its libraries.
#Tested on Windows 7
import subprocess
import datetime

#Cleans the output of the command and converts the output into a tuple. Tuple contains the Year, Month and Day in that order.
def cleanup_date_T(first_element):
    first_element_split = first_element.split()
    month = int(first_element_split[1][0:2])
    day = int(first_element_split[1][3:5])
    year = int(first_element_split[1][6:10])
    cleaned_current_date = (year,month,day)
    return(cleaned_current_date)

#Cleans the output of the command. Converts hours and minutes to become total minutes of that day. 
def cleanup_time_t(first_element):
    first_element_split = first_element.split()
    if (b'PM' or 'PM') in first_element_split[1]:
        if b'12' in first_element_split[0][0:2]:
            total_hours =  int(first_element_split[0][0:2])
        else:
            total_hours = int(first_element_split[0][0:2]) + 12
    elif (b'AM' or 'AM') in first_element_split[1]:
        if b'12' in first_element_split[0][0:2]:
            total_hours =  0
        else:
            total_hours =  int(first_element_split[0][0:2])
    else:
        total_hours =  int(first_element_split[0][0:2])
    total_minutes = int(first_element_split[0][3:5])
    return(total_hours,total_minutes)


#Cleansup the system boot time output and puts it in a tuple.
def cleanup_past_system_date_time(first_element):
    first_element_split = first_element.split()
    #Gets the date and splits it into three seperate elements
    date_split = list(first_element_split[3])
    length_list = len(date_split)
    counter = 0
    convert_date = list()
    while counter <= length_list-1:
        convert_date.append(chr(date_split[counter]))
        counter = counter + 1
    convert_date.pop() #Removes a comma that is leftover from converting 
    joined_date = ''.join(convert_date)
    past_date = joined_date.split('/')

    #Time. Converts the time from 12-hour AM/PM to 24-hour.
    splitting = first_element_split[4].split(b':')
    if (b'PM' or 'PM' ) in first_element_split[5]:
        if '12' == first_element_split[4][0:2]:
            total_hours_past=int(splitting[0])
        else:
            total_hours_past = int(splitting[0]) + 12
    else:
        total_hours_past=int(splitting[0])
    total_minutes_past = int(splitting[1])
    return(past_date, total_hours_past, total_minutes_past)

    
def main():
    current_date = subprocess.Popen(["cmd","/c","date","/T"], stdout=subprocess.PIPE)
    current_date_T = current_date.communicate()
    
    current_time = subprocess.Popen(["cmd","/c","time","/t"], stdout=subprocess.PIPE)
    current_time_t = current_time.communicate()
    
    past_time = subprocess.Popen(["cmd","/c","systeminfo","|", "find","System Boot Time:"], stdout=subprocess.PIPE)
    past_system_date_time = past_time.communicate()

    #Cleans the output from the commands. Makes it more usable and readable for me.
    date_tuple = cleanup_date_T(current_date_T[0])
    current_time_total_minutes= cleanup_time_t(current_time_t[0])
    past_date_time_tuple = cleanup_past_system_date_time(past_system_date_time[0])


    #Organizes the date and time in this format: Year-Month-Day Hour-Minute
    time_current = datetime.datetime(int(date_tuple[0]),int(date_tuple[1]),date_tuple[2], current_time_total_minutes[0],current_time_total_minutes[1])
    time_past = datetime.datetime(int(past_date_time_tuple[0][2]),int(past_date_time_tuple[0][0]),int(past_date_time_tuple[0][1]),past_date_time_tuple[1],past_date_time_tuple[2])

    #Subtracts the current time to the system boot time
    subtraction_time = str(time_current - time_past)
    time_split = subtraction_time.split(':')
    print("Your machine has been online for " + time_split[0] + " hours and " + time_split[1] + " minutes.")


main()
