# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.1.0
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeleteProductsResponseData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'deleted_count': 'int'
    }

    attribute_map = {
        'deleted_count': 'deleted_count'
    }

    def __init__(self, deleted_count=None):
        """
        DeleteProductsResponseData - a model defined in Swagger
        """

        self._deleted_count = None

        if deleted_count is not None:
          self.deleted_count = deleted_count

    @property
    def deleted_count(self):
        """
        Gets the deleted_count of this DeleteProductsResponseData.

        :return: The deleted_count of this DeleteProductsResponseData.
        :rtype: int
        """
        return self._deleted_count

    @deleted_count.setter
    def deleted_count(self, deleted_count):
        """
        Sets the deleted_count of this DeleteProductsResponseData.

        :param deleted_count: The deleted_count of this DeleteProductsResponseData.
        :type: int
        """

        self._deleted_count = deleted_count

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DeleteProductsResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other