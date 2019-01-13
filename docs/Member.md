# Member

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_hash** | **str** | Member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{avatarHash}/{size}.png size can be 30, 50, or 170 | [optional] 
**avatar_url** | **str** | The URL of the current avatar being used, regardless of whether it is a gravatar or uploaded avatar. | [optional] 
**bio** | **str** | Optional bio for the member | [optional] 
**bio_data** | **object** | If the bio includes custom emoji, this object will contain the information necessary to display them. | [optional] 
**confirmed** | **bool** | Whether the member has confirmed their email address after signing up | [optional] 
**email** | **str** | The primary email address for the member. You can only read your own. | [optional] 
**full_name** | **str** | The full display name for the member | [optional] 
**gravatar_hash** | **str** | Same as avatarHash above; member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{gravatarHash}/{size}.png size can be 30, 50, or 170 string. | [optional] 
**id** | **str** | The ID of the member | [optional] 
**id_boards** | [**list[ERRORUNKNOWN]**](.md) | An array of board IDs this member is on | [optional] 
**id_boards_pinned** | [**list[ERRORUNKNOWN]**](.md) | deprecated | [optional] 
**id_enterprises_admin** | [**list[ERRORUNKNOWN]**](.md) | An array of enterprise IDs this member is an admin of | [optional] 
**id_organizations** | [**list[ERRORUNKNOWN]**](.md) | An array of organization IDs this member is in | [optional] 
**id_prem_orgs_admin** | [**list[ERRORUNKNOWN]**](.md) |  | [optional] 
**initials** | **str** | The member&#39;s initials, used for display when there isn&#39;t an avatar set | [optional] 
**one_time_messages_dismissed** | [**list[ERRORUNKNOWN]**](.md) |  | [optional] 
**prefs** | **object** | \&quot;prefs\&quot;: {     \&quot;sendSummaries\&quot;: true,     \&quot;minutesBetweenSummaries\&quot;: -1,     \&quot;minutesBeforeDeadlineToNotify\&quot;: 1440,     \&quot;colorBlind\&quot;: false,     \&quot;locale\&quot;: \&quot;en-US\&quot;,     \&quot;timezoneInfo\&quot;: {       \&quot;timezoneNext\&quot;: \&quot;EST\&quot;,       \&quot;dateNext\&quot;: \&quot;2017-11-05T06:00:00.000Z\&quot;,       \&quot;offsetNext\&quot;: 300,       \&quot;timezoneCurrent\&quot;: \&quot;EDT\&quot;,       \&quot;offsetCurrent\&quot;: 240     },     \&quot;twoFactor\&quot;: {       \&quot;enabled\&quot;: true,       \&quot;needsNewBackups\&quot;: false     }   }  | [optional] 
**products** | [**list[ERRORUNKNOWN]**](.md) | 10 - member has Trello Gold as a result of being in a Business Class team 37 - member has monthly Trello Gold 38 - member has annual Trello Gold | [optional] 
**status** | **str** | deprecated | [optional] 
**trophies** | [**list[ERRORUNKNOWN]**](.md) | deprecated | [optional] 
**uploaded_avatar_hash** | **str** | Same as avatarHash - member profile images are hosted at: https://trello-avatars.s3.amazonaws.com/{uploadedAvatarHash}/{size}.png size can be 30, 50, or 170 | [optional] 
**uploaded_avatar_url** | **str** | The URL of the uploaded avatar if one has been uploaded. | [optional] 
**url** | **str** | The URL to the member&#39;s profile page | [optional] 
**username** | **str** | The username for the member. What is shown in @mentions for example | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


