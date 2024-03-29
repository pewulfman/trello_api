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


class Member(object):
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
        'avatar_hash': 'str',
        'avatar_url': 'str',
        'bio': 'str',
        'bio_data': 'object',
        'confirmed': 'bool',
        'email': 'str',
        'full_name': 'str',
        'gravatar_hash': 'str',
        'id': 'str',
        'id_boards': 'list[ERRORUNKNOWN]',
        'id_boards_pinned': 'list[ERRORUNKNOWN]',
        'id_enterprises_admin': 'list[ERRORUNKNOWN]',
        'id_organizations': 'list[ERRORUNKNOWN]',
        'id_prem_orgs_admin': 'list[ERRORUNKNOWN]',
        'initials': 'str',
        'one_time_messages_dismissed': 'list[ERRORUNKNOWN]',
        'prefs': 'object',
        'products': 'list[ERRORUNKNOWN]',
        'status': 'str',
        'trophies': 'list[ERRORUNKNOWN]',
        'uploaded_avatar_hash': 'str',
        'uploaded_avatar_url': 'str',
        'url': 'str',
        'username': 'str'
    }

    attribute_map = {
        'avatar_hash': 'avatarHash',
        'avatar_url': 'avatarUrl',
        'bio': 'bio',
        'bio_data': 'bioData',
        'confirmed': 'confirmed',
        'email': 'email',
        'full_name': 'fullName',
        'gravatar_hash': 'gravatarHash',
        'id': 'id',
        'id_boards': 'idBoards',
        'id_boards_pinned': 'idBoardsPinned',
        'id_enterprises_admin': 'idEnterprisesAdmin',
        'id_organizations': 'idOrganizations',
        'id_prem_orgs_admin': 'idPremOrgsAdmin',
        'initials': 'initials',
        'one_time_messages_dismissed': 'oneTimeMessagesDismissed',
        'prefs': 'prefs',
        'products': 'products',
        'status': 'status',
        'trophies': 'trophies',
        'uploaded_avatar_hash': 'uploadedAvatarHash',
        'uploaded_avatar_url': 'uploadedAvatarUrl',
        'url': 'url',
        'username': 'username'
    }

    def __init__(self, avatar_hash=None, avatar_url=None, bio=None, bio_data=None, confirmed=None, email=None, full_name=None, gravatar_hash=None, id=None, id_boards=None, id_boards_pinned=None, id_enterprises_admin=None, id_organizations=None, id_prem_orgs_admin=None, initials=None, one_time_messages_dismissed=None, prefs=None, products=None, status=None, trophies=None, uploaded_avatar_hash=None, uploaded_avatar_url=None, url=None, username=None):  # noqa: E501
        """Member - a model defined in Swagger"""  # noqa: E501

        self._avatar_hash = None
        self._avatar_url = None
        self._bio = None
        self._bio_data = None
        self._confirmed = None
        self._email = None
        self._full_name = None
        self._gravatar_hash = None
        self._id = None
        self._id_boards = None
        self._id_boards_pinned = None
        self._id_enterprises_admin = None
        self._id_organizations = None
        self._id_prem_orgs_admin = None
        self._initials = None
        self._one_time_messages_dismissed = None
        self._prefs = None
        self._products = None
        self._status = None
        self._trophies = None
        self._uploaded_avatar_hash = None
        self._uploaded_avatar_url = None
        self._url = None
        self._username = None
        self.discriminator = None

        if avatar_hash is not None:
            self.avatar_hash = avatar_hash
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if bio is not None:
            self.bio = bio
        if bio_data is not None:
            self.bio_data = bio_data
        if confirmed is not None:
            self.confirmed = confirmed
        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if gravatar_hash is not None:
            self.gravatar_hash = gravatar_hash
        if id is not None:
            self.id = id
        if id_boards is not None:
            self.id_boards = id_boards
        if id_boards_pinned is not None:
            self.id_boards_pinned = id_boards_pinned
        if id_enterprises_admin is not None:
            self.id_enterprises_admin = id_enterprises_admin
        if id_organizations is not None:
            self.id_organizations = id_organizations
        if id_prem_orgs_admin is not None:
            self.id_prem_orgs_admin = id_prem_orgs_admin
        if initials is not None:
            self.initials = initials
        if one_time_messages_dismissed is not None:
            self.one_time_messages_dismissed = one_time_messages_dismissed
        if prefs is not None:
            self.prefs = prefs
        if products is not None:
            self.products = products
        if status is not None:
            self.status = status
        if trophies is not None:
            self.trophies = trophies
        if uploaded_avatar_hash is not None:
            self.uploaded_avatar_hash = uploaded_avatar_hash
        if uploaded_avatar_url is not None:
            self.uploaded_avatar_url = uploaded_avatar_url
        if url is not None:
            self.url = url
        if username is not None:
            self.username = username

    @property
    def avatar_hash(self):
        """Gets the avatar_hash of this Member.  # noqa: E501

        Member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{avatarHash}/{size}.png size can be 30, 50, or 170  # noqa: E501

        :return: The avatar_hash of this Member.  # noqa: E501
        :rtype: str
        """
        return self._avatar_hash

    @avatar_hash.setter
    def avatar_hash(self, avatar_hash):
        """Sets the avatar_hash of this Member.

        Member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{avatarHash}/{size}.png size can be 30, 50, or 170  # noqa: E501

        :param avatar_hash: The avatar_hash of this Member.  # noqa: E501
        :type: str
        """

        self._avatar_hash = avatar_hash

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Member.  # noqa: E501

        The URL of the current avatar being used, regardless of whether it is a gravatar or uploaded avatar.  # noqa: E501

        :return: The avatar_url of this Member.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Member.

        The URL of the current avatar being used, regardless of whether it is a gravatar or uploaded avatar.  # noqa: E501

        :param avatar_url: The avatar_url of this Member.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def bio(self):
        """Gets the bio of this Member.  # noqa: E501

        Optional bio for the member  # noqa: E501

        :return: The bio of this Member.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this Member.

        Optional bio for the member  # noqa: E501

        :param bio: The bio of this Member.  # noqa: E501
        :type: str
        """

        self._bio = bio

    @property
    def bio_data(self):
        """Gets the bio_data of this Member.  # noqa: E501

        If the bio includes custom emoji, this object will contain the information necessary to display them.  # noqa: E501

        :return: The bio_data of this Member.  # noqa: E501
        :rtype: object
        """
        return self._bio_data

    @bio_data.setter
    def bio_data(self, bio_data):
        """Sets the bio_data of this Member.

        If the bio includes custom emoji, this object will contain the information necessary to display them.  # noqa: E501

        :param bio_data: The bio_data of this Member.  # noqa: E501
        :type: object
        """

        self._bio_data = bio_data

    @property
    def confirmed(self):
        """Gets the confirmed of this Member.  # noqa: E501

        Whether the member has confirmed their email address after signing up  # noqa: E501

        :return: The confirmed of this Member.  # noqa: E501
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this Member.

        Whether the member has confirmed their email address after signing up  # noqa: E501

        :param confirmed: The confirmed of this Member.  # noqa: E501
        :type: bool
        """

        self._confirmed = confirmed

    @property
    def email(self):
        """Gets the email of this Member.  # noqa: E501

        The primary email address for the member. You can only read your own.  # noqa: E501

        :return: The email of this Member.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Member.

        The primary email address for the member. You can only read your own.  # noqa: E501

        :param email: The email of this Member.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this Member.  # noqa: E501

        The full display name for the member  # noqa: E501

        :return: The full_name of this Member.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Member.

        The full display name for the member  # noqa: E501

        :param full_name: The full_name of this Member.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def gravatar_hash(self):
        """Gets the gravatar_hash of this Member.  # noqa: E501

        Same as avatarHash above; member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{gravatarHash}/{size}.png size can be 30, 50, or 170 string.  # noqa: E501

        :return: The gravatar_hash of this Member.  # noqa: E501
        :rtype: str
        """
        return self._gravatar_hash

    @gravatar_hash.setter
    def gravatar_hash(self, gravatar_hash):
        """Sets the gravatar_hash of this Member.

        Same as avatarHash above; member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{gravatarHash}/{size}.png size can be 30, 50, or 170 string.  # noqa: E501

        :param gravatar_hash: The gravatar_hash of this Member.  # noqa: E501
        :type: str
        """

        self._gravatar_hash = gravatar_hash

    @property
    def id(self):
        """Gets the id of this Member.  # noqa: E501

        The ID of the member  # noqa: E501

        :return: The id of this Member.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.

        The ID of the member  # noqa: E501

        :param id: The id of this Member.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id_boards(self):
        """Gets the id_boards of this Member.  # noqa: E501

        An array of board IDs this member is on  # noqa: E501

        :return: The id_boards of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._id_boards

    @id_boards.setter
    def id_boards(self, id_boards):
        """Sets the id_boards of this Member.

        An array of board IDs this member is on  # noqa: E501

        :param id_boards: The id_boards of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._id_boards = id_boards

    @property
    def id_boards_pinned(self):
        """Gets the id_boards_pinned of this Member.  # noqa: E501

        deprecated  # noqa: E501

        :return: The id_boards_pinned of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._id_boards_pinned

    @id_boards_pinned.setter
    def id_boards_pinned(self, id_boards_pinned):
        """Sets the id_boards_pinned of this Member.

        deprecated  # noqa: E501

        :param id_boards_pinned: The id_boards_pinned of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._id_boards_pinned = id_boards_pinned

    @property
    def id_enterprises_admin(self):
        """Gets the id_enterprises_admin of this Member.  # noqa: E501

        An array of enterprise IDs this member is an admin of  # noqa: E501

        :return: The id_enterprises_admin of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._id_enterprises_admin

    @id_enterprises_admin.setter
    def id_enterprises_admin(self, id_enterprises_admin):
        """Sets the id_enterprises_admin of this Member.

        An array of enterprise IDs this member is an admin of  # noqa: E501

        :param id_enterprises_admin: The id_enterprises_admin of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._id_enterprises_admin = id_enterprises_admin

    @property
    def id_organizations(self):
        """Gets the id_organizations of this Member.  # noqa: E501

        An array of organization IDs this member is in  # noqa: E501

        :return: The id_organizations of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._id_organizations

    @id_organizations.setter
    def id_organizations(self, id_organizations):
        """Sets the id_organizations of this Member.

        An array of organization IDs this member is in  # noqa: E501

        :param id_organizations: The id_organizations of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._id_organizations = id_organizations

    @property
    def id_prem_orgs_admin(self):
        """Gets the id_prem_orgs_admin of this Member.  # noqa: E501

          # noqa: E501

        :return: The id_prem_orgs_admin of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._id_prem_orgs_admin

    @id_prem_orgs_admin.setter
    def id_prem_orgs_admin(self, id_prem_orgs_admin):
        """Sets the id_prem_orgs_admin of this Member.

          # noqa: E501

        :param id_prem_orgs_admin: The id_prem_orgs_admin of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._id_prem_orgs_admin = id_prem_orgs_admin

    @property
    def initials(self):
        """Gets the initials of this Member.  # noqa: E501

        The member's initials, used for display when there isn't an avatar set  # noqa: E501

        :return: The initials of this Member.  # noqa: E501
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials):
        """Sets the initials of this Member.

        The member's initials, used for display when there isn't an avatar set  # noqa: E501

        :param initials: The initials of this Member.  # noqa: E501
        :type: str
        """

        self._initials = initials

    @property
    def one_time_messages_dismissed(self):
        """Gets the one_time_messages_dismissed of this Member.  # noqa: E501

          # noqa: E501

        :return: The one_time_messages_dismissed of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._one_time_messages_dismissed

    @one_time_messages_dismissed.setter
    def one_time_messages_dismissed(self, one_time_messages_dismissed):
        """Sets the one_time_messages_dismissed of this Member.

          # noqa: E501

        :param one_time_messages_dismissed: The one_time_messages_dismissed of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._one_time_messages_dismissed = one_time_messages_dismissed

    @property
    def prefs(self):
        """Gets the prefs of this Member.  # noqa: E501

        \"prefs\": {     \"sendSummaries\": true,     \"minutesBetweenSummaries\": -1,     \"minutesBeforeDeadlineToNotify\": 1440,     \"colorBlind\": false,     \"locale\": \"en-US\",     \"timezoneInfo\": {       \"timezoneNext\": \"EST\",       \"dateNext\": \"2017-11-05T06:00:00.000Z\",       \"offsetNext\": 300,       \"timezoneCurrent\": \"EDT\",       \"offsetCurrent\": 240     },     \"twoFactor\": {       \"enabled\": true,       \"needsNewBackups\": false     }   }   # noqa: E501

        :return: The prefs of this Member.  # noqa: E501
        :rtype: object
        """
        return self._prefs

    @prefs.setter
    def prefs(self, prefs):
        """Sets the prefs of this Member.

        \"prefs\": {     \"sendSummaries\": true,     \"minutesBetweenSummaries\": -1,     \"minutesBeforeDeadlineToNotify\": 1440,     \"colorBlind\": false,     \"locale\": \"en-US\",     \"timezoneInfo\": {       \"timezoneNext\": \"EST\",       \"dateNext\": \"2017-11-05T06:00:00.000Z\",       \"offsetNext\": 300,       \"timezoneCurrent\": \"EDT\",       \"offsetCurrent\": 240     },     \"twoFactor\": {       \"enabled\": true,       \"needsNewBackups\": false     }   }   # noqa: E501

        :param prefs: The prefs of this Member.  # noqa: E501
        :type: object
        """

        self._prefs = prefs

    @property
    def products(self):
        """Gets the products of this Member.  # noqa: E501

        10 - member has Trello Gold as a result of being in a Business Class team 37 - member has monthly Trello Gold 38 - member has annual Trello Gold  # noqa: E501

        :return: The products of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Member.

        10 - member has Trello Gold as a result of being in a Business Class team 37 - member has monthly Trello Gold 38 - member has annual Trello Gold  # noqa: E501

        :param products: The products of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._products = products

    @property
    def status(self):
        """Gets the status of this Member.  # noqa: E501

        deprecated  # noqa: E501

        :return: The status of this Member.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Member.

        deprecated  # noqa: E501

        :param status: The status of this Member.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def trophies(self):
        """Gets the trophies of this Member.  # noqa: E501

        deprecated  # noqa: E501

        :return: The trophies of this Member.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._trophies

    @trophies.setter
    def trophies(self, trophies):
        """Sets the trophies of this Member.

        deprecated  # noqa: E501

        :param trophies: The trophies of this Member.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._trophies = trophies

    @property
    def uploaded_avatar_hash(self):
        """Gets the uploaded_avatar_hash of this Member.  # noqa: E501

        Same as avatarHash - member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{uploadedAvatarHash}/{size}.png size can be 30, 50, or 170  # noqa: E501

        :return: The uploaded_avatar_hash of this Member.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_avatar_hash

    @uploaded_avatar_hash.setter
    def uploaded_avatar_hash(self, uploaded_avatar_hash):
        """Sets the uploaded_avatar_hash of this Member.

        Same as avatarHash - member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{uploadedAvatarHash}/{size}.png size can be 30, 50, or 170  # noqa: E501

        :param uploaded_avatar_hash: The uploaded_avatar_hash of this Member.  # noqa: E501
        :type: str
        """

        self._uploaded_avatar_hash = uploaded_avatar_hash

    @property
    def uploaded_avatar_url(self):
        """Gets the uploaded_avatar_url of this Member.  # noqa: E501

        The URL of the uploaded avatar if one has been uploaded.  # noqa: E501

        :return: The uploaded_avatar_url of this Member.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_avatar_url

    @uploaded_avatar_url.setter
    def uploaded_avatar_url(self, uploaded_avatar_url):
        """Sets the uploaded_avatar_url of this Member.

        The URL of the uploaded avatar if one has been uploaded.  # noqa: E501

        :param uploaded_avatar_url: The uploaded_avatar_url of this Member.  # noqa: E501
        :type: str
        """

        self._uploaded_avatar_url = uploaded_avatar_url

    @property
    def url(self):
        """Gets the url of this Member.  # noqa: E501

        The URL to the member's profile page  # noqa: E501

        :return: The url of this Member.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Member.

        The URL to the member's profile page  # noqa: E501

        :param url: The url of this Member.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username(self):
        """Gets the username of this Member.  # noqa: E501

        The username for the member. What is shown in @mentions for example  # noqa: E501

        :return: The username of this Member.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Member.

        The username for the member. What is shown in @mentions for example  # noqa: E501

        :param username: The username of this Member.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
