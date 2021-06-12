# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,EventType
from news import NewsFromBBC
from stock_news import stocknews
from stocks import get_data,clean,stock_analysis
from yahoo_fin import stock_info
from vslots import dose_avai_pincode,main_task
import requests
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionCoronaTracker(Action):

    def name(self) -> Text:
        return "action_corona_tracker"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            location = tracker.get_slot("location")
            response = requests.get("https://api.covid19india.org/data.json").json()
            print(location.title())
            for data in response["statewise"]:
                if location.title() == "India":
                    location = "Total"
                if data["state"] == location.title():
                    print(data)
                    message = "Corona Statistics in "+ location + ":" + "\n" + "Active : " + data["active"] +"\n" + "Confirmed : " + data[
                        "confirmed"] + "\n" + "Deaths : " + data["deaths"] + "\n" + "Recovered : " + data["recovered"]

            dispatcher.utter_message(text=message)

        except:
            dispatcher.utter_message("Sorry: Could not get information due to an internal error")

        return []


class ActionWeatherTracker(Action):

     def name(self) -> Text:
        return "action_weather_tracker"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         try:
            loc = tracker.get_slot('location')
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            API_KEY = "62c3c2895438fea212868bf530d34330"
            URL = BASE_URL + "q=" + loc + "&appid=" + API_KEY
            response = requests.get(URL)

            if response.status_code == 200:
                data = response.json()
                main = data['main']
                city = loc
                temperature = main['temp']
                temp_cel = main["temp"] - 273.15
                humidity = main['humidity']
                pressure = main['pressure']
                z = data["weather"]
                description = z[0]["description"]

                message = "Weather in " + city + ":" + "\n" "Temperature = " + str(temp_cel) + " degree celsius" + "\n" "Atmospheric pressure (in hPa unit) = " +str(pressure) + "\n""Humidity (in percentage) = " +str(humidity) + "\n" "Description : " + str(description)

            dispatcher.utter_message(text=message)

         except:
             m = "Sorry your request could not be processed."
             dispatcher.utter_message(text=m)

         return [SlotSet('location',loc)]


class ActionNewsTracker(Action):
    def name(self) -> Text:
        return "action_news_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            message = NewsFromBBC()
            #print(message)
            dispatcher.utter_message(text=message)

        except:
            m = "Sorry your request could not be processed."
            dispatcher.utter_message(text=m)

        return []


class ActionStocksTracker(Action):

    def name(self) -> Text:
        return "action_stocks_tracker"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            ticker = tracker.get_slot('stock')
            message = stock_analysis(ticker)
            dispatcher.utter_message(text=message)

        except:
            m = "Sorry your request could not be completed"
            dispatcher.utter_message(text=m)

        return [SlotSet('stock',ticker)]


class ActionStockNewsTracker(Action):
    def name(self) -> Text:
        return "action_stock_news_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            message = stocknews()
            #print(message)
            dispatcher.utter_message(text=message)

        except:
            m = "Sorry your request could not be processed."
            dispatcher.utter_message(text=m)

        return []

class ActionCurrentPrice(Action):
    def name(self) -> Text:
        return "action_current_price"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            tckr = tracker.get_slot('ticker')
            price = stock_info.get_live_price(tckr)
            if(tckr[-2:]=='NS' or tckr[-2]=='BO'):
                message = "Current price of " + tckr + " is " + str(price) + " INR."
                dispatcher.utter_message(text=message)
            else:
                message = "Current price of " + tckr+ " is " + str(price) + " USD."
                dispatcher.utter_message(text=message)

        except:
            m = "Sorry data could not be fetched. Please ensure that you have typed the ticker correctly."
            dispatcher.utter_message(text=m)

        return []

class ValidatepincodeForm(FormValidationAction):
    def name(self) -> Text:
        return "slot_pincode_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
                                                                        ) -> List[EventType]:

        required_slots = ["pincode", "date"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
#SlotSet("requested_slot", None)
        return []

class ActionPincodeSubmit(Action):

    def name(self) -> Text:
        return "action_pincode_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global message
        try:
            message=dose_avai_pincode(tracker.get_slot('pincode'),tracker.get_slot('date'))
            dispatcher.utter_message(text=message)

        except:
            message = "Sorry your request could not be proceed due to an internal error."
            dispatcher.utter_message(text=message)

        return []