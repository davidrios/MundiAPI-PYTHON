# -*- coding: utf-8 -*-

"""
    mundiapi.models.update_subscription_card_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapi.models.create_card_request

class UpdateSubscriptionCardRequest(object):

    """Implementation of the 'UpdateSubscriptionCardRequest' model.

    Request for updating the card from a subscription

    Attributes:
        card (CreateCardRequest): Credit card data
        card_id (string): Credit card id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card":'card',
        "card_id":'card_id'
    }

    def __init__(self,
                 card=None,
                 card_id=None):
        """Constructor for the UpdateSubscriptionCardRequest class"""

        # Initialize members of the class
        self.card = card
        self.card_id = card_id


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        card = mundiapi.models.create_card_request.CreateCardRequest.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        card_id = dictionary.get('card_id')

        # Return an object of this model
        return cls(card,
                   card_id)


