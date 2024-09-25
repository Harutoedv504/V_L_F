def video_length_finder(video_length):
    #take the video length and return it in seconds.
    # if the video length is in minutes, convert it to seconds.
    if 'm' in video_length:
     minutes, seconds = video_length.split('m')
     # Remove the 's' character from the seconds variable
     seconds = seconds.rstrip('s')
     return int(minutes) * 60 + int(seconds)
    #If the number of seconds is 60 or over, return -1    
    if int(video_length) % 60 != 0:
     return -1
    #You may get a number of minutes over 99 
    if int(video_length) > 99 * 60:
        return -1
     
    else:
        return int(video_length)

#testing the function

print(video_length_finder('1m30')) # should return 90
print(video_length_finder('2m15')) # should return 135
print(video_length_finder('99')) # should return -1
print(video_length_finder('89')) # should return -1
print(video_length_finder('120')) # should return 120
