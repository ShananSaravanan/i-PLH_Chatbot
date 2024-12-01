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





