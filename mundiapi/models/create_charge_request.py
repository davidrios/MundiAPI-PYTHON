# -*- coding: utf-8 -*-

"""
    mundiapi.models.create_charge_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapi.api_helper import APIHelper
import mundiapi.models.create_customer_request
import mundiapi.models.create_payment_request

class CreateChargeRequest(object):

    """Implementation of the 'CreateChargeRequest' model.

    Request for creating a new charge

    Attributes:
        code (string): Code
        amount (int): The amount of the charge, in cents
        customer_id (string): The customer's id
        customer (CreateCustomerRequest): Customer data
        payment (CreatePaymentRequest): Payment data
        metadata (dict<object, string>): Metadata
        due_at (datetime): The charge due date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'code',
        "amount":'amount',
        "customer_id":'customer_id',
        "customer":'customer',
        "payment":'payment',
        "metadata":'metadata',
        "due_at":'due_at'
    }

    def __init__(self,
                 code=None,
                 amount=None,
                 customer_id=None,
                 customer=None,
                 payment=None,
                 metadata=None,
                 due_at=None):
        """Constructor for the CreateChargeRequest class"""

        # Initialize members of the class
        self.code = code
        self.amount = amount
        self.customer_id = customer_id
        self.customer = customer
        self.payment = payment
        self.metadata = metadata
        self.due_at = APIHelper.RFC3339DateTime(due_at) if due_at else None


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
        code = dictionary.get('code')
        amount = dictionary.get('amount')
        customer_id = dictionary.get('customer_id')
        customer = mundiapi.models.create_customer_request.CreateCustomerRequest.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        payment = mundiapi.models.create_payment_request.CreatePaymentRequest.from_dictionary(dictionary.get('payment')) if dictionary.get('payment') else None
        metadata = dictionary.get('metadata')
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None

        # Return an object of this model
        return cls(code,
                   amount,
                   customer_id,
                   customer,
                   payment,
                   metadata,
                   due_at)


