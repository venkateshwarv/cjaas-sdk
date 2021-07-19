# coding: utf-8

"""
    Azure Functions OpenAPI Extension

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProfileViewQueryResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'customer_id': 'str',
        'generated_at': 'datetime',
        'attribute_view': 'list[ProfileAttributeView]'
    }

    attribute_map = {
        'name': 'name',
        'customer_id': 'customerId',
        'generated_at': 'generatedAt',
        'attribute_view': 'attributeView'
    }

    def __init__(self, name=None, customer_id=None, generated_at=None, attribute_view=None):  # noqa: E501
        """ProfileViewQueryResponse - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._customer_id = None
        self._generated_at = None
        self._attribute_view = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if customer_id is not None:
            self.customer_id = customer_id
        if generated_at is not None:
            self.generated_at = generated_at
        if attribute_view is not None:
            self.attribute_view = attribute_view

    @property
    def name(self):
        """Gets the name of this ProfileViewQueryResponse.  # noqa: E501


        :return: The name of this ProfileViewQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileViewQueryResponse.


        :param name: The name of this ProfileViewQueryResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def customer_id(self):
        """Gets the customer_id of this ProfileViewQueryResponse.  # noqa: E501


        :return: The customer_id of this ProfileViewQueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ProfileViewQueryResponse.


        :param customer_id: The customer_id of this ProfileViewQueryResponse.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def generated_at(self):
        """Gets the generated_at of this ProfileViewQueryResponse.  # noqa: E501


        :return: The generated_at of this ProfileViewQueryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._generated_at

    @generated_at.setter
    def generated_at(self, generated_at):
        """Sets the generated_at of this ProfileViewQueryResponse.


        :param generated_at: The generated_at of this ProfileViewQueryResponse.  # noqa: E501
        :type: datetime
        """

        self._generated_at = generated_at

    @property
    def attribute_view(self):
        """Gets the attribute_view of this ProfileViewQueryResponse.  # noqa: E501


        :return: The attribute_view of this ProfileViewQueryResponse.  # noqa: E501
        :rtype: list[ProfileAttributeView]
        """
        return self._attribute_view

    @attribute_view.setter
    def attribute_view(self, attribute_view):
        """Sets the attribute_view of this ProfileViewQueryResponse.


        :param attribute_view: The attribute_view of this ProfileViewQueryResponse.  # noqa: E501
        :type: list[ProfileAttributeView]
        """

        self._attribute_view = attribute_view

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProfileViewQueryResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProfileViewQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other