# Custom

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **object** | An object that contains this custom fields display properties. { cardFront: true } | [optional] 
**field_group** | **str** | A hash created from the fields of a Custom Field used to manage Custom Fields and values between boards. For more on its use, check out the Grouping Custom Fields Across Boards section of the Custom Fields guide. | [optional] 
**id** | **str** | The ID of the Custom Field definition. | [optional] 
**id_model** | **str** | The ID of the model that they Custom Field is defined on. This should always be an ID of a board. | [optional] 
**model_type** | **str** | The type of model that the Custom Field is being defined for. This should always be board. | [optional] 
**name** | **str** | The name of the Custom Field. This is displayed to the user in the Trello clients. | [optional] 
**options** | [**list[ERRORUNKNOWN]**](.md) | An array of objects used for Custom Fields of the list type. The objects contain data about the options available for the dropdown. | [optional] 
**pos** | **str** | The position of the Custom Field. This will be used to determine the order that Custom Fields should be listed when being shown to the user. | [optional] 
**type** | **str** | Determines the type of values that can be used when setting values for Custom Fields on cards. Should be one of: number, date, text, checkbox, and list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


