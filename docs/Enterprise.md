# Enterprise

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Long-form name of the enterprise used when displaying the full name of the enterprise. Example: Trello&#39;s Enterprise | [optional] 
**id** | **str** | The ID of the enterprise. | [optional] 
**id_admins** | [**list[ERRORUNKNOWN]**](.md) | Array of Member IDs that are admins of the enterprise. | [optional] 
**id_members** | [**list[ERRORUNKNOWN]**](.md) | Array of Member IDs that belong to the enterprise. | [optional] 
**id_organizations** | [**list[ERRORUNKNOWN]**](.md) | Array of Organization IDs that belong to the enterprise. | [optional] 
**name** | **str** | Short-form name of the enterprise. Example: test_enterprise. | [optional] 
**prefs** | **object** | JSON Object containing information about the preferences set within the enterprise. Example: {   \&quot;ssoOnly\&quot;: false,   \&quot;signup\&quot;: {     \&quot;message\&quot;: \&quot;😁 Howdy, friends.\&quot;,     \&quot;confirmation\&quot;: \&quot;We&#39;re confirming that you are a 💫.\&quot;,     \&quot;banner\&quot;: \&quot;Banner Text!\&quot;,     \&quot;bannerHtml\&quot;: \&quot;&lt;p&gt;Banner Text!&lt;/p&gt;\\n\&quot;,     \&quot;confirmationHtml\&quot;: \&quot;&lt;p&gt;We&#39;re confirming that you are a 💫.&lt;/p&gt;\\n\&quot;,     \&quot;messageHtml\&quot;: \&quot;&lt;p&gt;😁 Howdy, friends.&lt;/p&gt;\\n\&quot;   },   \&quot;mandatoryTransferDate\&quot;: null,   \&quot;maxMembers\&quot;: null }  | [optional] 
**products** | [**list[ERRORUNKNOWN]**](.md) | Array of products that the enterprise has enabled. | [optional] 
**sso_activation_failed** | **bool** | Determines whether SSO successfully activated. | [optional] 
**user_types** | **object** | Object containing keys for every member type (all, member, collaborator, saml, none) and values representing the count of each type of member. For example: {   \&quot;all\&quot;: 6,   \&quot;member\&quot;: 5,   \&quot;collaborator\&quot;: 0,   \&quot;saml\&quot;: 0,   \&quot;none\&quot;: 1 }  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


