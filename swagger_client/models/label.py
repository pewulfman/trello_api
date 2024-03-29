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


class Label(object):
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
        'color': 'str',
        'id': 'str',
        'id_board': 'str',
        'name': 'str'
    }

    attribute_map = {
        'color': 'color',
        'id': 'id',
        'id_board': 'idBoard',
        'name': 'name'
    }

    def __init__(self, color=None, id=None, id_board=None, name=None):  # noqa: E501
        """Label - a model defined in Swagger"""  # noqa: E501

        self._color = None
        self._id = None
        self._id_board = None
        self._name = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if id is not None:
            self.id = id
        if id_board is not None:
            self.id_board = id_board
        if name is not None:
            self.name = name

    @property
    def color(self):
        """Gets the color of this Label.  # noqa: E501

        The color of the label. One of: yellow, purple, blue, red, green, orange, black, sky, pink, lime, null (null means no color, and the label will not show on the front of cards)  # noqa: E501

        :return: The color of this Label.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Label.

        The color of the label. One of: yellow, purple, blue, red, green, orange, black, sky, pink, lime, null (null means no color, and the label will not show on the front of cards)  # noqa: E501

        :param color: The color of this Label.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def id(self):
        """Gets the id of this Label.  # noqa: E501

        The ID of the label  # noqa: E501

        :return: The id of this Label.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Label.

        The ID of the label  # noqa: E501

        :param id: The id of this Label.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id_board(self):
        """Gets the id_board of this Label.  # noqa: E501

        The ID of the board the label is on  # noqa: E501

        :return: The id_board of this Label.  # noqa: E501
        :rtype: str
        """
        return self._id_board

    @id_board.setter
    def id_board(self, id_board):
        """Sets the id_board of this Label.

        The ID of the board the label is on  # noqa: E501

        :param id_board: The id_board of this Label.  # noqa: E501
        :type: str
        """

        self._id_board = id_board

    @property
    def name(self):
        """Gets the name of this Label.  # noqa: E501

        The optional name of the label (0 - 16384 chars)  # noqa: E501

        :return: The name of this Label.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Label.

        The optional name of the label (0 - 16384 chars)  # noqa: E501

        :param name: The name of this Label.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, Label):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
