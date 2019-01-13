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


class Board(object):
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
        'closed': 'bool',
        'desc': 'str',
        'desc_data': 'str',
        'id': 'str',
        'id_organization': 'str',
        'label_names': 'object',
        'limits': 'object',
        'memberships': 'list[ERRORUNKNOWN]',
        'name': 'str',
        'pinned': 'bool',
        'prefs': 'object',
        'short_url': 'str',
        'starred': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'closed': 'closed',
        'desc': 'desc',
        'desc_data': 'descData',
        'id': 'id',
        'id_organization': 'idOrganization',
        'label_names': 'labelNames',
        'limits': 'limits',
        'memberships': 'memberships',
        'name': 'name',
        'pinned': 'pinned',
        'prefs': 'prefs',
        'short_url': 'shortUrl',
        'starred': 'starred',
        'url': 'url'
    }

    def __init__(self, closed=None, desc=None, desc_data=None, id=None, id_organization=None, label_names=None, limits=None, memberships=None, name=None, pinned=None, prefs=None, short_url=None, starred=None, url=None):  # noqa: E501
        """Board - a model defined in Swagger"""  # noqa: E501

        self._closed = None
        self._desc = None
        self._desc_data = None
        self._id = None
        self._id_organization = None
        self._label_names = None
        self._limits = None
        self._memberships = None
        self._name = None
        self._pinned = None
        self._prefs = None
        self._short_url = None
        self._starred = None
        self._url = None
        self.discriminator = None

        if closed is not None:
            self.closed = closed
        if desc is not None:
            self.desc = desc
        if desc_data is not None:
            self.desc_data = desc_data
        if id is not None:
            self.id = id
        if id_organization is not None:
            self.id_organization = id_organization
        if label_names is not None:
            self.label_names = label_names
        if limits is not None:
            self.limits = limits
        if memberships is not None:
            self.memberships = memberships
        if name is not None:
            self.name = name
        if pinned is not None:
            self.pinned = pinned
        if prefs is not None:
            self.prefs = prefs
        if short_url is not None:
            self.short_url = short_url
        if starred is not None:
            self.starred = starred
        if url is not None:
            self.url = url

    @property
    def closed(self):
        """Gets the closed of this Board.  # noqa: E501

        Boolean whether the board has been closed or not.  # noqa: E501

        :return: The closed of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._closed

    @closed.setter
    def closed(self, closed):
        """Sets the closed of this Board.

        Boolean whether the board has been closed or not.  # noqa: E501

        :param closed: The closed of this Board.  # noqa: E501
        :type: bool
        """

        self._closed = closed

    @property
    def desc(self):
        """Gets the desc of this Board.  # noqa: E501

        The description of the board. Deprecated  # noqa: E501

        :return: The desc of this Board.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Board.

        The description of the board. Deprecated  # noqa: E501

        :param desc: The desc of this Board.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def desc_data(self):
        """Gets the desc_data of this Board.  # noqa: E501

        If the description includes custom emoji, this will contain the data necessary to display them.  # noqa: E501

        :return: The desc_data of this Board.  # noqa: E501
        :rtype: str
        """
        return self._desc_data

    @desc_data.setter
    def desc_data(self, desc_data):
        """Sets the desc_data of this Board.

        If the description includes custom emoji, this will contain the data necessary to display them.  # noqa: E501

        :param desc_data: The desc_data of this Board.  # noqa: E501
        :type: str
        """

        self._desc_data = desc_data

    @property
    def id(self):
        """Gets the id of this Board.  # noqa: E501

        The ID of the board  # noqa: E501

        :return: The id of this Board.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Board.

        The ID of the board  # noqa: E501

        :param id: The id of this Board.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id_organization(self):
        """Gets the id_organization of this Board.  # noqa: E501

        MongoID of the organization to which the board belongs.  # noqa: E501

        :return: The id_organization of this Board.  # noqa: E501
        :rtype: str
        """
        return self._id_organization

    @id_organization.setter
    def id_organization(self, id_organization):
        """Sets the id_organization of this Board.

        MongoID of the organization to which the board belongs.  # noqa: E501

        :param id_organization: The id_organization of this Board.  # noqa: E501
        :type: str
        """

        self._id_organization = id_organization

    @property
    def label_names(self):
        """Gets the label_names of this Board.  # noqa: E501

        Object containing color keys and the label names given for one label of each color on the board. To get a full list of labels on the board see /boards/{id}/labels/.  # noqa: E501

        :return: The label_names of this Board.  # noqa: E501
        :rtype: object
        """
        return self._label_names

    @label_names.setter
    def label_names(self, label_names):
        """Sets the label_names of this Board.

        Object containing color keys and the label names given for one label of each color on the board. To get a full list of labels on the board see /boards/{id}/labels/.  # noqa: E501

        :param label_names: The label_names of this Board.  # noqa: E501
        :type: object
        """

        self._label_names = label_names

    @property
    def limits(self):
        """Gets the limits of this Board.  # noqa: E501

        An object containing information on the limits that exist for the board. Read more about at Limits.  # noqa: E501

        :return: The limits of this Board.  # noqa: E501
        :rtype: object
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Board.

        An object containing information on the limits that exist for the board. Read more about at Limits.  # noqa: E501

        :param limits: The limits of this Board.  # noqa: E501
        :type: object
        """

        self._limits = limits

    @property
    def memberships(self):
        """Gets the memberships of this Board.  # noqa: E501

        Array of objects that represent the relationship of users to this board as memberships.  # noqa: E501

        :return: The memberships of this Board.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._memberships

    @memberships.setter
    def memberships(self, memberships):
        """Sets the memberships of this Board.

        Array of objects that represent the relationship of users to this board as memberships.  # noqa: E501

        :param memberships: The memberships of this Board.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._memberships = memberships

    @property
    def name(self):
        """Gets the name of this Board.  # noqa: E501

        The name of the board  # noqa: E501

        :return: The name of this Board.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Board.

        The name of the board  # noqa: E501

        :param name: The name of this Board.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pinned(self):
        """Gets the pinned of this Board.  # noqa: E501

        Boolean whether the board has been pinned or not.  # noqa: E501

        :return: The pinned of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this Board.

        Boolean whether the board has been pinned or not.  # noqa: E501

        :param pinned: The pinned of this Board.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def prefs(self):
        """Gets the prefs of this Board.  # noqa: E501

        Short for \"preferences\", these are the settings for the board  # noqa: E501

        :return: The prefs of this Board.  # noqa: E501
        :rtype: object
        """
        return self._prefs

    @prefs.setter
    def prefs(self, prefs):
        """Sets the prefs of this Board.

        Short for \"preferences\", these are the settings for the board  # noqa: E501

        :param prefs: The prefs of this Board.  # noqa: E501
        :type: object
        """

        self._prefs = prefs

    @property
    def short_url(self):
        """Gets the short_url of this Board.  # noqa: E501

        URL for the board using only its shortMongoID  # noqa: E501

        :return: The short_url of this Board.  # noqa: E501
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """Sets the short_url of this Board.

        URL for the board using only its shortMongoID  # noqa: E501

        :param short_url: The short_url of this Board.  # noqa: E501
        :type: str
        """

        self._short_url = short_url

    @property
    def starred(self):
        """Gets the starred of this Board.  # noqa: E501

        Whether the board has been starred by the current request's user.  # noqa: E501

        :return: The starred of this Board.  # noqa: E501
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        """Sets the starred of this Board.

        Whether the board has been starred by the current request's user.  # noqa: E501

        :param starred: The starred of this Board.  # noqa: E501
        :type: bool
        """

        self._starred = starred

    @property
    def url(self):
        """Gets the url of this Board.  # noqa: E501

        Persistent URL for the board.  # noqa: E501

        :return: The url of this Board.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Board.

        Persistent URL for the board.  # noqa: E501

        :param url: The url of this Board.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, Board):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other