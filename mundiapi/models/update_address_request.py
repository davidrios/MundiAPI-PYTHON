# -*- coding: utf-8 -*-

"""
    mundiapi.models.update_address_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class UpdateAddressRequest(object):

    """Implementation of the 'UpdateAddressRequest' model.

    Request for updating an address

    Attributes:
        number (string): Number
        complement (string): Complement
        metadata (dict<object, string>): Metadata
        line_2 (string): Line 2 for address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number" : "number",
        "complement" : "complement",
        "metadata" : "metadata",
        "line_2" : "line_2"
    }

    def __init__(self,
                 number=None,
                 complement=None,
                 metadata=None,
                 line_2=None):
        """Constructor for the UpdateAddressRequest class"""

        # Initialize members of the class
        self.number = number
        self.complement = complement
        self.metadata = metadata
        self.line_2 = line_2


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
        number = dictionary.get("number")
        complement = dictionary.get("complement")
        metadata = dictionary.get("metadata")
        line_2 = dictionary.get("line_2")

        # Return an object of this model
        return cls(number,
                   complement,
                   metadata,
                   line_2)


