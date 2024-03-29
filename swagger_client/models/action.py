# coding: utf-8

"""
    Trello Api

    Trello Api generated from the online documentation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Action(object):
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
        'data': 'object',
        'id': 'str',
        'id_member_creator': 'str',
        'type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'id': 'id',
        'id_member_creator': 'idMemberCreator',
        'type': 'type'
    }

    def __init__(self, data=None, id=None, id_member_creator=None, type=None):  # noqa: E501
        """Action - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._id = None
        self._id_member_creator = None
        self._type = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if id is not None:
            self.id = id
        if id_member_creator is not None:
            self.id_member_creator = id_member_creator
        if type is not None:
            self.type = type

    @property
    def data(self):
        """Gets the data of this Action.  # noqa: E501

        Relevant information regarding the action  # noqa: E501

        :return: The data of this Action.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Action.

        Relevant information regarding the action  # noqa: E501

        :param data: The data of this Action.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def id(self):
        """Gets the id of this Action.  # noqa: E501

        The ID of the action  # noqa: E501

        :return: The id of this Action.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Action.

        The ID of the action  # noqa: E501

        :param id: The id of this Action.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id_member_creator(self):
        """Gets the id_member_creator of this Action.  # noqa: E501

        The ID of the member who caused the action  # noqa: E501

        :return: The id_member_creator of this Action.  # noqa: E501
        :rtype: str
        """
        return self._id_member_creator

    @id_member_creator.setter
    def id_member_creator(self, id_member_creator):
        """Sets the id_member_creator of this Action.

        The ID of the member who caused the action  # noqa: E501

        :param id_member_creator: The id_member_creator of this Action.  # noqa: E501
        :type: str
        """

        self._id_member_creator = id_member_creator

    @property
    def type(self):
        """Gets the type of this Action.  # noqa: E501

        The type of the action. See list of Action Types for options.  # noqa: E501

        :return: The type of this Action.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Action.

        The type of the action. See list of Action Types for options.  # noqa: E501

        :param type: The type of this Action.  # noqa: E501
        :type: str
        """

        self._type = type

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
