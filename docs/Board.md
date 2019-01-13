# Board

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed** | **bool** | Boolean whether the board has been closed or not. | [optional] 
**desc** | **str** | The description of the board. Deprecated | [optional] 
**desc_data** | **str** | If the description includes custom emoji, this will contain the data necessary to display them. | [optional] 
**id** | **str** | The ID of the board | [optional] 
**id_organization** | **str** | MongoID of the organization to which the board belongs. | [optional] 
**label_names** | **object** | Object containing color keys and the label names given for one label of each color on the board. To get a full list of labels on the board see /boards/{id}/labels/. | [optional] 
**limits** | **object** | An object containing information on the limits that exist for the board. Read more about at Limits. | [optional] 
**memberships** | [**list[ERRORUNKNOWN]**](.md) | Array of objects that represent the relationship of users to this board as memberships. | [optional] 
**name** | **str** | The name of the board | [optional] 
**pinned** | **bool** | Boolean whether the board has been pinned or not. | [optional] 
**prefs** | **object** | Short for \&quot;preferences\&quot;, these are the settings for the board | [optional] 
**short_url** | **str** | URL for the board using only its shortMongoID | [optional] 
**starred** | **bool** | Whether the board has been starred by the current request&#39;s user. | [optional] 
**url** | **str** | Persistent URL for the board. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


