# -*- coding: utf-8 -*-

"""
    mundiapi.models.get_transaction_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
from mundiapi.api_helper import APIHelper
import mundiapi.models.get_billing_address_response
import mundiapi.models.get_card_response

class GetTransactionResponse(object):

    """Implementation of the 'GetTransactionResponse' model.

    Generic response object for getting a transaction.

    Attributes:
        gateway_id (string): Gateway transaction id
        amount (int): Amount in cents
        status (string): Transaction status
        success (bool): Indicates if the transaction ocurred successfuly
        created_at (datetime): Creation date
        updated_at (datetime): Last update date
        attempt_count (int): Number of attempts tried
        max_attempts (int): Max attempts
        next_attempt (datetime): Date and time of the next attempt
        transaction_type (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "gateway_id" : "gateway_id",
        "amount" : "amount",
        "status" : "status",
        "success" : "success",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "attempt_count" : "attempt_count",
        "max_attempts" : "max_attempts",
        "next_attempt" : "next_attempt",
        "transaction_type" : "transaction_type"
    }

    def __init__(self,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 success=None,
                 created_at=None,
                 updated_at=None,
                 attempt_count=None,
                 max_attempts=None,
                 next_attempt=None,
                 transaction_type=None):
        """Constructor for the GetTransactionResponse class"""

        # Initialize members of the class
        self.gateway_id = gateway_id
        self.amount = amount
        self.status = status
        self.success = success
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.attempt_count = attempt_count
        self.max_attempts = max_attempts
        self.next_attempt = APIHelper.RFC3339DateTime(next_attempt) if next_attempt else None
        self.transaction_type = transaction_type


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

        discriminators = {
            'boleto': GetBoletoTransactionResponse.from_dictionary,
            'bank_transfer': GetBankTransferTransactionResponse.from_dictionary,
            'safetypay': GetSafetyPayTransactionResponse.from_dictionary,
            'credit_card': GetCreditCardTransactionResponse.from_dictionary,
            'voucher': GetVoucherTransactionResponse.from_dictionary
        }
        unboxer = discriminators.get(dictionary.get('transaction_type'))

        # Delegate unboxing to another function if a discriminator
        # value for a child class is present.
        if unboxer:
            return unboxer(dictionary)

        # Extract variables from the dictionary
        gateway_id = dictionary.get("gateway_id")
        amount = dictionary.get("amount")
        status = dictionary.get("status")
        success = dictionary.get("success")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        attempt_count = dictionary.get("attempt_count")
        max_attempts = dictionary.get("max_attempts")
        next_attempt = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_attempt")).datetime if dictionary.get("next_attempt") else None
        transaction_type = dictionary.get("transaction_type")

        # Return an object of this model
        return cls(gateway_id,
                   amount,
                   status,
                   success,
                   created_at,
                   updated_at,
                   attempt_count,
                   max_attempts,
                   next_attempt,
                   transaction_type)


class GetBoletoTransactionResponse(GetTransactionResponse):

    """Implementation of the 'GetBoletoTransactionResponse' model.

    Response object for getting a boleto transaction
    NOTE: This class inherits from 'GetTransactionResponse'.

    Attributes:
        url (string): TODO: type description here.
        bar_code (string): TODO: type description here.
        nosso_numero (string): TODO: type description here.
        bank (string): TODO: type description here.
        document_number (string): TODO: type description here.
        instructions (string): TODO: type description here.
        billing_address (GetBillingAddressResponse): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url" : "url",
        "bar_code" : "bar_code",
        "nosso_numero" : "nosso_numero",
        "bank" : "bank",
        "document_number" : "document_number",
        "instructions" : "instructions",
        "billing_address" : "billing_address",
        "gateway_id" : "gateway_id",
        "amount" : "amount",
        "status" : "status",
        "success" : "success",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "attempt_count" : "attempt_count",
        "max_attempts" : "max_attempts",
        "next_attempt" : "next_attempt",
        "transaction_type" : "transaction_type"
    }

    def __init__(self,
                 url=None,
                 bar_code=None,
                 nosso_numero=None,
                 bank=None,
                 document_number=None,
                 instructions=None,
                 billing_address=None,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 success=None,
                 created_at=None,
                 updated_at=None,
                 attempt_count=None,
                 max_attempts=None,
                 next_attempt=None,
                 transaction_type=None):
        """Constructor for the GetBoletoTransactionResponse class"""

        # Initialize members of the class
        self.url = url
        self.bar_code = bar_code
        self.nosso_numero = nosso_numero
        self.bank = bank
        self.document_number = document_number
        self.instructions = instructions
        self.billing_address = billing_address

        # Call the constructor for the base class
        super(GetBoletoTransactionResponse, self).__init__(gateway_id,
                                                           amount,
                                                           status,
                                                           success,
                                                           created_at,
                                                           updated_at,
                                                           attempt_count,
                                                           max_attempts,
                                                           next_attempt,
                                                           transaction_type)


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
        url = dictionary.get("url")
        bar_code = dictionary.get("bar_code")
        nosso_numero = dictionary.get("nosso_numero")
        bank = dictionary.get("bank")
        document_number = dictionary.get("document_number")
        instructions = dictionary.get("instructions")
        billing_address = mundiapi.models.get_billing_address_response.GetBillingAddressResponse.from_dictionary(dictionary.get("billing_address")) if dictionary.get("billing_address") else None
        gateway_id = dictionary.get("gateway_id")
        amount = dictionary.get("amount")
        status = dictionary.get("status")
        success = dictionary.get("success")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        attempt_count = dictionary.get("attempt_count")
        max_attempts = dictionary.get("max_attempts")
        next_attempt = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_attempt")).datetime if dictionary.get("next_attempt") else None
        transaction_type = dictionary.get("transaction_type")

        # Return an object of this model
        return cls(url,
                   bar_code,
                   nosso_numero,
                   bank,
                   document_number,
                   instructions,
                   billing_address,
                   gateway_id,
                   amount,
                   status,
                   success,
                   created_at,
                   updated_at,
                   attempt_count,
                   max_attempts,
                   next_attempt,
                   transaction_type)


class GetBankTransferTransactionResponse(GetTransactionResponse):

    """Implementation of the 'GetBankTransferTransactionResponse' model.

    Response object for getting a bank transfer transaction
    NOTE: This class inherits from 'GetTransactionResponse'.

    Attributes:
        url (string): Payment url
        bank_tid (string): Transaction identifier for the bank
        bank (string): Bank
        paid_at (datetime): Payment date
        paid_amount (int): Paid amount

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url" : "url",
        "bank_tid" : "bank_tid",
        "bank" : "bank",
        "gateway_id" : "gateway_id",
        "amount" : "amount",
        "status" : "status",
        "success" : "success",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "attempt_count" : "attempt_count",
        "max_attempts" : "max_attempts",
        "paid_at" : "paid_at",
        "paid_amount" : "paid_amount",
        "next_attempt" : "next_attempt",
        "transaction_type" : "transaction_type"
    }

    def __init__(self,
                 url=None,
                 bank_tid=None,
                 bank=None,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 success=None,
                 created_at=None,
                 updated_at=None,
                 attempt_count=None,
                 max_attempts=None,
                 paid_at=None,
                 paid_amount=None,
                 next_attempt=None,
                 transaction_type=None):
        """Constructor for the GetBankTransferTransactionResponse class"""

        # Initialize members of the class
        self.url = url
        self.bank_tid = bank_tid
        self.bank = bank
        self.paid_at = APIHelper.RFC3339DateTime(paid_at) if paid_at else None
        self.paid_amount = paid_amount

        # Call the constructor for the base class
        super(GetBankTransferTransactionResponse, self).__init__(gateway_id,
                                                                 amount,
                                                                 status,
                                                                 success,
                                                                 created_at,
                                                                 updated_at,
                                                                 attempt_count,
                                                                 max_attempts,
                                                                 next_attempt,
                                                                 transaction_type)


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
        url = dictionary.get("url")
        bank_tid = dictionary.get("bank_tid")
        bank = dictionary.get("bank")
        gateway_id = dictionary.get("gateway_id")
        amount = dictionary.get("amount")
        status = dictionary.get("status")
        success = dictionary.get("success")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        attempt_count = dictionary.get("attempt_count")
        max_attempts = dictionary.get("max_attempts")
        paid_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("paid_at")).datetime if dictionary.get("paid_at") else None
        paid_amount = dictionary.get("paid_amount")
        next_attempt = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_attempt")).datetime if dictionary.get("next_attempt") else None
        transaction_type = dictionary.get("transaction_type")

        # Return an object of this model
        return cls(url,
                   bank_tid,
                   bank,
                   gateway_id,
                   amount,
                   status,
                   success,
                   created_at,
                   updated_at,
                   attempt_count,
                   max_attempts,
                   paid_at,
                   paid_amount,
                   next_attempt,
                   transaction_type)


class GetSafetyPayTransactionResponse(GetTransactionResponse):

    """Implementation of the 'GetSafetyPayTransactionResponse' model.

    Response object for getting a safety pay transaction
    NOTE: This class inherits from 'GetTransactionResponse'.

    Attributes:
        url (string): Payment url
        bank_tid (string): Transaction identifier on bank
        paid_at (datetime): Payment date
        paid_amount (int): Paid amount

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url" : "url",
        "bank_tid" : "bank_tid",
        "gateway_id" : "gateway_id",
        "amount" : "amount",
        "status" : "status",
        "success" : "success",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "attempt_count" : "attempt_count",
        "max_attempts" : "max_attempts",
        "paid_at" : "paid_at",
        "paid_amount" : "paid_amount",
        "next_attempt" : "next_attempt",
        "transaction_type" : "transaction_type"
    }

    def __init__(self,
                 url=None,
                 bank_tid=None,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 success=None,
                 created_at=None,
                 updated_at=None,
                 attempt_count=None,
                 max_attempts=None,
                 paid_at=None,
                 paid_amount=None,
                 next_attempt=None,
                 transaction_type=None):
        """Constructor for the GetSafetyPayTransactionResponse class"""

        # Initialize members of the class
        self.url = url
        self.bank_tid = bank_tid
        self.paid_at = APIHelper.RFC3339DateTime(paid_at) if paid_at else None
        self.paid_amount = paid_amount

        # Call the constructor for the base class
        super(GetSafetyPayTransactionResponse, self).__init__(gateway_id,
                                                              amount,
                                                              status,
                                                              success,
                                                              created_at,
                                                              updated_at,
                                                              attempt_count,
                                                              max_attempts,
                                                              next_attempt,
                                                              transaction_type)


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
        url = dictionary.get("url")
        bank_tid = dictionary.get("bank_tid")
        gateway_id = dictionary.get("gateway_id")
        amount = dictionary.get("amount")
        status = dictionary.get("status")
        success = dictionary.get("success")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        attempt_count = dictionary.get("attempt_count")
        max_attempts = dictionary.get("max_attempts")
        paid_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("paid_at")).datetime if dictionary.get("paid_at") else None
        paid_amount = dictionary.get("paid_amount")
        next_attempt = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_attempt")).datetime if dictionary.get("next_attempt") else None
        transaction_type = dictionary.get("transaction_type")

        # Return an object of this model
        return cls(url,
                   bank_tid,
                   gateway_id,
                   amount,
                   status,
                   success,
                   created_at,
                   updated_at,
                   attempt_count,
                   max_attempts,
                   paid_at,
                   paid_amount,
                   next_attempt,
                   transaction_type)


class GetCreditCardTransactionResponse(GetTransactionResponse):

    """Implementation of the 'GetCreditCardTransactionResponse' model.

    Response object for getting a credit card transaction
    NOTE: This class inherits from 'GetTransactionResponse'.

    Attributes:
        statement_descriptor (string): Text that will appear on the credit
            card's statement
        acquirer_name (string): Acquirer name
        acquirer_affiliation_code (string): Aquirer affiliation code
        acquirer_tid (string): Acquirer TID
        acquirer_nsu (string): Acquirer NSU
        acquirer_auth_code (string): Acquirer authorization code
        operation_type (string): Operation type
        card (GetCardResponse): Card data
        acquirer_message (string): Acquirer message
        installments (int): Number of installments

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor" : "statement_descriptor",
        "acquirer_name" : "acquirer_name",
        "acquirer_affiliation_code" : "acquirer_affiliation_code",
        "acquirer_tid" : "acquirer_tid",
        "acquirer_nsu" : "acquirer_nsu",
        "acquirer_auth_code" : "acquirer_auth_code",
        "operation_type" : "operation_type",
        "card" : "card",
        "acquirer_message" : "acquirer_message",
        "gateway_id" : "gateway_id",
        "amount" : "amount",
        "status" : "status",
        "success" : "success",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "attempt_count" : "attempt_count",
        "max_attempts" : "max_attempts",
        "installments" : "installments",
        "next_attempt" : "next_attempt",
        "transaction_type" : "transaction_type"
    }

    def __init__(self,
                 statement_descriptor=None,
                 acquirer_name=None,
                 acquirer_affiliation_code=None,
                 acquirer_tid=None,
                 acquirer_nsu=None,
                 acquirer_auth_code=None,
                 operation_type=None,
                 card=None,
                 acquirer_message=None,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 success=None,
                 created_at=None,
                 updated_at=None,
                 attempt_count=None,
                 max_attempts=None,
                 installments=None,
                 next_attempt=None,
                 transaction_type=None):
        """Constructor for the GetCreditCardTransactionResponse class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.acquirer_name = acquirer_name
        self.acquirer_affiliation_code = acquirer_affiliation_code
        self.acquirer_tid = acquirer_tid
        self.acquirer_nsu = acquirer_nsu
        self.acquirer_auth_code = acquirer_auth_code
        self.operation_type = operation_type
        self.card = card
        self.acquirer_message = acquirer_message
        self.installments = installments

        # Call the constructor for the base class
        super(GetCreditCardTransactionResponse, self).__init__(gateway_id,
                                                               amount,
                                                               status,
                                                               success,
                                                               created_at,
                                                               updated_at,
                                                               attempt_count,
                                                               max_attempts,
                                                               next_attempt,
                                                               transaction_type)


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
        statement_descriptor = dictionary.get("statement_descriptor")
        acquirer_name = dictionary.get("acquirer_name")
        acquirer_affiliation_code = dictionary.get("acquirer_affiliation_code")
        acquirer_tid = dictionary.get("acquirer_tid")
        acquirer_nsu = dictionary.get("acquirer_nsu")
        acquirer_auth_code = dictionary.get("acquirer_auth_code")
        operation_type = dictionary.get("operation_type")
        card = mundiapi.models.get_card_response.GetCardResponse.from_dictionary(dictionary.get("card")) if dictionary.get("card") else None
        acquirer_message = dictionary.get("acquirer_message")
        gateway_id = dictionary.get("gateway_id")
        amount = dictionary.get("amount")
        status = dictionary.get("status")
        success = dictionary.get("success")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        attempt_count = dictionary.get("attempt_count")
        max_attempts = dictionary.get("max_attempts")
        installments = dictionary.get("installments")
        next_attempt = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_attempt")).datetime if dictionary.get("next_attempt") else None
        transaction_type = dictionary.get("transaction_type")

        # Return an object of this model
        return cls(statement_descriptor,
                   acquirer_name,
                   acquirer_affiliation_code,
                   acquirer_tid,
                   acquirer_nsu,
                   acquirer_auth_code,
                   operation_type,
                   card,
                   acquirer_message,
                   gateway_id,
                   amount,
                   status,
                   success,
                   created_at,
                   updated_at,
                   attempt_count,
                   max_attempts,
                   installments,
                   next_attempt,
                   transaction_type)


class GetVoucherTransactionResponse(GetTransactionResponse):

    """Implementation of the 'GetVoucherTransactionResponse' model.

    Response for voucher transactions
    NOTE: This class inherits from 'GetTransactionResponse'.

    Attributes:
        statement_descriptor (string): Text that will appear on the voucher's
            statement
        acquirer_name (string): Acquirer name
        acquirer_affiliation_code (string): Acquirer affiliation code
        acquirer_tid (string): Acquirer TID
        acquirer_nsu (string): Acquirer NSU
        acquirer_auth_code (string): Acquirer authorization code
        acquirer_message (string): acquirer_message
        acquirer_return_code (string): Acquirer return code
        operation_type (string): Operation type
        card (GetCardResponse): Card data

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "statement_descriptor" : "statement_descriptor",
        "acquirer_name" : "acquirer_name",
        "acquirer_affiliation_code" : "acquirer_affiliation_code",
        "acquirer_tid" : "acquirer_tid",
        "acquirer_nsu" : "acquirer_nsu",
        "acquirer_auth_code" : "acquirer_auth_code",
        "acquirer_message" : "acquirer_message",
        "acquirer_return_code" : "acquirer_return_code",
        "operation_type" : "operation_type",
        "card" : "card",
        "gateway_id" : "gateway_id",
        "amount" : "amount",
        "status" : "status",
        "success" : "success",
        "created_at" : "created_at",
        "updated_at" : "updated_at",
        "attempt_count" : "attempt_count",
        "max_attempts" : "max_attempts",
        "next_attempt" : "next_attempt",
        "transaction_type" : "transaction_type"
    }

    def __init__(self,
                 statement_descriptor=None,
                 acquirer_name=None,
                 acquirer_affiliation_code=None,
                 acquirer_tid=None,
                 acquirer_nsu=None,
                 acquirer_auth_code=None,
                 acquirer_message=None,
                 acquirer_return_code=None,
                 operation_type=None,
                 card=None,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 success=None,
                 created_at=None,
                 updated_at=None,
                 attempt_count=None,
                 max_attempts=None,
                 next_attempt=None,
                 transaction_type=None):
        """Constructor for the GetVoucherTransactionResponse class"""

        # Initialize members of the class
        self.statement_descriptor = statement_descriptor
        self.acquirer_name = acquirer_name
        self.acquirer_affiliation_code = acquirer_affiliation_code
        self.acquirer_tid = acquirer_tid
        self.acquirer_nsu = acquirer_nsu
        self.acquirer_auth_code = acquirer_auth_code
        self.acquirer_message = acquirer_message
        self.acquirer_return_code = acquirer_return_code
        self.operation_type = operation_type
        self.card = card

        # Call the constructor for the base class
        super(GetVoucherTransactionResponse, self).__init__(gateway_id,
                                                            amount,
                                                            status,
                                                            success,
                                                            created_at,
                                                            updated_at,
                                                            attempt_count,
                                                            max_attempts,
                                                            next_attempt,
                                                            transaction_type)


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
        statement_descriptor = dictionary.get("statement_descriptor")
        acquirer_name = dictionary.get("acquirer_name")
        acquirer_affiliation_code = dictionary.get("acquirer_affiliation_code")
        acquirer_tid = dictionary.get("acquirer_tid")
        acquirer_nsu = dictionary.get("acquirer_nsu")
        acquirer_auth_code = dictionary.get("acquirer_auth_code")
        acquirer_message = dictionary.get("acquirer_message")
        acquirer_return_code = dictionary.get("acquirer_return_code")
        operation_type = dictionary.get("operation_type")
        card = mundiapi.models.get_card_response.GetCardResponse.from_dictionary(dictionary.get("card")) if dictionary.get("card") else None
        gateway_id = dictionary.get("gateway_id")
        amount = dictionary.get("amount")
        status = dictionary.get("status")
        success = dictionary.get("success")
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        attempt_count = dictionary.get("attempt_count")
        max_attempts = dictionary.get("max_attempts")
        next_attempt = APIHelper.RFC3339DateTime.from_value(dictionary.get("next_attempt")).datetime if dictionary.get("next_attempt") else None
        transaction_type = dictionary.get("transaction_type")

        # Return an object of this model
        return cls(statement_descriptor,
                   acquirer_name,
                   acquirer_affiliation_code,
                   acquirer_tid,
                   acquirer_nsu,
                   acquirer_auth_code,
                   acquirer_message,
                   acquirer_return_code,
                   operation_type,
                   card,
                   gateway_id,
                   amount,
                   status,
                   success,
                   created_at,
                   updated_at,
                   attempt_count,
                   max_attempts,
                   next_attempt,
                   transaction_type)


