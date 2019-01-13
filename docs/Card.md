# Card

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_item_states** | [**list[ERRORUNKNOWN]**](.md) |  | [optional] 
**closed** | **bool** | Whether the card is closed (archived). Note: Archived lists and boards do not cascade archives to cards. A card can have closed: false but be on an archived board. | [optional] 
**desc** | **str** | The description for the card. Up to 16384 chars. | [optional] 
**due_complete** | **bool** | Whether the due date has been marked complete | [optional] 
**id** | **str** | The ID of the card | [optional] 
**id_attachment_cover** | **str** | The id of the attachment selected as the cover image, if one exists | [optional] 
**id_board** | **str** | The ID of the board the card is on | [optional] 
**id_checklists** | [**list[ERRORUNKNOWN]**](.md) | An array of checklist IDs that are on this card | [optional] 
**id_labels** | [**list[ERRORUNKNOWN]**](.md) | An array of label IDs that are on this card | [optional] 
**id_list** | **str** | The ID of the list the card is in | [optional] 
**id_members** | [**list[ERRORUNKNOWN]**](.md) | An array of member IDs that are on this card | [optional] 
**id_members_voted** | [**list[ERRORUNKNOWN]**](.md) | An array of member IDs who have voted on this card | [optional] 
**id_short** | **int** | Numeric ID for the card on this board. Only unique to the board, and subject to change as the card moves | [optional] 
**labels** | [**list[ERRORUNKNOWN]**](.md) | Array of label objects on this card | [optional] 
**manual_cover_attachment** | **bool** | Whether the card cover image was selected automatically by Trello, or manually by the user | [optional] 
**name** | **str** | Name of the card | [optional] 
**short_link** | **str** | The 8 character shortened ID for the card | [optional] 
**short_url** | **str** | URL to the card without the name slug | [optional] 
**subscribed** | **bool** | Whether this member is subscribed to the card | [optional] 
**url** | **str** | Full URL to the card, with the name slug | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


