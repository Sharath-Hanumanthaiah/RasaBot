# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Optional, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

class ActionAskPatientName(Action):

    def name(self) -> Text:
        return "action_ask_Patient_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="can i know patient name")

        return []

class ActionAskPatientAge(Action):

    def name(self) -> Text:
        return "action_ask_patient_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="can i know patient Age")

        return []

class ActionAskpatientAddress(Action):

    def name(self) -> Text:
        return "action_ask_patient_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="share me the address")

        return []

class ActionHealthService(Action):

    def name(self) -> Text:
        return "action_health_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(buttons=[
            {
                "title":"patient registration",
                "payload":"patient registration"
            },
             {
                "title":"Help Line Numbers",
                "payload":"Help Line Numbers"
            }
        ])

        return []

class ActionMainService(Action):

    def name(self) -> Text:
        return "action_main_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(buttons=[
            {
                "title":"patient registration",
                "payload":"patient registration"
            },
             {
                "title":"Help Line Numbers",
                "payload":"Help Line Numbers"
            }
        ])

        return []

class ActionSendHelplineNumber(Action):

    def name(self) -> Text:
        return "action_send_helpline_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=" 2021241020452")

        return []

class ValidateRestaurantForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_Patient_details"

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
        return ["Patient_name", "patient_age", "patient_address"]
   
    def validate_Patient_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate user name."""
        if len(value.lower()) > 3:
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"Patient_name": value}
        else:
            dispatcher.utter_message(text="Please share proper name")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"Patient_name": None}
    
    def validate_patient_age(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate user name."""
        if value.isdigit:
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"patient_age": value}
        else:
            dispatcher.utter_message(text="Please share proper age")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"patient_age": None}

    def validate_patient_address(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate user name."""
        return {"patient_address": value}


