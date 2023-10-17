class Solution:
    def maximumTime(self, time: str) -> str:
        hours, minutes = time.split(":")
        
        latest_hour = ""
        latest_min = ""
        
        if hours == "??":
            latest_hour = "23"
        
        elif hours[0] == "?":
            if int(hours[1]) <= 3:
                latest_hour = "2" + hours[1]
            else:
                latest_hour = "1" + hours[1]
        
        elif hours[1] == "?":
            if int(hours[0]) < 2:
                latest_hour = hours[0] + "9"
            else:
                latest_hour = hours[0] + "3"
        else:
            latest_hour = hours
        
        if minutes == "??":
            latest_min = "59"
        
        elif minutes[0] == "?":
            latest_min = "5" + minutes[1]
        
        elif minutes[1] == "?":
            latest_min = minutes[0] + "9"
        
        else:
            latest_min = minutes
        
        return latest_hour + ":" + latest_min