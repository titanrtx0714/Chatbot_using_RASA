import requests

def dose_avai_pincode(pincode, date):
    api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(pincode,date)

    return main_task(api)

def main_task(api):
    response=requests.get(api)
    data=response.json()['sessions']
    output = ""
    try:
        for area in data:
            if area['available_capacity']>0:
                output += ("Hospital name: " + str(area['name']) + "\n" + "Address: " + str(area[
                    'address']) + "\n" + "Available_capacity_dose1: " + str(area['available_capacity_dose1']) + "\n" +
                        "Available_capacity_dose2: " + str(area['available_capacity_dose2']) + "\n" + "Available_capacity: " +
                        str(area['available_capacity']) + "\n" +
                        "min_age_limt: " + str(area['min_age_limit']) + "\n" + "Time_slots: " + str(area['slots'])[1:-1] +"\n")

    except:
        output+=("Currently there are no slots available.")

    return output


print(dose_avai_pincode('245101','14-06-2021'))