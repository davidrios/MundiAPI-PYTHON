# -*- coding: utf-8 -*-

"""
    mundiapi.controllers.invoices_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.get_invoice_response import GetInvoiceResponse
from ..models.list_invoices_response import ListInvoicesResponse

class InvoicesController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def get_invoice(self,
                    invoice_id):
        """Does a GET request to /invoices/{invoice_id}.

        Gets an invoice

        Args:
            invoice_id (string): Invoice Id

        Returns:
            GetInvoiceResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/invoices/{invoice_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'invoice_id': invoice_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetInvoiceResponse.from_dictionary)

    def cancel_invoice(self,
                       invoice_id):
        """Does a DELETE request to /invoices/{invoice_id}.

        Cancels an invoice

        Args:
            invoice_id (string): Invoice id

        Returns:
            GetInvoiceResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/invoices/{invoice_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'invoice_id': invoice_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetInvoiceResponse.from_dictionary)

    def update_invoice_metadata(self,
                                invoice_id,
                                request):
        """Does a PATCH request to /invoices/{invoice_id}/metadata.

        Updates the metadata from an invoice

        Args:
            invoice_id (string): The invoice id
            request (UpdateMetadataRequest): Request for updating the invoice
                metadata

        Returns:
            GetInvoiceResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/invoices/{invoice_id}/metadata'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'invoice_id': invoice_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetInvoiceResponse.from_dictionary)

    def get_invoices(self,
                     page=None,
                     size=None,
                     code=None,
                     customer_id=None,
                     subscription_id=None,
                     created_since=None,
                     created_until=None,
                     status=None,
                     due_since=None,
                     due_until=None):
        """Does a GET request to /invoices.

        Gets all invoices

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            code (string, optional): Filter for Invoice's code
            customer_id (string, optional): Filter for Invoice's customer id
            subscription_id (string, optional): Filter for Invoice's
                subscription id
            created_since (datetime, optional): Filter for Invoice's creation
                date start range
            created_until (datetime, optional): Filter for Invoices creation
                date end range
            status (string, optional): Filter for Invoice's status
            due_since (datetime, optional): Filter for Invoice's due date
                start range
            due_until (datetime, optional): Filter for Invoice's due date end
                range

        Returns:
            ListInvoicesResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/invoices'
        _query_parameters = {
            'page': page,
            'size': size,
            'code': code,
            'customer_id': customer_id,
            'subscription_id': subscription_id,
            'created_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since),
            'created_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until),
            'status': status,
            'due_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, due_since),
            'due_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, due_until)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListInvoicesResponse.from_dictionary)

    def create_invoice(self,
                       subscription_id,
                       cycle_id):
        """Does a POST request to /subscriptions/{subscription_id}/cycles/{cycle_id}/pay.

        Create an Invoice

        Args:
            subscription_id (string): Subscription Id
            cycle_id (string): Cycle Id

        Returns:
            GetInvoiceResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/subscriptions/{subscription_id}/cycles/{cycle_id}/pay'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'subscription_id': subscription_id,
            'cycle_id': cycle_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetInvoiceResponse.from_dictionary)

    def update_invoice_status(self,
                              invoice_id,
                              request):
        """Does a PATCH request to /invoices/{invoice_id}/status.

        Updates the status from an invoice

        Args:
            invoice_id (string): Invoice Id
            request (UpdateInvoiceStatusRequest): Request for updating an
                invoice's status

        Returns:
            GetInvoiceResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/invoices/{invoice_id}/status'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'invoice_id': invoice_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetInvoiceResponse.from_dictionary)
