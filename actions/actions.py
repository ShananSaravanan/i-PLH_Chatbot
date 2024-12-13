# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
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
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet

# class ActionSubmitForm(Action):
#     def name(self) -> str:
#         return "action_submit_form"

#     def run(self, dispatcher, tracker, domain):
#         user_name = tracker.get_slot("name")
#         # Debugging line to check slot value
#         print(f"User's name is: {user_name}")
#         dispatcher.utter_message(text=f"Thanks, {user_name}!")
#         return [SlotSet("name", user_name)]


# from rasa_sdk import Action
# from rasa_sdk.events import ReminderScheduled, AllSlotsReset
# import datetime

# class ActionCheckInactivity(Action):
#     def name(self) -> str:
#         return "action_check_inactivity"

#     def run(self, dispatcher, tracker, domain):
#         # Schedule a reminder for inactivity after 30 seconds
#         reminder_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
#         reminder = ReminderScheduled(
#             intent_name="trigger_inactivity",
#             trigger_date_time=reminder_time,
#             name="inactivity_reminder",
#             kill_on_user_message=True  # Automatically cancel the reminder if the user responds
#         )
#         return [reminder]

# from rasa_sdk import Action
# from rasa_sdk.events import AllSlotsReset

# class ActionEndConversationOnInactivity(Action):
#     def name(self) -> str:
#         return "action_end_conversation_on_inactivity"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(text="It seems you're busy. I'll end the conversation now. Goodbye!")
#         return [AllSlotsReset()]





