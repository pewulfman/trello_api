# swagger_client.DefaultApi

All URIs are relative to *https://api.trello.com/1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_id_action_reactions_get**](DefaultApi.md#actions_id_action_reactions_get) | **GET** /actions/{idAction}/reactions | List reactions for an action
[**actions_id_action_reactions_id_delete**](DefaultApi.md#actions_id_action_reactions_id_delete) | **DELETE** /actions/{idAction}/reactions/{id} | Deletes a reaction
[**actions_id_action_reactions_id_get**](DefaultApi.md#actions_id_action_reactions_id_get) | **GET** /actions/{idAction}/reactions/{id} | Get information for a reaction
[**actions_id_action_reactions_post**](DefaultApi.md#actions_id_action_reactions_post) | **POST** /actions/{idAction}/reactions | Adds a new reaction to an action
[**actions_id_action_reactions_summary_get**](DefaultApi.md#actions_id_action_reactions_summary_get) | **GET** /actions/{idAction}/reactionsSummary | List a summary of all reactions for an action
[**actions_id_board_get**](DefaultApi.md#actions_id_board_get) | **GET** /actions/{id}/board | Get the board for an action
[**actions_id_card_get**](DefaultApi.md#actions_id_card_get) | **GET** /actions/{id}/card | Get the card for an action
[**actions_id_delete**](DefaultApi.md#actions_id_delete) | **DELETE** /actions/{id} | Delete a comment action
[**actions_id_display_get**](DefaultApi.md#actions_id_display_get) | **GET** /actions/{id}/display | Get the display information for an action.
[**actions_id_field_get**](DefaultApi.md#actions_id_field_get) | **GET** /actions/{id}/{field} | Get a specific property of an action
[**actions_id_get**](DefaultApi.md#actions_id_get) | **GET** /actions/{id} | Get information about an action
[**actions_id_list_get**](DefaultApi.md#actions_id_list_get) | **GET** /actions/{id}/list | Get the list for an action
[**actions_id_member_creator_get**](DefaultApi.md#actions_id_member_creator_get) | **GET** /actions/{id}/memberCreator | Gets the member who created the action
[**actions_id_member_get**](DefaultApi.md#actions_id_member_get) | **GET** /actions/{id}/member | Gets the member of an action (not the creator)
[**actions_id_organization_get**](DefaultApi.md#actions_id_organization_get) | **GET** /actions/{id}/organization | Get the organization of an action
[**actions_id_put**](DefaultApi.md#actions_id_put) | **PUT** /actions/{id} | Update a comment action
[**actions_id_text_put**](DefaultApi.md#actions_id_text_put) | **PUT** /actions/{id}/text | Update a comment action
[**batch_get**](DefaultApi.md#batch_get) | **GET** /batch | 
[**boards_id_actions_get**](DefaultApi.md#boards_id_actions_get) | **GET** /boards/{id}/actions | 
[**boards_id_board_plugins_get**](DefaultApi.md#boards_id_board_plugins_get) | **GET** /boards/{id}/boardPlugins | Get the enabled Power-Ups on a board
[**boards_id_board_plugins_id_plugin_delete**](DefaultApi.md#boards_id_board_plugins_id_plugin_delete) | **DELETE** /boards/{id}/boardPlugins/{idPlugin} | Disable a Power-Up on a board
[**boards_id_board_plugins_post**](DefaultApi.md#boards_id_board_plugins_post) | **POST** /boards/{id}/boardPlugins | Enable a Power-Up on a board
[**boards_id_board_stars_get**](DefaultApi.md#boards_id_board_stars_get) | **GET** /boards/{id}/boardStars | 
[**boards_id_calendar_key_generate_post**](DefaultApi.md#boards_id_calendar_key_generate_post) | **POST** /boards/{id}/calendarKey/generate | Create a new board.
[**boards_id_cards_card_id_get**](DefaultApi.md#boards_id_cards_card_id_get) | **GET** /boards/{id}/cards/{cardId} | 
[**boards_id_cards_filter_get**](DefaultApi.md#boards_id_cards_filter_get) | **GET** /boards/{id}/cards/{filter} | 
[**boards_id_cards_get**](DefaultApi.md#boards_id_cards_get) | **GET** /boards/{id}/cards | 
[**boards_id_checklists_get**](DefaultApi.md#boards_id_checklists_get) | **GET** /boards/{id}/checklists | 
[**boards_id_checklists_post**](DefaultApi.md#boards_id_checklists_post) | **POST** /boards/{id}/checklists | Create a new checklist.
[**boards_id_custom_fields_get**](DefaultApi.md#boards_id_custom_fields_get) | **GET** /boards/{id}/customFields | Get the Custom Field Definitions that exist on a board.
[**boards_id_delete**](DefaultApi.md#boards_id_delete) | **DELETE** /boards/{id} | Delete a board.
[**boards_id_email_key_generate_post**](DefaultApi.md#boards_id_email_key_generate_post) | **POST** /boards/{id}/emailKey/generate | 
[**boards_id_field_get**](DefaultApi.md#boards_id_field_get) | **GET** /boards/{id}/{field} | 
[**boards_id_get**](DefaultApi.md#boards_id_get) | **GET** /boards/{id} | Request a single board.
[**boards_id_id_tags_post**](DefaultApi.md#boards_id_id_tags_post) | **POST** /boards/{id}/idTags | 
[**boards_id_labels_get**](DefaultApi.md#boards_id_labels_get) | **GET** /boards/{id}/labels | 
[**boards_id_labels_post**](DefaultApi.md#boards_id_labels_post) | **POST** /boards/{id}/labels | 
[**boards_id_lists_filter_get**](DefaultApi.md#boards_id_lists_filter_get) | **GET** /boards/{id}/lists/{filter} | 
[**boards_id_lists_get**](DefaultApi.md#boards_id_lists_get) | **GET** /boards/{id}/lists | 
[**boards_id_lists_post**](DefaultApi.md#boards_id_lists_post) | **POST** /boards/{id}/lists | 
[**boards_id_marked_as_viewed_post**](DefaultApi.md#boards_id_marked_as_viewed_post) | **POST** /boards/{id}/markedAsViewed | 
[**boards_id_members_get**](DefaultApi.md#boards_id_members_get) | **GET** /boards/{id}/members | Get the members for a board
[**boards_id_members_id_member_delete**](DefaultApi.md#boards_id_members_id_member_delete) | **DELETE** /boards/{id}/members/{idMember} | 
[**boards_id_members_id_member_put**](DefaultApi.md#boards_id_members_id_member_put) | **PUT** /boards/{id}/members/{idMember} | Add a member to the board.
[**boards_id_members_put**](DefaultApi.md#boards_id_members_put) | **PUT** /boards/{id}/members | Update an existing board by id
[**boards_id_memberships_get**](DefaultApi.md#boards_id_memberships_get) | **GET** /boards/{id}/memberships | Get information about the memberships users have to the board.
[**boards_id_memberships_id_membership_put**](DefaultApi.md#boards_id_memberships_id_membership_put) | **PUT** /boards/{id}/memberships/{idMembership} | Update an existing board by id
[**boards_id_my_prefs_email_position_put**](DefaultApi.md#boards_id_my_prefs_email_position_put) | **PUT** /boards/{id}/myPrefs/emailPosition | Update an existing board by id
[**boards_id_my_prefs_id_email_list_put**](DefaultApi.md#boards_id_my_prefs_id_email_list_put) | **PUT** /boards/{id}/myPrefs/idEmailList | Update an existing board by id
[**boards_id_my_prefs_show_list_guide_put**](DefaultApi.md#boards_id_my_prefs_show_list_guide_put) | **PUT** /boards/{id}/myPrefs/showListGuide | Update an existing board by id
[**boards_id_my_prefs_show_sidebar_activity_put**](DefaultApi.md#boards_id_my_prefs_show_sidebar_activity_put) | **PUT** /boards/{id}/myPrefs/showSidebarActivity | Update an existing board by id
[**boards_id_my_prefs_show_sidebar_board_actions_put**](DefaultApi.md#boards_id_my_prefs_show_sidebar_board_actions_put) | **PUT** /boards/{id}/myPrefs/showSidebarBoardActions | Update an existing board by id
[**boards_id_my_prefs_show_sidebar_members_put**](DefaultApi.md#boards_id_my_prefs_show_sidebar_members_put) | **PUT** /boards/{id}/myPrefs/showSidebarMembers | Update an existing board by id
[**boards_id_my_prefs_show_sidebar_put**](DefaultApi.md#boards_id_my_prefs_show_sidebar_put) | **PUT** /boards/{id}/myPrefs/showSidebar | Update an existing board by id
[**boards_id_plugins_get**](DefaultApi.md#boards_id_plugins_get) | **GET** /boards/{id}/plugins | List the Power-Ups for a board
[**boards_id_power_ups_post**](DefaultApi.md#boards_id_power_ups_post) | **POST** /boards/{id}/powerUps | 
[**boards_id_power_ups_power_up_delete**](DefaultApi.md#boards_id_power_ups_power_up_delete) | **DELETE** /boards/{id}/powerUps/{powerUp} | 
[**boards_id_put**](DefaultApi.md#boards_id_put) | **PUT** /boards/{id} | Update an existing board by id
[**boards_id_tags_get**](DefaultApi.md#boards_id_tags_get) | **GET** /boards/{id}/tags | 
[**boards_post**](DefaultApi.md#boards_post) | **POST** /boards/ | Create a new board.
[**card_id_card_custom_field_id_custom_field_item_put**](DefaultApi.md#card_id_card_custom_field_id_custom_field_item_put) | **PUT** /card/{idCard}/customField/{idCustomField}/item | Setting, updating, and removing the value for a Custom Field on a card.
[**cards_id_actions_comments_post**](DefaultApi.md#cards_id_actions_comments_post) | **POST** /cards/{id}/actions/comments | Add a new comment to a card
[**cards_id_actions_get**](DefaultApi.md#cards_id_actions_get) | **GET** /cards/{id}/actions | List the actions on a card
[**cards_id_actions_id_action_comments_delete**](DefaultApi.md#cards_id_actions_id_action_comments_delete) | **DELETE** /cards/{id}/actions/{idAction}/comments | Delete a comment
[**cards_id_actions_id_action_comments_put**](DefaultApi.md#cards_id_actions_id_action_comments_put) | **PUT** /cards/{id}/actions/{idAction}/comments | Update an existing comment
[**cards_id_attachments_get**](DefaultApi.md#cards_id_attachments_get) | **GET** /cards/{id}/attachments | List the attachments on a card
[**cards_id_attachments_id_attachment_delete**](DefaultApi.md#cards_id_attachments_id_attachment_delete) | **DELETE** /cards/{id}/attachments/{idAttachment} | Delete an attachment
[**cards_id_attachments_id_attachment_get**](DefaultApi.md#cards_id_attachments_id_attachment_get) | **GET** /cards/{id}/attachments/{idAttachment} | Get a specific attachment on a card
[**cards_id_attachments_post**](DefaultApi.md#cards_id_attachments_post) | **POST** /cards/{id}/attachments | Add an attachment to a card
[**cards_id_board_get**](DefaultApi.md#cards_id_board_get) | **GET** /cards/{id}/board | Get the board a card is on
[**cards_id_card_checklist_id_checklist_check_item_id_check_item_put**](DefaultApi.md#cards_id_card_checklist_id_checklist_check_item_id_check_item_put) | **PUT** /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem} | Update an item in a checklist on a card.
[**cards_id_check_item_id_check_item_delete**](DefaultApi.md#cards_id_check_item_id_check_item_delete) | **DELETE** /cards/{id}/checkItem/{idCheckItem} | Delete a checklist item
[**cards_id_check_item_id_check_item_get**](DefaultApi.md#cards_id_check_item_id_check_item_get) | **GET** /cards/{id}/checkItem/{idCheckItem} | Get a specific checkItem on a card
[**cards_id_check_item_id_check_item_put**](DefaultApi.md#cards_id_check_item_id_check_item_put) | **PUT** /cards/{id}/checkItem/{idCheckItem} | Update an item in a checklist on a card.
[**cards_id_check_item_states_get**](DefaultApi.md#cards_id_check_item_states_get) | **GET** /cards/{id}/checkItemStates | Get the completed checklist items on a card
[**cards_id_checklists_get**](DefaultApi.md#cards_id_checklists_get) | **GET** /cards/{id}/checklists | Get the checklists on a card
[**cards_id_checklists_id_checklist_delete**](DefaultApi.md#cards_id_checklists_id_checklist_delete) | **DELETE** /cards/{id}/checklists/{idChecklist} | Delete a checklist from a card
[**cards_id_checklists_post**](DefaultApi.md#cards_id_checklists_post) | **POST** /cards/{id}/checklists | Create a new checklist on a card
[**cards_id_custom_field_items_get**](DefaultApi.md#cards_id_custom_field_items_get) | **GET** /cards/{id}/customFieldItems | Get the custom field items for a card.
[**cards_id_delete**](DefaultApi.md#cards_id_delete) | **DELETE** /cards/{id} | Delete a card
[**cards_id_field_get**](DefaultApi.md#cards_id_field_get) | **GET** /cards/{id}/{field} | Get a specific property of a card
[**cards_id_get**](DefaultApi.md#cards_id_get) | **GET** /cards/{id} | Get a card by its ID
[**cards_id_id_labels_id_label_delete**](DefaultApi.md#cards_id_id_labels_id_label_delete) | **DELETE** /cards/{id}/idLabels/{idLabel} | Remove a label from a card
[**cards_id_id_labels_post**](DefaultApi.md#cards_id_id_labels_post) | **POST** /cards/{id}/idLabels | Add a label to a card
[**cards_id_id_members_id_member_delete**](DefaultApi.md#cards_id_id_members_id_member_delete) | **DELETE** /cards/{id}/idMembers/{idMember} | Remove a member from a card
[**cards_id_id_members_post**](DefaultApi.md#cards_id_id_members_post) | **POST** /cards/{id}/idMembers | Add a member to a card
[**cards_id_labels_post**](DefaultApi.md#cards_id_labels_post) | **POST** /cards/{id}/labels | Add a new label to a card
[**cards_id_list_get**](DefaultApi.md#cards_id_list_get) | **GET** /cards/{id}/list | Get the list a card is in
[**cards_id_mark_associated_notifications_read_post**](DefaultApi.md#cards_id_mark_associated_notifications_read_post) | **POST** /cards/{id}/markAssociatedNotificationsRead | Mark notifications about this card as read
[**cards_id_members_get**](DefaultApi.md#cards_id_members_get) | **GET** /cards/{id}/members | Get the members on a card
[**cards_id_members_voted_get**](DefaultApi.md#cards_id_members_voted_get) | **GET** /cards/{id}/membersVoted | Get the members who have voted on a card
[**cards_id_members_voted_id_member_delete**](DefaultApi.md#cards_id_members_voted_id_member_delete) | **DELETE** /cards/{id}/membersVoted/{idMember} | Remove a member&#39;s vote from a card
[**cards_id_members_voted_post**](DefaultApi.md#cards_id_members_voted_post) | **POST** /cards/{id}/membersVoted | Vote on the card
[**cards_id_plugin_data_get**](DefaultApi.md#cards_id_plugin_data_get) | **GET** /cards/{id}/pluginData | Get any shared pluginData on a card
[**cards_id_put**](DefaultApi.md#cards_id_put) | **PUT** /cards/{id} | Update a card
[**cards_id_stickers_get**](DefaultApi.md#cards_id_stickers_get) | **GET** /cards/{id}/stickers | Get the stickers on a card
[**cards_id_stickers_id_sticker_delete**](DefaultApi.md#cards_id_stickers_id_sticker_delete) | **DELETE** /cards/{id}/stickers/{idSticker} | Remove a sticker from the card
[**cards_id_stickers_id_sticker_get**](DefaultApi.md#cards_id_stickers_id_sticker_get) | **GET** /cards/{id}/stickers/{idSticker} | Get a specific sticker on a card
[**cards_id_stickers_id_sticker_put**](DefaultApi.md#cards_id_stickers_id_sticker_put) | **PUT** /cards/{id}/stickers/{idSticker} | Update a sticker on a card
[**cards_post**](DefaultApi.md#cards_post) | **POST** /cards | Create a new card
[**checklists_id_board_get**](DefaultApi.md#checklists_id_board_get) | **GET** /checklists/{id}/board | 
[**checklists_id_cards_get**](DefaultApi.md#checklists_id_cards_get) | **GET** /checklists/{id}/cards | 
[**checklists_id_check_items_get**](DefaultApi.md#checklists_id_check_items_get) | **GET** /checklists/{id}/checkItems | 
[**checklists_id_check_items_id_check_item_delete**](DefaultApi.md#checklists_id_check_items_id_check_item_delete) | **DELETE** /checklists/{id}/checkItems/{idCheckItem} | Remove an item from a checklist
[**checklists_id_check_items_id_check_item_get**](DefaultApi.md#checklists_id_check_items_id_check_item_get) | **GET** /checklists/{id}/checkItems/{idCheckItem} | 
[**checklists_id_check_items_id_check_item_put**](DefaultApi.md#checklists_id_check_items_id_check_item_put) | **PUT** /checklists/{id}/checkItems/{idCheckItem} | Update check item.
[**checklists_id_check_items_post**](DefaultApi.md#checklists_id_check_items_post) | **POST** /checklists/{id}/checkItems | 
[**checklists_id_delete**](DefaultApi.md#checklists_id_delete) | **DELETE** /checklists/{id} | Delete a checklist
[**checklists_id_field_get**](DefaultApi.md#checklists_id_field_get) | **GET** /checklists/{id}/{field} | 
[**checklists_id_get**](DefaultApi.md#checklists_id_get) | **GET** /checklists/{id} | 
[**checklists_id_name_put**](DefaultApi.md#checklists_id_name_put) | **PUT** /checklists/{id}/name | 
[**checklists_id_put**](DefaultApi.md#checklists_id_put) | **PUT** /checklists/{id} | Update an existing checklist.
[**checklists_post**](DefaultApi.md#checklists_post) | **POST** /checklists | 
[**custom_fields_id_delete**](DefaultApi.md#custom_fields_id_delete) | **DELETE** /customFields/{id} | Delete a Custom Field from a board.
[**custom_fields_id_get**](DefaultApi.md#custom_fields_id_get) | **GET** /customFields/{id} | 
[**custom_fields_id_options_get**](DefaultApi.md#custom_fields_id_options_get) | **GET** /customFields/{id}/options | Get the options of a drop down Custom Field
[**custom_fields_id_options_id_custom_field_option_get**](DefaultApi.md#custom_fields_id_options_id_custom_field_option_get) | **GET** /customFields/{id}/options/{idCustomFieldOption} | 
[**custom_fields_id_options_post**](DefaultApi.md#custom_fields_id_options_post) | **POST** /customFields/{id}/options | Add an option to a dropdown Custom Field
[**custom_fields_id_put**](DefaultApi.md#custom_fields_id_put) | **PUT** /customFields/{id} | Update a Custom Field definition.
[**custom_fields_post**](DefaultApi.md#custom_fields_post) | **POST** /customFields | Create a new Custom Field on a board.
[**customfields_id_options_id_custom_field_option_delete**](DefaultApi.md#customfields_id_options_id_custom_field_option_delete) | **DELETE** /customfields/{id}/options/{idCustomFieldOption} | Delete an option from a Custom Field dropdown.
[**emoji_get**](DefaultApi.md#emoji_get) | **GET** /emoji | List available emoji
[**enterprises_id_admins_get**](DefaultApi.md#enterprises_id_admins_get) | **GET** /enterprises/{id}/admins | Get an enterprise&#39;s admin members.
[**enterprises_id_admins_id_member_delete**](DefaultApi.md#enterprises_id_admins_id_member_delete) | **DELETE** /enterprises/{id}/admins/{idMember} | Remove an member as admin from an enterprise.
[**enterprises_id_admins_id_member_put**](DefaultApi.md#enterprises_id_admins_id_member_put) | **PUT** /enterprises/{id}/admins/{idMember} | Make member an admin of enterprise.
[**enterprises_id_get**](DefaultApi.md#enterprises_id_get) | **GET** /enterprises/{id} | Get an enterprise by its ID.
[**enterprises_id_members_get**](DefaultApi.md#enterprises_id_members_get) | **GET** /enterprises/{id}/members | Get the members of an enterprise.
[**enterprises_id_members_id_member_deactivated_put**](DefaultApi.md#enterprises_id_members_id_member_deactivated_put) | **PUT** /enterprises/{id}/members/{idMember}/deactivated | Deactivate a member of an enterprise.
[**enterprises_id_members_id_member_get**](DefaultApi.md#enterprises_id_members_id_member_get) | **GET** /enterprises/{id}/members/{idMember} | Get a specific member of an enterprise by ID.
[**enterprises_id_organizations_id_organization_delete**](DefaultApi.md#enterprises_id_organizations_id_organization_delete) | **DELETE** /enterprises/{id}/organizations/{idOrganization} | Remove an organization from an enterprise.
[**enterprises_id_organizations_put**](DefaultApi.md#enterprises_id_organizations_put) | **PUT** /enterprises/{id}/organizations | Transfer an organization to an enterprise.
[**enterprises_id_signup_url_get**](DefaultApi.md#enterprises_id_signup_url_get) | **GET** /enterprises/{id}/signupUrl | Get the signup URL for an enterprise.
[**enterprises_id_tokens_post**](DefaultApi.md#enterprises_id_tokens_post) | **POST** /enterprises/{id}/tokens | Generate an auth token for an enterprise.
[**enterprises_id_transferrable_organization_id_organization_get**](DefaultApi.md#enterprises_id_transferrable_organization_id_organization_get) | **GET** /enterprises/{id}/transferrable/organization/{idOrganization} | Get whether an organization can be transferred to an enterprise.
[**labels_id_color_put**](DefaultApi.md#labels_id_color_put) | **PUT** /labels/{id}/color | Update the color of a label by ID.
[**labels_id_delete**](DefaultApi.md#labels_id_delete) | **DELETE** /labels/{id} | Delete a label by ID.
[**labels_id_get**](DefaultApi.md#labels_id_get) | **GET** /labels/{id} | Get information about a label by ID.
[**labels_id_name_put**](DefaultApi.md#labels_id_name_put) | **PUT** /labels/{id}/name | Update the name of a label by ID.
[**labels_id_put**](DefaultApi.md#labels_id_put) | **PUT** /labels/{id} | Update a label by ID.
[**labels_post**](DefaultApi.md#labels_post) | **POST** /labels | Create a new label on a board.
[**lists_id_actions_get**](DefaultApi.md#lists_id_actions_get) | **GET** /lists/{id}/actions | List the actions on a list
[**lists_id_archive_all_cards_post**](DefaultApi.md#lists_id_archive_all_cards_post) | **POST** /lists/{id}/archiveAllCards | Archive all cards in a list
[**lists_id_board_get**](DefaultApi.md#lists_id_board_get) | **GET** /lists/{id}/board | Get the board a list is on
[**lists_id_cards_get**](DefaultApi.md#lists_id_cards_get) | **GET** /lists/{id}/cards | List the cards in a list
[**lists_id_closed_put**](DefaultApi.md#lists_id_closed_put) | **PUT** /lists/{id}/closed | Archive or unarchive a list
[**lists_id_field_get**](DefaultApi.md#lists_id_field_get) | **GET** /lists/{id}/{field} | Get a specific property of a list
[**lists_id_get**](DefaultApi.md#lists_id_get) | **GET** /lists/{id} | Get information about a list
[**lists_id_id_board_put**](DefaultApi.md#lists_id_id_board_put) | **PUT** /lists/{id}/idBoard | Move a list to a new board
[**lists_id_move_all_cards_post**](DefaultApi.md#lists_id_move_all_cards_post) | **POST** /lists/{id}/moveAllCards | Move all cards in a list
[**lists_id_name_put**](DefaultApi.md#lists_id_name_put) | **PUT** /lists/{id}/name | Rename a list
[**lists_id_pos_put**](DefaultApi.md#lists_id_pos_put) | **PUT** /lists/{id}/pos | Change the position of a list
[**lists_id_put**](DefaultApi.md#lists_id_put) | **PUT** /lists/{id} | Update the properties of a list
[**lists_id_subscribed_put**](DefaultApi.md#lists_id_subscribed_put) | **PUT** /lists/{id}/subscribed | Subscribe or unsubscribe from a list
[**lists_post**](DefaultApi.md#lists_post) | **POST** /lists | Create a new list on a board
[**members_id_actions_get**](DefaultApi.md#members_id_actions_get) | **GET** /members/{id}/actions | List the actions for a member
[**members_id_avatar_post**](DefaultApi.md#members_id_avatar_post) | **POST** /members/{id}/avatar | Create a new avatar for a member
[**members_id_board_backgrounds_get**](DefaultApi.md#members_id_board_backgrounds_get) | **GET** /members/{id}/boardBackgrounds | Get a member&#39;s custom board backgrounds
[**members_id_board_backgrounds_id_background_delete**](DefaultApi.md#members_id_board_backgrounds_id_background_delete) | **DELETE** /members/{id}/boardBackgrounds/{idBackground} | Delete a board background
[**members_id_board_backgrounds_id_background_get**](DefaultApi.md#members_id_board_backgrounds_id_background_get) | **GET** /members/{id}/boardBackgrounds/{idBackground} | Get a member&#39;s board background
[**members_id_board_backgrounds_id_background_put**](DefaultApi.md#members_id_board_backgrounds_id_background_put) | **PUT** /members/{id}/boardBackgrounds/{idBackground} | Update a board background
[**members_id_board_backgrounds_post**](DefaultApi.md#members_id_board_backgrounds_post) | **POST** /members/{id}/boardBackgrounds | Upload a new boardBackground
[**members_id_board_stars_get**](DefaultApi.md#members_id_board_stars_get) | **GET** /members/{id}/boardStars | List a member&#39;s board stars
[**members_id_board_stars_id_star_delete**](DefaultApi.md#members_id_board_stars_id_star_delete) | **DELETE** /members/{id}/boardStars/{idStar} | Unstar a board
[**members_id_board_stars_id_star_get**](DefaultApi.md#members_id_board_stars_id_star_get) | **GET** /members/{id}/boardStars/{idStar} | Get a specific boardStar
[**members_id_board_stars_id_star_put**](DefaultApi.md#members_id_board_stars_id_star_put) | **PUT** /members/{id}/boardStars/{idStar} | Update the position of a starred board
[**members_id_board_stars_post**](DefaultApi.md#members_id_board_stars_post) | **POST** /members/{id}/boardStars | Star a new board
[**members_id_boards_get**](DefaultApi.md#members_id_boards_get) | **GET** /members/{id}/boards | Lists the boards a member has access to
[**members_id_boards_invited_get**](DefaultApi.md#members_id_boards_invited_get) | **GET** /members/{id}/boardsInvited | Get the boards the member has been invited to
[**members_id_cards_get**](DefaultApi.md#members_id_cards_get) | **GET** /members/{id}/cards | Gets the cards a member is on
[**members_id_custom_board_backgrounds_get**](DefaultApi.md#members_id_custom_board_backgrounds_get) | **GET** /members/{id}/customBoardBackgrounds | Get a member&#39;s custom board backgrounds
[**members_id_custom_board_backgrounds_id_background_delete**](DefaultApi.md#members_id_custom_board_backgrounds_id_background_delete) | **DELETE** /members/{id}/customBoardBackgrounds/{idBackground} | Delete a custom board background
[**members_id_custom_board_backgrounds_id_background_get**](DefaultApi.md#members_id_custom_board_backgrounds_id_background_get) | **GET** /members/{id}/customBoardBackgrounds/{idBackground} | Get a specific custom board background
[**members_id_custom_board_backgrounds_id_background_put**](DefaultApi.md#members_id_custom_board_backgrounds_id_background_put) | **PUT** /members/{id}/customBoardBackgrounds/{idBackground} | 
[**members_id_custom_board_backgrounds_post**](DefaultApi.md#members_id_custom_board_backgrounds_post) | **POST** /members/{id}/customBoardBackgrounds | Upload a new custom board background
[**members_id_custom_emoji_get**](DefaultApi.md#members_id_custom_emoji_get) | **GET** /members/{id}/customEmoji | Get a member&#39;s uploaded custom emoji
[**members_id_custom_emoji_id_emoji_get**](DefaultApi.md#members_id_custom_emoji_id_emoji_get) | **GET** /members/{id}/customEmoji/{idEmoji} | Get a custom emoji
[**members_id_custom_emoji_post**](DefaultApi.md#members_id_custom_emoji_post) | **POST** /members/{id}/customEmoji | Upload a new custom emoji
[**members_id_custom_stickers_get**](DefaultApi.md#members_id_custom_stickers_get) | **GET** /members/{id}/customStickers | Get a member&#39;s uploaded stickers
[**members_id_custom_stickers_id_sticker_delete**](DefaultApi.md#members_id_custom_stickers_id_sticker_delete) | **DELETE** /members/{id}/customStickers/{idSticker} | Delete a custom sticker
[**members_id_custom_stickers_id_sticker_get**](DefaultApi.md#members_id_custom_stickers_id_sticker_get) | **GET** /members/{id}/customStickers/{idSticker} | Get an uploaded sticker
[**members_id_custom_stickers_post**](DefaultApi.md#members_id_custom_stickers_post) | **POST** /members/{id}/customStickers | Upload a new custom sticker
[**members_id_enterprises_get**](DefaultApi.md#members_id_enterprises_get) | **GET** /members/{id}/enterprises/ | Get the enterprises that a member belongs to.
[**members_id_field_get**](DefaultApi.md#members_id_field_get) | **GET** /members/{id}/{field} | Get a particular property of a member
[**members_id_get**](DefaultApi.md#members_id_get) | **GET** /members/{id} | Get a member
[**members_id_notifications_get**](DefaultApi.md#members_id_notifications_get) | **GET** /members/{id}/notifications | Get a member&#39;s notifications
[**members_id_one_time_messages_dismissed_post**](DefaultApi.md#members_id_one_time_messages_dismissed_post) | **POST** /members/{id}/oneTimeMessagesDismissed | Dismiss a message
[**members_id_organizations_get**](DefaultApi.md#members_id_organizations_get) | **GET** /members/{id}/organizations | Get a member&#39;s teams
[**members_id_organizations_invited_get**](DefaultApi.md#members_id_organizations_invited_get) | **GET** /members/{id}/organizationsInvited | Get a member&#39;s teams they have been invited to
[**members_id_put**](DefaultApi.md#members_id_put) | **PUT** /members/{id} | Update a member
[**members_id_saved_searches_get**](DefaultApi.md#members_id_saved_searches_get) | **GET** /members/{id}/savedSearches | List the saved searches of a member
[**members_id_saved_searches_id_search_delete**](DefaultApi.md#members_id_saved_searches_id_search_delete) | **DELETE** /members/{id}/savedSearches/{idSearch} | Delete a saved search
[**members_id_saved_searches_id_search_get**](DefaultApi.md#members_id_saved_searches_id_search_get) | **GET** /members/{id}/savedSearches/{idSearch} | Get a saved search
[**members_id_saved_searches_id_search_put**](DefaultApi.md#members_id_saved_searches_id_search_put) | **PUT** /members/{id}/savedSearches/{idSearch} | Update a saved search
[**members_id_saved_searches_post**](DefaultApi.md#members_id_saved_searches_post) | **POST** /members/{id}/savedSearches | Create a new saved search
[**members_id_tokens_get**](DefaultApi.md#members_id_tokens_get) | **GET** /members/{id}/tokens | List a members app tokens
[**notifications_all_read_post**](DefaultApi.md#notifications_all_read_post) | **POST** /notifications/all/read | Mark all notifications as read
[**notifications_id_board_get**](DefaultApi.md#notifications_id_board_get) | **GET** /notifications/{id}/board | Get the board a notification is associated with
[**notifications_id_card_get**](DefaultApi.md#notifications_id_card_get) | **GET** /notifications/{id}/card | Get the card a notification is associated with
[**notifications_id_field_get**](DefaultApi.md#notifications_id_field_get) | **GET** /notifications/{id}/{field} | Get a specific property of a notification
[**notifications_id_get**](DefaultApi.md#notifications_id_get) | **GET** /notifications/{id} | 
[**notifications_id_list_get**](DefaultApi.md#notifications_id_list_get) | **GET** /notifications/{id}/list | Get the list a notification is associated with
[**notifications_id_member_creator_get**](DefaultApi.md#notifications_id_member_creator_get) | **GET** /notifications/{id}/memberCreator | Get the member who created the notification
[**notifications_id_member_get**](DefaultApi.md#notifications_id_member_get) | **GET** /notifications/{id}/member | Get the member (not the creator) a notification is about
[**notifications_id_organization_get**](DefaultApi.md#notifications_id_organization_get) | **GET** /notifications/{id}/organization | Get the organization a notification is associated with
[**notifications_id_put**](DefaultApi.md#notifications_id_put) | **PUT** /notifications/{id} | Update the read status of a notification
[**notifications_id_unread_put**](DefaultApi.md#notifications_id_unread_put) | **PUT** /notifications/{id}/unread | Update the read status of a notification
[**organizations_id_actions_get**](DefaultApi.md#organizations_id_actions_get) | **GET** /organizations/{id}/actions | List the actions on a team
[**organizations_id_boards_get**](DefaultApi.md#organizations_id_boards_get) | **GET** /organizations/{id}/boards | List the boards in a team
[**organizations_id_delete**](DefaultApi.md#organizations_id_delete) | **DELETE** /organizations/{id} | Delete a team
[**organizations_id_exports_get**](DefaultApi.md#organizations_id_exports_get) | **GET** /organizations/{id}/exports | Retrieve the exports that exist for the given organization
[**organizations_id_exports_post**](DefaultApi.md#organizations_id_exports_post) | **POST** /organizations/{id}/exports | Kick off CSV export for an organization
[**organizations_id_field_get**](DefaultApi.md#organizations_id_field_get) | **GET** /organizations/{id}/{field} | 
[**organizations_id_get**](DefaultApi.md#organizations_id_get) | **GET** /organizations/{id} | 
[**organizations_id_logo_delete**](DefaultApi.md#organizations_id_logo_delete) | **DELETE** /organizations/{id}/logo | Delete a the logo from a team
[**organizations_id_logo_post**](DefaultApi.md#organizations_id_logo_post) | **POST** /organizations/{id}/logo | Set the logo image for a team
[**organizations_id_members_filter_get**](DefaultApi.md#organizations_id_members_filter_get) | **GET** /organizations/{id}/members/{filter} | 
[**organizations_id_members_get**](DefaultApi.md#organizations_id_members_get) | **GET** /organizations/{id}/members | List the members in a team
[**organizations_id_members_id_member_all_delete**](DefaultApi.md#organizations_id_members_id_member_all_delete) | **DELETE** /organizations/{id}/members/{idMember}/all | Remove a member from a team and from all team boards
[**organizations_id_members_id_member_deactivated_put**](DefaultApi.md#organizations_id_members_id_member_deactivated_put) | **PUT** /organizations/{id}/members/{idMember}/deactivated | Deactivate or reactivate a member of a team
[**organizations_id_members_id_member_delete**](DefaultApi.md#organizations_id_members_id_member_delete) | **DELETE** /organizations/{id}/members/{idMember} | Remove a member from a team
[**organizations_id_members_id_member_put**](DefaultApi.md#organizations_id_members_id_member_put) | **PUT** /organizations/{id}/members/{idMember} | Add a member to a team or update their member type.
[**organizations_id_members_invited_get**](DefaultApi.md#organizations_id_members_invited_get) | **GET** /organizations/{id}/membersInvited | List the members with pending invites to a team
[**organizations_id_members_put**](DefaultApi.md#organizations_id_members_put) | **PUT** /organizations/{id}/members | 
[**organizations_id_memberships_get**](DefaultApi.md#organizations_id_memberships_get) | **GET** /organizations/{id}/memberships | List the memberships of a team
[**organizations_id_memberships_id_membership_get**](DefaultApi.md#organizations_id_memberships_id_membership_get) | **GET** /organizations/{id}/memberships/{idMembership} | List the memberships of a team
[**organizations_id_new_billable_guests_id_board_get**](DefaultApi.md#organizations_id_new_billable_guests_id_board_get) | **GET** /organizations/{id}/newBillableGuests/{idBoard} | Used to check whether the given board has new billable guests on it.
[**organizations_id_plugin_data_get**](DefaultApi.md#organizations_id_plugin_data_get) | **GET** /organizations/{id}/pluginData | Get organization scoped pluginData on this team
[**organizations_id_prefs_associated_domain_delete**](DefaultApi.md#organizations_id_prefs_associated_domain_delete) | **DELETE** /organizations/{id}/prefs/associatedDomain | Remove the associated Google Apps domain from a team
[**organizations_id_prefs_org_invite_restrict_delete**](DefaultApi.md#organizations_id_prefs_org_invite_restrict_delete) | **DELETE** /organizations/{id}/prefs/orgInviteRestrict | Remove the email domain restriction on who can be invited to the team
[**organizations_id_put**](DefaultApi.md#organizations_id_put) | **PUT** /organizations/{id} | Update an organization
[**organizations_id_tags_get**](DefaultApi.md#organizations_id_tags_get) | **GET** /organizations/{id}/tags | List the organization&#39;s collections
[**organizations_id_tags_id_tag_delete**](DefaultApi.md#organizations_id_tags_id_tag_delete) | **DELETE** /organizations/{id}/tags/{idTag} | Delete an organization&#39;s tag
[**organizations_id_tags_post**](DefaultApi.md#organizations_id_tags_post) | **POST** /organizations/{id}/tags | Create a new collection in a team
[**organizations_post**](DefaultApi.md#organizations_post) | **POST** /organizations | Create a new team
[**search_get**](DefaultApi.md#search_get) | **GET** /search | Find what you&#39;re looking for in Trello
[**search_members_get**](DefaultApi.md#search_members_get) | **GET** /search/members | Search for Trello members
[**tokens_token_delete**](DefaultApi.md#tokens_token_delete) | **DELETE** /tokens/{token} | Delete a token.
[**tokens_token_get**](DefaultApi.md#tokens_token_get) | **GET** /tokens/{token} | Retrieve information about a token.
[**tokens_token_member_get**](DefaultApi.md#tokens_token_member_get) | **GET** /tokens/{token}/member | Retrieve information about a token&#39;s owner by token.
[**tokens_token_webhooks_get**](DefaultApi.md#tokens_token_webhooks_get) | **GET** /tokens/{token}/webhooks | Retrieve all webhooks created with a token.
[**tokens_token_webhooks_id_webhook_delete**](DefaultApi.md#tokens_token_webhooks_id_webhook_delete) | **DELETE** /tokens/{token}/webhooks/{idWebhook} | Delete a webhook created with given token.
[**tokens_token_webhooks_id_webhook_get**](DefaultApi.md#tokens_token_webhooks_id_webhook_get) | **GET** /tokens/{token}/webhooks/{idWebhook} | Retrieve a webhook created with a token.
[**tokens_token_webhooks_post**](DefaultApi.md#tokens_token_webhooks_post) | **POST** /tokens/{token}/webhooks | Create a new webhook for a token.
[**tokens_token_webhooks_webhook_id_put**](DefaultApi.md#tokens_token_webhooks_webhook_id_put) | **PUT** /tokens/{token}/webhooks/{webhookId} | Update an existing webhook.
[**webhooks_id_delete**](DefaultApi.md#webhooks_id_delete) | **DELETE** /webhooks/{id} | Delete a webhook by ID.
[**webhooks_id_field_get**](DefaultApi.md#webhooks_id_field_get) | **GET** /webhooks/{id}/{field} | Get a webhook&#39;s field.
[**webhooks_id_get**](DefaultApi.md#webhooks_id_get) | **GET** /webhooks/{id} | Get a webhook by ID.
[**webhooks_id_put**](DefaultApi.md#webhooks_id_put) | **PUT** /webhooks/{id} | Update a webhook by ID.
[**webhooks_post**](DefaultApi.md#webhooks_post) | **POST** /webhooks | Create a new webhook.


# **actions_id_action_reactions_get**
> actions_id_action_reactions_get(id_action, member=member, emoji=emoji)

List reactions for an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_action = 'id_action_example' # str | The ID of the action
member = 'member_example' # str | Whether to load the member as a nested resource. See Members Nested Resource (optional)
emoji = 'emoji_example' # str | Whether to load the emoji as a nested resource. (optional)

try:
    # List reactions for an action
    api_instance.actions_id_action_reactions_get(id_action, member=member, emoji=emoji)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_action_reactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | **str**| The ID of the action | 
 **member** | **str**| Whether to load the member as a nested resource. See Members Nested Resource | [optional] 
 **emoji** | **str**| Whether to load the emoji as a nested resource. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_action_reactions_id_delete**
> actions_id_action_reactions_id_delete(id_action, id)

Deletes a reaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_action = 'id_action_example' # str | The ID of the action
id = 'id_example' # str | The ID of the reaction

try:
    # Deletes a reaction
    api_instance.actions_id_action_reactions_id_delete(id_action, id)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_action_reactions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | **str**| The ID of the action | 
 **id** | **str**| The ID of the reaction | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_action_reactions_id_get**
> actions_id_action_reactions_id_get(id_action, id, member=member, emoji=emoji)

Get information for a reaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_action = 'id_action_example' # str | The ID of the action
id = 'id_example' # str | The ID of the reaction
member = 'member_example' # str | Whether to load the member as a nested resource. See Members Nested Resource (optional)
emoji = 'emoji_example' # str | Whether to load the emoji as a nested resource. (optional)

try:
    # Get information for a reaction
    api_instance.actions_id_action_reactions_id_get(id_action, id, member=member, emoji=emoji)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_action_reactions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | **str**| The ID of the action | 
 **id** | **str**| The ID of the reaction | 
 **member** | **str**| Whether to load the member as a nested resource. See Members Nested Resource | [optional] 
 **emoji** | **str**| Whether to load the emoji as a nested resource. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_action_reactions_post**
> actions_id_action_reactions_post(id_action)

Adds a new reaction to an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_action = 'id_action_example' # str | The ID of the action

try:
    # Adds a new reaction to an action
    api_instance.actions_id_action_reactions_post(id_action)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_action_reactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | **str**| The ID of the action | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_action_reactions_summary_get**
> actions_id_action_reactions_summary_get(id_action)

List a summary of all reactions for an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_action = 'id_action_example' # str | The ID of the action

try:
    # List a summary of all reactions for an action
    api_instance.actions_id_action_reactions_summary_get(id_action)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_action_reactions_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | **str**| The ID of the action | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_board_get**
> actions_id_board_get(id, fields=fields)

Get the board for an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
fields = 'fields_example' # str | all or a comma-separated list of board fields (optional)

try:
    # Get the board for an action
    api_instance.actions_id_board_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_board_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **fields** | **str**| all or a comma-separated list of board fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_card_get**
> actions_id_card_get(id, fields=fields)

Get the card for an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
fields = 'fields_example' # str | all or a comma-separated list of card fields (optional)

try:
    # Get the card for an action
    api_instance.actions_id_card_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_card_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **fields** | **str**| all or a comma-separated list of card fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_delete**
> actions_id_delete(id)

Delete a comment action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the commentCard action to delete

try:
    # Delete a comment action
    api_instance.actions_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the commentCard action to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_display_get**
> actions_id_display_get(id)

Get the display information for an action.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action

try:
    # Get the display information for an action.
    api_instance.actions_id_display_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_display_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_field_get**
> actions_id_field_get(id, field)

Get a specific property of an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
field = 'field_example' # str | An action field

try:
    # Get a specific property of an action
    api_instance.actions_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **field** | **str**| An action field | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_get**
> actions_id_get(id, display=display, entities=entities, fields=fields, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields)

Get information about an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
display = 'display_example' # str |  (optional)
entities = 'entities_example' # str |  (optional)
fields = 'fields_example' # str | all or a comma-separated list of action fields (optional)
member = 'member_example' # str |  (optional)
member_fields = 'member_fields_example' # str | all or a comma-separated list of member fields (optional)
member_creator = 'member_creator_example' # str | Whether to include the member object for the creator of the action (optional)
member_creator_fields = 'member_creator_fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Get information about an action
    api_instance.actions_id_get(id, display=display, entities=entities, fields=fields, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **display** | **str**|  | [optional] 
 **entities** | **str**|  | [optional] 
 **fields** | **str**| all or a comma-separated list of action fields | [optional] 
 **member** | **str**|  | [optional] 
 **member_fields** | **str**| all or a comma-separated list of member fields | [optional] 
 **member_creator** | **str**| Whether to include the member object for the creator of the action | [optional] 
 **member_creator_fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_list_get**
> actions_id_list_get(id, fields=fields)

Get the list for an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
fields = 'fields_example' # str | all or a comma-separated list of list fields (optional)

try:
    # Get the list for an action
    api_instance.actions_id_list_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **fields** | **str**| all or a comma-separated list of list fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_member_creator_get**
> actions_id_member_creator_get(id, fields=fields)

Gets the member who created the action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Gets the member who created the action
    api_instance.actions_id_member_creator_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_member_creator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_member_get**
> actions_id_member_get(id, fields=fields)

Gets the member of an action (not the creator)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Gets the member of an action (not the creator)
    api_instance.actions_id_member_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_organization_get**
> actions_id_organization_get(id, fields=fields)

Get the organization of an action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action
fields = 'fields_example' # str | all or a comma-separated list of organization fields (optional)

try:
    # Get the organization of an action
    api_instance.actions_id_organization_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action | 
 **fields** | **str**| all or a comma-separated list of organization fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_put**
> actions_id_put(id, text)

Update a comment action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action to update
text = 'text_example' # str | The new text for the comment

try:
    # Update a comment action
    api_instance.actions_id_put(id, text)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action to update | 
 **text** | **str**| The new text for the comment | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_id_text_put**
> actions_id_text_put(id, value)

Update a comment action

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the action to update
value = 'value_example' # str | The new text for the comment

try:
    # Update a comment action
    api_instance.actions_id_text_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->actions_id_text_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the action to update | 
 **value** | **str**| The new text for the comment | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_get**
> batch_get(urls)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
urls = 'urls_example' # str | A list of API routes. Maximum of 10 routes allowed. The routes should begin with a forward slash and should not include the API version number - e.g. \"urls=/members/trello,/cards/[cardId]\"

try:
    api_instance.batch_get(urls)
except ApiException as e:
    print("Exception when calling DefaultApi->batch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urls** | **str**| A list of API routes. Maximum of 10 routes allowed. The routes should begin with a forward slash and should not include the API version number - e.g. \&quot;urls&#x3D;/members/trello,/cards/[cardId]\&quot; | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_actions_get**
> boards_id_actions_get(board_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
board_id = 'board_id_example' # str | 

try:
    api_instance.boards_id_actions_get(board_id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_board_plugins_get**
> boards_id_board_plugins_get(id)

Get the enabled Power-Ups on a board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board

try:
    # Get the enabled Power-Ups on a board
    api_instance.boards_id_board_plugins_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_board_plugins_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_board_plugins_id_plugin_delete**
> boards_id_board_plugins_id_plugin_delete(id, id_plugin)

Disable a Power-Up on a board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
id_plugin = 'id_plugin_example' # str | The ID of the Power-Up to disable

try:
    # Disable a Power-Up on a board
    api_instance.boards_id_board_plugins_id_plugin_delete(id, id_plugin)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_board_plugins_id_plugin_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **id_plugin** | **str**| The ID of the Power-Up to disable | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_board_plugins_post**
> boards_id_board_plugins_post(id, id_plugin=id_plugin)

Enable a Power-Up on a board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
id_plugin = 'id_plugin_example' # str | The ID of the Power-Up to enable (optional)

try:
    # Enable a Power-Up on a board
    api_instance.boards_id_board_plugins_post(id, id_plugin=id_plugin)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_board_plugins_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **id_plugin** | **str**| The ID of the Power-Up to enable | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_board_stars_get**
> boards_id_board_stars_get(board_id, filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
board_id = 'board_id_example' # str | 
filter = 'filter_example' # str | Valid values: mine, none

try:
    api_instance.boards_id_board_stars_get(board_id, filter)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_board_stars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**|  | 
 **filter** | **str**| Valid values: mine, none | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_calendar_key_generate_post**
> boards_id_calendar_key_generate_post(id)

Create a new board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update

try:
    # Create a new board.
    api_instance.boards_id_calendar_key_generate_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_calendar_key_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_cards_card_id_get**
> boards_id_cards_card_id_get(id, id_card)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
id_card = 'id_card_example' # str | The id the card to retrieve.

try:
    api_instance.boards_id_cards_card_id_get(id, id_card)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_cards_card_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **id_card** | **str**| The id the card to retrieve. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_cards_filter_get**
> boards_id_cards_filter_get(board_id, filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
board_id = 'board_id_example' # str | 
filter = 'filter_example' # str | Valid Values: all, closed, none, open, visible.

try:
    api_instance.boards_id_cards_filter_get(board_id, filter)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_cards_filter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**|  | 
 **filter** | **str**| Valid Values: all, closed, none, open, visible. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_cards_get**
> boards_id_cards_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.boards_id_cards_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_cards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_checklists_get**
> boards_id_checklists_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board

try:
    api_instance.boards_id_checklists_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_checklists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_checklists_post**
> boards_id_checklists_post(id)

Create a new checklist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update

try:
    # Create a new checklist.
    api_instance.boards_id_checklists_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_checklists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_custom_fields_get**
> boards_id_custom_fields_get(id)

Get the Custom Field Definitions that exist on a board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board

try:
    # Get the Custom Field Definitions that exist on a board.
    api_instance.boards_id_custom_fields_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_custom_fields_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_delete**
> boards_id_delete(id)

Delete a board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to delete

try:
    # Delete a board.
    api_instance.boards_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_email_key_generate_post**
> boards_id_email_key_generate_post(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update

try:
    api_instance.boards_id_email_key_generate_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_email_key_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_field_get**
> boards_id_field_get(id, field)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board.
field = 'field_example' # str | The field you'd like to receive. Valid values: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url.

try:
    api_instance.boards_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board. | 
 **field** | **str**| The field you&#39;d like to receive. Valid values: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_get**
> boards_id_get(id, actions=actions, board_stars=board_stars, cards=cards, card_plugin_data=card_plugin_data, checklists=checklists, custom_fields=custom_fields, fields=fields, labels=labels, lists=lists, members=members, memberships=memberships, members_invited=members_invited, members_invited_fields=members_invited_fields, plugin_data=plugin_data, organization=organization, organization_plugin_data=organization_plugin_data, my_prefs=my_prefs, tags=tags)

Request a single board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
actions = 'actions_example' # str | This is a nested resource. Read more about actions as nested resources here. (optional)
board_stars = 'board_stars_example' # str | Valid values are one of: mine or none. (optional)
cards = 'cards_example' # str | This is a nested resource. Read more about cards as nested resources here. (optional)
card_plugin_data = 'card_plugin_data_example' # str | Use with the cards param to include card pluginData with the response (optional)
checklists = 'checklists_example' # str | This is a nested resource. Read more about checklists as nested resources here. (optional)
custom_fields = 'custom_fields_example' # str | This is a nested resource. Read more about custom fields as nested resources here. (optional)
fields = 'fields_example' # str | The fields of the board to be included in the response. Valid values: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url (optional)
labels = 'labels_example' # str | This is a nested resource. Read more about labels as nested resources here. (optional)
lists = 'lists_example' # str | This is a nested resource. Read more about lists as nested resources here. (optional)
members = 'members_example' # str | This is a nested resource. Read more about members as nested resources here. (optional)
memberships = 'memberships_example' # str | This is a nested resource. Read more about memberships as nested resources here. (optional)
members_invited = 'members_invited_example' # str | Returns a list of member objects representing members who been invited to be a member of the board. One of: admins, all, none, normal, owners (optional)
members_invited_fields = 'members_invited_fields_example' # str | The member fields to be included in the membersInvited response. Valid values: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username (optional)
plugin_data = 'plugin_data_example' # str | Determines whether the pluginData for this board should be returned. Valid values: true or false. (optional)
organization = 'organization_example' # str | This is a nested resource. Read more about organizations as nested resources here. (optional)
organization_plugin_data = 'organization_plugin_data_example' # str | Use with the organization param to include organization pluginData with the response (optional)
my_prefs = 'my_prefs_example' # str |  (optional)
tags = 'tags_example' # str | Also known as collections, tags, refer to the collection(s) that a Board belongs to. (optional)

try:
    # Request a single board.
    api_instance.boards_id_get(id, actions=actions, board_stars=board_stars, cards=cards, card_plugin_data=card_plugin_data, checklists=checklists, custom_fields=custom_fields, fields=fields, labels=labels, lists=lists, members=members, memberships=memberships, members_invited=members_invited, members_invited_fields=members_invited_fields, plugin_data=plugin_data, organization=organization, organization_plugin_data=organization_plugin_data, my_prefs=my_prefs, tags=tags)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **actions** | **str**| This is a nested resource. Read more about actions as nested resources here. | [optional] 
 **board_stars** | **str**| Valid values are one of: mine or none. | [optional] 
 **cards** | **str**| This is a nested resource. Read more about cards as nested resources here. | [optional] 
 **card_plugin_data** | **str**| Use with the cards param to include card pluginData with the response | [optional] 
 **checklists** | **str**| This is a nested resource. Read more about checklists as nested resources here. | [optional] 
 **custom_fields** | **str**| This is a nested resource. Read more about custom fields as nested resources here. | [optional] 
 **fields** | **str**| The fields of the board to be included in the response. Valid values: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url | [optional] 
 **labels** | **str**| This is a nested resource. Read more about labels as nested resources here. | [optional] 
 **lists** | **str**| This is a nested resource. Read more about lists as nested resources here. | [optional] 
 **members** | **str**| This is a nested resource. Read more about members as nested resources here. | [optional] 
 **memberships** | **str**| This is a nested resource. Read more about memberships as nested resources here. | [optional] 
 **members_invited** | **str**| Returns a list of member objects representing members who been invited to be a member of the board. One of: admins, all, none, normal, owners | [optional] 
 **members_invited_fields** | **str**| The member fields to be included in the membersInvited response. Valid values: all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username | [optional] 
 **plugin_data** | **str**| Determines whether the pluginData for this board should be returned. Valid values: true or false. | [optional] 
 **organization** | **str**| This is a nested resource. Read more about organizations as nested resources here. | [optional] 
 **organization_plugin_data** | **str**| Use with the organization param to include organization pluginData with the response | [optional] 
 **my_prefs** | **str**|  | [optional] 
 **tags** | **str**| Also known as collections, tags, refer to the collection(s) that a Board belongs to. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_id_tags_post**
> boards_id_id_tags_post(id, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | The id of a tag from the organization to which this board belongs.

try:
    api_instance.boards_id_id_tags_post(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_id_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| The id of a tag from the organization to which this board belongs. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_labels_get**
> boards_id_labels_get(id, fields=fields, limit=limit)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
fields = 'fields_example' # str | all or a comma-separated list of label fields (optional)
limit = 'limit_example' # str | 0 to 1000 (optional)

try:
    api_instance.boards_id_labels_get(id, fields=fields, limit=limit)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **fields** | **str**| all or a comma-separated list of label fields | [optional] 
 **limit** | **str**| 0 to 1000 | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_labels_post**
> boards_id_labels_post(id, name, color)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
name = 'name_example' # str | The name of the label to be created. 1 to 16384 characters long.
color = 'color_example' # str | Sets the color of the new label. Valid values are a label color or null.

try:
    api_instance.boards_id_labels_post(id, name, color)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **name** | **str**| The name of the label to be created. 1 to 16384 characters long. | 
 **color** | **str**| Sets the color of the new label. Valid values are a label color or null. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_lists_filter_get**
> boards_id_lists_filter_get(id, filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
filter = 'filter_example' # str | One of all, closed, none, open

try:
    api_instance.boards_id_lists_filter_get(id, filter)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_lists_filter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **filter** | **str**| One of all, closed, none, open | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_lists_get**
> boards_id_lists_get(id, cards=cards, card_fields=card_fields, filter=filter, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
cards = 'cards_example' # str | One of: all, closed, none, open (optional)
card_fields = 'card_fields_example' # str | all or a comma-separated list of card fields (optional)
filter = 'filter_example' # str | One of all, closed, none, open (optional)
fields = 'fields_example' # str | all or a comma-separated list of list fields (optional)

try:
    api_instance.boards_id_lists_get(id, cards=cards, card_fields=card_fields, filter=filter, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_lists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **cards** | **str**| One of: all, closed, none, open | [optional] 
 **card_fields** | **str**| all or a comma-separated list of card fields | [optional] 
 **filter** | **str**| One of all, closed, none, open | [optional] 
 **fields** | **str**| all or a comma-separated list of list fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_lists_post**
> boards_id_lists_post(id, name, pos=pos)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
name = 'name_example' # str | The name of the list to be created. 1 to 16384 characters long.
pos = 'pos_example' # str | Determines the position of the list. Valid values: top, bottom, or a positive number. (optional)

try:
    api_instance.boards_id_lists_post(id, name, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_lists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **name** | **str**| The name of the list to be created. 1 to 16384 characters long. | 
 **pos** | **str**| Determines the position of the list. Valid values: top, bottom, or a positive number. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_marked_as_viewed_post**
> boards_id_marked_as_viewed_post(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update

try:
    api_instance.boards_id_marked_as_viewed_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_marked_as_viewed_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_members_get**
> boards_id_members_get(id)

Get the members for a board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board

try:
    # Get the members for a board
    api_instance.boards_id_members_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_members_id_member_delete**
> boards_id_members_id_member_delete(id, id_member)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
id_member = 'id_member_example' # str | The id, username, or organization name of the user to be removed from the board.

try:
    api_instance.boards_id_members_id_member_delete(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_members_id_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **id_member** | **str**| The id, username, or organization name of the user to be removed from the board. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_members_id_member_put**
> boards_id_members_id_member_put(id, id_member, type)

Add a member to the board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
id_member = 'id_member_example' # str | The id of the member to add to the board.
type = 'type_example' # str | One of: admin, normal, observer. Determines the type of member this user will be on the board.

try:
    # Add a member to the board.
    api_instance.boards_id_members_id_member_put(id, id_member, type)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_members_id_member_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **id_member** | **str**| The id of the member to add to the board. | 
 **type** | **str**| One of: admin, normal, observer. Determines the type of member this user will be on the board. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_members_put**
> boards_id_members_put(id, email)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
email = 'email_example' # str | The email address of a user to add as a member of the board.

try:
    # Update an existing board by id
    api_instance.boards_id_members_put(id, email)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_members_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **email** | **str**| The email address of a user to add as a member of the board. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_memberships_get**
> boards_id_memberships_get(id, filter=filter, activity=activity, org_member_type=org_member_type, member=member, member_fields=member_fields)

Get information about the memberships users have to the board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
filter = 'filter_example' # str | One of admins, all, none, normal (optional)
activity = 'activity_example' # str | Works for premium organizations only. (optional)
org_member_type = 'org_member_type_example' # str | Shows the type of member to the org the user is. For instance, an org admin will have a orgMemberType of admin. (optional)
member = 'member_example' # str | Determines whether to include a nester member object. (optional)
member_fields = 'member_fields_example' # str | Fields to show if member=true. Valid values: nested member resource fields. (optional)

try:
    # Get information about the memberships users have to the board.
    api_instance.boards_id_memberships_get(id, filter=filter, activity=activity, org_member_type=org_member_type, member=member, member_fields=member_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_memberships_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **filter** | **str**| One of admins, all, none, normal | [optional] 
 **activity** | **str**| Works for premium organizations only. | [optional] 
 **org_member_type** | **str**| Shows the type of member to the org the user is. For instance, an org admin will have a orgMemberType of admin. | [optional] 
 **member** | **str**| Determines whether to include a nester member object. | [optional] 
 **member_fields** | **str**| Fields to show if member&#x3D;true. Valid values: nested member resource fields. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_memberships_id_membership_put**
> boards_id_memberships_id_membership_put(id, id_membership, type, member_fields=member_fields)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
id_membership = 'id_membership_example' # str | The id of a membership that should be added to this board.
type = 'type_example' # str | One of: admin, normal, observer. Determines the type of member that this membership will be to this board.
member_fields = 'member_fields_example' # str | Valid values: all, avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username (optional)

try:
    # Update an existing board by id
    api_instance.boards_id_memberships_id_membership_put(id, id_membership, type, member_fields=member_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_memberships_id_membership_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **id_membership** | **str**| The id of a membership that should be added to this board. | 
 **type** | **str**| One of: admin, normal, observer. Determines the type of member that this membership will be to this board. | 
 **member_fields** | **str**| Valid values: all, avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_my_prefs_email_position_put**
> boards_id_my_prefs_email_position_put(id, value)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | Valid values: bottom, top. Determines the position of the email address.

try:
    # Update an existing board by id
    api_instance.boards_id_my_prefs_email_position_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_my_prefs_email_position_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| Valid values: bottom, top. Determines the position of the email address. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_my_prefs_id_email_list_put**
> boards_id_my_prefs_id_email_list_put(id, value)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | The id of an email list.

try:
    # Update an existing board by id
    api_instance.boards_id_my_prefs_id_email_list_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_my_prefs_id_email_list_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| The id of an email list. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_my_prefs_show_list_guide_put**
> boards_id_my_prefs_show_list_guide_put(id, value)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | Determines whether to show the list guide.

try:
    # Update an existing board by id
    api_instance.boards_id_my_prefs_show_list_guide_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_my_prefs_show_list_guide_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| Determines whether to show the list guide. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_my_prefs_show_sidebar_activity_put**
> boards_id_my_prefs_show_sidebar_activity_put(id, value)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | Determines whether to show sidebar activity.

try:
    # Update an existing board by id
    api_instance.boards_id_my_prefs_show_sidebar_activity_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_my_prefs_show_sidebar_activity_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| Determines whether to show sidebar activity. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_my_prefs_show_sidebar_board_actions_put**
> boards_id_my_prefs_show_sidebar_board_actions_put(id, value)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | Determines whether to show the sidebar board actions.

try:
    # Update an existing board by id
    api_instance.boards_id_my_prefs_show_sidebar_board_actions_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_my_prefs_show_sidebar_board_actions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| Determines whether to show the sidebar board actions. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_my_prefs_show_sidebar_members_put**
> boards_id_my_prefs_show_sidebar_members_put(id, value)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | Determines whether to show members of the board in the sidebar.

try:
    # Update an existing board by id
    api_instance.boards_id_my_prefs_show_sidebar_members_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_my_prefs_show_sidebar_members_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| Determines whether to show members of the board in the sidebar. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_my_prefs_show_sidebar_put**
> boards_id_my_prefs_show_sidebar_put(id, value)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | Determines whether to show the side bar.

try:
    # Update an existing board by id
    api_instance.boards_id_my_prefs_show_sidebar_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_my_prefs_show_sidebar_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| Determines whether to show the side bar. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_plugins_get**
> boards_id_plugins_get(id, filter=filter)

List the Power-Ups for a board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
filter = 'filter_example' # str | One of: enabled or available (optional)

try:
    # List the Power-Ups for a board
    api_instance.boards_id_plugins_get(id, filter=filter)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_plugins_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **filter** | **str**| One of: enabled or available | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_power_ups_post**
> boards_id_power_ups_post(id, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
value = 'value_example' # str | The Power-Up to be enabled on the board. One of: calendar, cardAging, recap, voting.

try:
    api_instance.boards_id_power_ups_post(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_power_ups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **value** | **str**| The Power-Up to be enabled on the board. One of: calendar, cardAging, recap, voting. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_power_ups_power_up_delete**
> boards_id_power_ups_power_up_delete(id, power_up)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
power_up = 'power_up_example' # str | The Power-Up to be enabled on the board. One of: calendar, cardAging, recap, voting.

try:
    api_instance.boards_id_power_ups_power_up_delete(id, power_up)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_power_ups_power_up_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **power_up** | **str**| The Power-Up to be enabled on the board. One of: calendar, cardAging, recap, voting. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_put**
> boards_id_put(id, name=name, desc=desc, closed=closed, subscribed=subscribed, id_organization=id_organization, prefspermission_level=prefspermission_level, prefsself_join=prefsself_join, prefscard_covers=prefscard_covers, prefsinvitations=prefsinvitations, prefsvoting=prefsvoting, prefscomments=prefscomments, prefsbackground=prefsbackground, prefscard_aging=prefscard_aging, prefscalendar_feed_enabled=prefscalendar_feed_enabled, label_namesgreen=label_namesgreen, label_namesyellow=label_namesyellow, label_namesorange=label_namesorange, label_namesred=label_namesred, label_namespurple=label_namespurple, label_namesblue=label_namesblue)

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
name = 'name_example' # str | The new name for the board. 1 to 16384 characters long. (optional)
desc = 'desc_example' # str | A new description for the board, 0 to 16384 characters long (optional)
closed = 'closed_example' # str | Whether the board is closed (optional)
subscribed = 'subscribed_example' # str | Whether the acting user is subscribed to the board (optional)
id_organization = 'id_organization_example' # str | The id of the team the board should be moved to (optional)
prefspermission_level = 'prefspermission_level_example' # str | One of: org, private, public (optional)
prefsself_join = 'prefsself_join_example' # str | Whether team members can join the board themselves (optional)
prefscard_covers = 'prefscard_covers_example' # str | Whether card covers should be displayed on this board (optional)
prefsinvitations = 'prefsinvitations_example' # str | Who can invite people to this board. One of: admins, members (optional)
prefsvoting = 'prefsvoting_example' # str | Who can vote on this board. One of disabled, members, observers, org, public (optional)
prefscomments = 'prefscomments_example' # str | Who can comment on cards on this board. One of: disabled, members, observers, org, public (optional)
prefsbackground = 'prefsbackground_example' # str | The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey (optional)
prefscard_aging = 'prefscard_aging_example' # str | One of: pirate, regular (optional)
prefscalendar_feed_enabled = 'prefscalendar_feed_enabled_example' # str | Determines whether the calendar feed is enabled or not. (optional)
label_namesgreen = 'label_namesgreen_example' # str | Name for the green label. 1 to 16384 characters long (optional)
label_namesyellow = 'label_namesyellow_example' # str | Name for the yellow label. 1 to 16384 characters long (optional)
label_namesorange = 'label_namesorange_example' # str | Name for the orange label. 1 to 16384 characters long (optional)
label_namesred = 'label_namesred_example' # str | Name for the red label. 1 to 16384 characters long (optional)
label_namespurple = 'label_namespurple_example' # str | Name for the purple label. 1 to 16384 characters long (optional)
label_namesblue = 'label_namesblue_example' # str | Name for the blue label. 1 to 16384 characters long (optional)

try:
    # Update an existing board by id
    api_instance.boards_id_put(id, name=name, desc=desc, closed=closed, subscribed=subscribed, id_organization=id_organization, prefspermission_level=prefspermission_level, prefsself_join=prefsself_join, prefscard_covers=prefscard_covers, prefsinvitations=prefsinvitations, prefsvoting=prefsvoting, prefscomments=prefscomments, prefsbackground=prefsbackground, prefscard_aging=prefscard_aging, prefscalendar_feed_enabled=prefscalendar_feed_enabled, label_namesgreen=label_namesgreen, label_namesyellow=label_namesyellow, label_namesorange=label_namesorange, label_namesred=label_namesred, label_namespurple=label_namespurple, label_namesblue=label_namesblue)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **name** | **str**| The new name for the board. 1 to 16384 characters long. | [optional] 
 **desc** | **str**| A new description for the board, 0 to 16384 characters long | [optional] 
 **closed** | **str**| Whether the board is closed | [optional] 
 **subscribed** | **str**| Whether the acting user is subscribed to the board | [optional] 
 **id_organization** | **str**| The id of the team the board should be moved to | [optional] 
 **prefspermission_level** | **str**| One of: org, private, public | [optional] 
 **prefsself_join** | **str**| Whether team members can join the board themselves | [optional] 
 **prefscard_covers** | **str**| Whether card covers should be displayed on this board | [optional] 
 **prefsinvitations** | **str**| Who can invite people to this board. One of: admins, members | [optional] 
 **prefsvoting** | **str**| Who can vote on this board. One of disabled, members, observers, org, public | [optional] 
 **prefscomments** | **str**| Who can comment on cards on this board. One of: disabled, members, observers, org, public | [optional] 
 **prefsbackground** | **str**| The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey | [optional] 
 **prefscard_aging** | **str**| One of: pirate, regular | [optional] 
 **prefscalendar_feed_enabled** | **str**| Determines whether the calendar feed is enabled or not. | [optional] 
 **label_namesgreen** | **str**| Name for the green label. 1 to 16384 characters long | [optional] 
 **label_namesyellow** | **str**| Name for the yellow label. 1 to 16384 characters long | [optional] 
 **label_namesorange** | **str**| Name for the orange label. 1 to 16384 characters long | [optional] 
 **label_namesred** | **str**| Name for the red label. 1 to 16384 characters long | [optional] 
 **label_namespurple** | **str**| Name for the purple label. 1 to 16384 characters long | [optional] 
 **label_namesblue** | **str**| Name for the blue label. 1 to 16384 characters long | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_tags_get**
> boards_id_tags_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board

try:
    api_instance.boards_id_tags_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_post**
> boards_post(name, default_labels=default_labels, default_lists=default_lists, desc=desc, id_organization=id_organization, id_board_source=id_board_source, keep_from_source=keep_from_source, power_ups=power_ups, prefs_permission_level=prefs_permission_level, prefs_voting=prefs_voting, prefs_comments=prefs_comments, prefs_invitations=prefs_invitations, prefs_self_join=prefs_self_join, prefs_card_covers=prefs_card_covers, prefs_background=prefs_background, prefs_card_aging=prefs_card_aging)

Create a new board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The new name for the board. 1 to 16384 characters long.
default_labels = 'default_labels_example' # str | Determines whether to use the default set of labels. (optional)
default_lists = 'default_lists_example' # str | Determines whether to add the default set of lists to a board (To Do, Doing, Done). It is ignored if idBoardSource is provided. (optional)
desc = 'desc_example' # str | A new description for the board, 0 to 16384 characters long (optional)
id_organization = 'id_organization_example' # str | The id or name of the team the board should belong to. (optional)
id_board_source = 'id_board_source_example' # str | The id of a board to copy into the new board. (optional)
keep_from_source = 'keep_from_source_example' # str | To keep cards from the original board pass in the value cards (optional)
power_ups = 'power_ups_example' # str | The Power-Ups that should be enabled on the new board. One of: all, calendar, cardAging, recap, voting. (optional)
prefs_permission_level = 'prefs_permission_level_example' # str | The permissions level of the board. One of: org, private, public. (optional)
prefs_voting = 'prefs_voting_example' # str | Who can vote on this board. One of disabled, members, observers, org, public. (optional)
prefs_comments = 'prefs_comments_example' # str | Who can comment on cards on this board. One of: disabled, members, observers, org, public. (optional)
prefs_invitations = 'prefs_invitations_example' # str | Determines what types of members can invite users to join. One of: admins, members. (optional)
prefs_self_join = 'prefs_self_join_example' # str | Determines whether users can join the boards themselves or whether they have to be invited. (optional)
prefs_card_covers = 'prefs_card_covers_example' # str | Determines whether card covers are enabled. (optional)
prefs_background = 'prefs_background_example' # str | The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey. (optional)
prefs_card_aging = 'prefs_card_aging_example' # str | Determines the type of card aging that should take place on the board if card aging is enabled. One of: pirate, regular. (optional)

try:
    # Create a new board.
    api_instance.boards_post(name, default_labels=default_labels, default_lists=default_lists, desc=desc, id_organization=id_organization, id_board_source=id_board_source, keep_from_source=keep_from_source, power_ups=power_ups, prefs_permission_level=prefs_permission_level, prefs_voting=prefs_voting, prefs_comments=prefs_comments, prefs_invitations=prefs_invitations, prefs_self_join=prefs_self_join, prefs_card_covers=prefs_card_covers, prefs_background=prefs_background, prefs_card_aging=prefs_card_aging)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new name for the board. 1 to 16384 characters long. | 
 **default_labels** | **str**| Determines whether to use the default set of labels. | [optional] 
 **default_lists** | **str**| Determines whether to add the default set of lists to a board (To Do, Doing, Done). It is ignored if idBoardSource is provided. | [optional] 
 **desc** | **str**| A new description for the board, 0 to 16384 characters long | [optional] 
 **id_organization** | **str**| The id or name of the team the board should belong to. | [optional] 
 **id_board_source** | **str**| The id of a board to copy into the new board. | [optional] 
 **keep_from_source** | **str**| To keep cards from the original board pass in the value cards | [optional] 
 **power_ups** | **str**| The Power-Ups that should be enabled on the new board. One of: all, calendar, cardAging, recap, voting. | [optional] 
 **prefs_permission_level** | **str**| The permissions level of the board. One of: org, private, public. | [optional] 
 **prefs_voting** | **str**| Who can vote on this board. One of disabled, members, observers, org, public. | [optional] 
 **prefs_comments** | **str**| Who can comment on cards on this board. One of: disabled, members, observers, org, public. | [optional] 
 **prefs_invitations** | **str**| Determines what types of members can invite users to join. One of: admins, members. | [optional] 
 **prefs_self_join** | **str**| Determines whether users can join the boards themselves or whether they have to be invited. | [optional] 
 **prefs_card_covers** | **str**| Determines whether card covers are enabled. | [optional] 
 **prefs_background** | **str**| The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey. | [optional] 
 **prefs_card_aging** | **str**| Determines the type of card aging that should take place on the board if card aging is enabled. One of: pirate, regular. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **card_id_card_custom_field_id_custom_field_item_put**
> card_id_card_custom_field_id_custom_field_item_put(id_card, id_custom_field, value)

Setting, updating, and removing the value for a Custom Field on a card.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_card = 'id_card_example' # str | ID of the card that the Custom Field value should be set/updated for
id_custom_field = 'id_custom_field_example' # str | ID of the Custom Field on the card.
value = 'value_example' # str | An object containing the key and value to set for the card's Custom Field value. The key used to set the value should match the type of Custom Field defined.

try:
    # Setting, updating, and removing the value for a Custom Field on a card.
    api_instance.card_id_card_custom_field_id_custom_field_item_put(id_card, id_custom_field, value)
except ApiException as e:
    print("Exception when calling DefaultApi->card_id_card_custom_field_id_custom_field_item_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_card** | **str**| ID of the card that the Custom Field value should be set/updated for | 
 **id_custom_field** | **str**| ID of the Custom Field on the card. | 
 **value** | **str**| An object containing the key and value to set for the card&#39;s Custom Field value. The key used to set the value should match the type of Custom Field defined. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_actions_comments_post**
> cards_id_actions_comments_post(id, text)

Add a new comment to a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
text = 'text_example' # str | The comment

try:
    # Add a new comment to a card
    api_instance.cards_id_actions_comments_post(id, text)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_actions_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **text** | **str**| The comment | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_actions_get**
> cards_id_actions_get(id)

List the actions on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card

try:
    # List the actions on a card
    api_instance.cards_id_actions_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_actions_id_action_comments_delete**
> cards_id_actions_id_action_comments_delete(id, id_action)

Delete a comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_action = 'id_action_example' # str | The ID of the comment action

try:
    # Delete a comment
    api_instance.cards_id_actions_id_action_comments_delete(id, id_action)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_actions_id_action_comments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_action** | **str**| The ID of the comment action | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_actions_id_action_comments_put**
> cards_id_actions_id_action_comments_put(id, id_action, text)

Update an existing comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_action = 'id_action_example' # str | The ID of the comment action to update
text = 'text_example' # str | The new text for the comment

try:
    # Update an existing comment
    api_instance.cards_id_actions_id_action_comments_put(id, id_action, text)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_actions_id_action_comments_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_action** | **str**| The ID of the comment action to update | 
 **text** | **str**| The new text for the comment | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_attachments_get**
> cards_id_attachments_get(id, fields, filter)

List the attachments on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of attachment fields
filter = 'filter_example' # str | Use cover to restrict to just the cover attachment

try:
    # List the attachments on a card
    api_instance.cards_id_attachments_get(id, fields, filter)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of attachment fields | 
 **filter** | **str**| Use cover to restrict to just the cover attachment | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_attachments_id_attachment_delete**
> cards_id_attachments_id_attachment_delete(id, id_attachment)

Delete an attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_attachment = 'id_attachment_example' # str | The ID of the attachment to delete

try:
    # Delete an attachment
    api_instance.cards_id_attachments_id_attachment_delete(id, id_attachment)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_attachments_id_attachment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_attachment** | **str**| The ID of the attachment to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_attachments_id_attachment_get**
> cards_id_attachments_id_attachment_get(id, id_attachment, fields=fields)

Get a specific attachment on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_attachment = 'id_attachment_example' # str | The ID of the attachment
fields = 'fields_example' # str | all or a comma-separated list of attachment fields (optional)

try:
    # Get a specific attachment on a card
    api_instance.cards_id_attachments_id_attachment_get(id, id_attachment, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_attachments_id_attachment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_attachment** | **str**| The ID of the attachment | 
 **fields** | **str**| all or a comma-separated list of attachment fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_attachments_post**
> cards_id_attachments_post(id, name=name, file=file, mime_type=mime_type, url=url)

Add an attachment to a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
name = 'name_example' # str | The name of the attachment. Max length 256. (optional)
file = 'file_example' # str | The file to attach, as multipart/form-data (optional)
mime_type = 'mime_type_example' # str | The mimeType of the attachment. Max length 256 (optional)
url = 'url_example' # str | A URL to attach. Must start with http:// or https:// (optional)

try:
    # Add an attachment to a card
    api_instance.cards_id_attachments_post(id, name=name, file=file, mime_type=mime_type, url=url)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **name** | **str**| The name of the attachment. Max length 256. | [optional] 
 **file** | **str**| The file to attach, as multipart/form-data | [optional] 
 **mime_type** | **str**| The mimeType of the attachment. Max length 256 | [optional] 
 **url** | **str**| A URL to attach. Must start with http:// or https:// | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_board_get**
> cards_id_board_get(id, fields=fields)

Get the board a card is on

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of board fields (optional)

try:
    # Get the board a card is on
    api_instance.cards_id_board_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_board_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of board fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_card_checklist_id_checklist_check_item_id_check_item_put**
> cards_id_card_checklist_id_checklist_check_item_id_check_item_put(id_card, id_check_item, id_checklist, pos=pos)

Update an item in a checklist on a card.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_card = 'id_card_example' # str | The ID of the card
id_check_item = 'id_check_item_example' # str | The ID of the checklist item to update
id_checklist = 'id_checklist_example' # str | The ID of the item to update.
pos = 'pos_example' # str | top, bottom, or a positive float (optional)

try:
    # Update an item in a checklist on a card.
    api_instance.cards_id_card_checklist_id_checklist_check_item_id_check_item_put(id_card, id_check_item, id_checklist, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_card_checklist_id_checklist_check_item_id_check_item_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_card** | **str**| The ID of the card | 
 **id_check_item** | **str**| The ID of the checklist item to update | 
 **id_checklist** | **str**| The ID of the item to update. | 
 **pos** | **str**| top, bottom, or a positive float | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_check_item_id_check_item_delete**
> cards_id_check_item_id_check_item_delete(id, id_check_item)

Delete a checklist item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_check_item = 'id_check_item_example' # str | The ID of the checklist item to delete

try:
    # Delete a checklist item
    api_instance.cards_id_check_item_id_check_item_delete(id, id_check_item)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_check_item_id_check_item_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_check_item** | **str**| The ID of the checklist item to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_check_item_id_check_item_get**
> cards_id_check_item_id_check_item_get(id, id_check_item, fields=fields)

Get a specific checkItem on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_check_item = 'id_check_item_example' # str | The ID of the checkitem
fields = 'fields_example' # str | all or a comma-separated list of name,nameData,pos,state,type (optional)

try:
    # Get a specific checkItem on a card
    api_instance.cards_id_check_item_id_check_item_get(id, id_check_item, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_check_item_id_check_item_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_check_item** | **str**| The ID of the checkitem | 
 **fields** | **str**| all or a comma-separated list of name,nameData,pos,state,type | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_check_item_id_check_item_put**
> cards_id_check_item_id_check_item_put(id, id_check_item, name=name, state=state, id_checklist=id_checklist, pos=pos)

Update an item in a checklist on a card.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_check_item = 'id_check_item_example' # str | The ID of the checklist item to update
name = 'name_example' # str | The new name for the checklist item (optional)
state = 'state_example' # str | One of: complete, incomplete (optional)
id_checklist = 'id_checklist_example' # str | The ID of the checklist this item is in (optional)
pos = 'pos_example' # str | top, bottom, or a positive float (optional)

try:
    # Update an item in a checklist on a card.
    api_instance.cards_id_check_item_id_check_item_put(id, id_check_item, name=name, state=state, id_checklist=id_checklist, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_check_item_id_check_item_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_check_item** | **str**| The ID of the checklist item to update | 
 **name** | **str**| The new name for the checklist item | [optional] 
 **state** | **str**| One of: complete, incomplete | [optional] 
 **id_checklist** | **str**| The ID of the checklist this item is in | [optional] 
 **pos** | **str**| top, bottom, or a positive float | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_check_item_states_get**
> cards_id_check_item_states_get(id, fields=fields)

Get the completed checklist items on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of: idCheckItem, state (optional)

try:
    # Get the completed checklist items on a card
    api_instance.cards_id_check_item_states_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_check_item_states_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of: idCheckItem, state | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_checklists_get**
> cards_id_checklists_get(id, check_items=check_items, check_item_fields=check_item_fields, filter=filter, fields=fields)

Get the checklists on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
check_items = 'check_items_example' # str | all or none (optional)
check_item_fields = 'check_item_fields_example' # str | all or a comma-separated list of: name,nameData,pos,state,type (optional)
filter = 'filter_example' # str | all or none (optional)
fields = 'fields_example' # str | all or a comma-separated list of: idBoard,idCard,name,pos (optional)

try:
    # Get the checklists on a card
    api_instance.cards_id_checklists_get(id, check_items=check_items, check_item_fields=check_item_fields, filter=filter, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_checklists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **check_items** | **str**| all or none | [optional] 
 **check_item_fields** | **str**| all or a comma-separated list of: name,nameData,pos,state,type | [optional] 
 **filter** | **str**| all or none | [optional] 
 **fields** | **str**| all or a comma-separated list of: idBoard,idCard,name,pos | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_checklists_id_checklist_delete**
> cards_id_checklists_id_checklist_delete(id, id_checklist)

Delete a checklist from a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_checklist = 'id_checklist_example' # str | The ID of the checklist to delete

try:
    # Delete a checklist from a card
    api_instance.cards_id_checklists_id_checklist_delete(id, id_checklist)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_checklists_id_checklist_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_checklist** | **str**| The ID of the checklist to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_checklists_post**
> cards_id_checklists_post(id, name=name, id_checklist_source=id_checklist_source, pos=pos)

Create a new checklist on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
name = 'name_example' # str | The name of the checklist (optional)
id_checklist_source = 'id_checklist_source_example' # str | The ID of a source checklist to copy into the new one (optional)
pos = 'pos_example' # str | The position of the checklist on the card. One of: top, bottom, or a positive number. (optional)

try:
    # Create a new checklist on a card
    api_instance.cards_id_checklists_post(id, name=name, id_checklist_source=id_checklist_source, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_checklists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **name** | **str**| The name of the checklist | [optional] 
 **id_checklist_source** | **str**| The ID of a source checklist to copy into the new one | [optional] 
 **pos** | **str**| The position of the checklist on the card. One of: top, bottom, or a positive number. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_custom_field_items_get**
> cards_id_custom_field_items_get(id)

Get the custom field items for a card.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card

try:
    # Get the custom field items for a card.
    api_instance.cards_id_custom_field_items_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_custom_field_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_delete**
> cards_id_delete(id)

Delete a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card

try:
    # Delete a card
    api_instance.cards_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_field_get**
> cards_id_field_get(id, field)

Get a specific property of a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the card
field = 'field_example' # str | The desired field. One of fields

try:
    # Get a specific property of a card
    api_instance.cards_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the card | 
 **field** | **str**| The desired field. One of fields | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_get**
> cards_id_get(id, fields=fields, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, members_voted=members_voted, member_voted_fields=member_voted_fields, check_item_states=check_item_states, checklists=checklists, checklist_fields=checklist_fields, board=board, board_fields=board_fields, list=list, plugin_data=plugin_data, stickers=stickers, sticker_fields=sticker_fields, custom_field_items=custom_field_items)

Get a card by its ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of fields. Defaults: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url (optional)
actions = 'actions_example' # str | See the Actions Nested Resource (optional)
attachments = 'attachments_example' # str | true, false, or cover (optional)
attachment_fields = 'attachment_fields_example' # str | all or a comma-separated list of attachment fields (optional)
members = 'members_example' # str | Whether to return member objects for members on the card (optional)
member_fields = 'member_fields_example' # str | all or a comma-separated list of member fields. Defaults: avatarHash, fullName, initials, username (optional)
members_voted = 'members_voted_example' # str | Whether to return member objects for members who voted on the card (optional)
member_voted_fields = 'member_voted_fields_example' # str | all or a comma-separated list of member fields. Defaults: avatarHash, fullName, initials, username (optional)
check_item_states = 'check_item_states_example' # str |  (optional)
checklists = 'checklists_example' # str | Whether to return the checklists on the card. all or none (optional)
checklist_fields = 'checklist_fields_example' # str | all or a comma-separated list of idBoard,idCard,name,pos (optional)
board = 'board_example' # str | Whether to return the board object the card is on (optional)
board_fields = 'board_fields_example' # str | all or a comma-separated list of board fields. Defaults: name, desc, descData, closed, idOrganization, pinned, url, prefs (optional)
list = 'list_example' # str | See the Lists Nested Resource (optional)
plugin_data = 'plugin_data_example' # str | Whether to include pluginData on the card with the response (optional)
stickers = 'stickers_example' # str | Whether to include sticker models with the response (optional)
sticker_fields = 'sticker_fields_example' # str | all or a comma-separated list of sticker fields (optional)
custom_field_items = 'custom_field_items_example' # str | Whether to include the customFieldItems (optional)

try:
    # Get a card by its ID
    api_instance.cards_id_get(id, fields=fields, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, members_voted=members_voted, member_voted_fields=member_voted_fields, check_item_states=check_item_states, checklists=checklists, checklist_fields=checklist_fields, board=board, board_fields=board_fields, list=list, plugin_data=plugin_data, stickers=stickers, sticker_fields=sticker_fields, custom_field_items=custom_field_items)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of fields. Defaults: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url | [optional] 
 **actions** | **str**| See the Actions Nested Resource | [optional] 
 **attachments** | **str**| true, false, or cover | [optional] 
 **attachment_fields** | **str**| all or a comma-separated list of attachment fields | [optional] 
 **members** | **str**| Whether to return member objects for members on the card | [optional] 
 **member_fields** | **str**| all or a comma-separated list of member fields. Defaults: avatarHash, fullName, initials, username | [optional] 
 **members_voted** | **str**| Whether to return member objects for members who voted on the card | [optional] 
 **member_voted_fields** | **str**| all or a comma-separated list of member fields. Defaults: avatarHash, fullName, initials, username | [optional] 
 **check_item_states** | **str**|  | [optional] 
 **checklists** | **str**| Whether to return the checklists on the card. all or none | [optional] 
 **checklist_fields** | **str**| all or a comma-separated list of idBoard,idCard,name,pos | [optional] 
 **board** | **str**| Whether to return the board object the card is on | [optional] 
 **board_fields** | **str**| all or a comma-separated list of board fields. Defaults: name, desc, descData, closed, idOrganization, pinned, url, prefs | [optional] 
 **list** | **str**| See the Lists Nested Resource | [optional] 
 **plugin_data** | **str**| Whether to include pluginData on the card with the response | [optional] 
 **stickers** | **str**| Whether to include sticker models with the response | [optional] 
 **sticker_fields** | **str**| all or a comma-separated list of sticker fields | [optional] 
 **custom_field_items** | **str**| Whether to include the customFieldItems | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_id_labels_id_label_delete**
> cards_id_id_labels_id_label_delete(id, id_label)

Remove a label from a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_label = 'id_label_example' # str | The ID of the label to remove

try:
    # Remove a label from a card
    api_instance.cards_id_id_labels_id_label_delete(id, id_label)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_id_labels_id_label_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_label** | **str**| The ID of the label to remove | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_id_labels_post**
> cards_id_id_labels_post(id, value=value)

Add a label to a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
value = 'value_example' # str | The ID of the label to add (optional)

try:
    # Add a label to a card
    api_instance.cards_id_id_labels_post(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_id_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **value** | **str**| The ID of the label to add | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_id_members_id_member_delete**
> cards_id_id_members_id_member_delete(id, id_member)

Remove a member from a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_member = 'id_member_example' # str | The ID of the member to remove from the card

try:
    # Remove a member from a card
    api_instance.cards_id_id_members_id_member_delete(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_id_members_id_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_member** | **str**| The ID of the member to remove from the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_id_members_post**
> cards_id_id_members_post(id, value=value)

Add a member to a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
value = 'value_example' # str | The ID of the member to add to the card (optional)

try:
    # Add a member to a card
    api_instance.cards_id_id_members_post(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **value** | **str**| The ID of the member to add to the card | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_labels_post**
> cards_id_labels_post(id, color, name=name)

Add a new label to a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
color = 'color_example' # str | A valid label color or null. See labels
name = 'name_example' # str | A name for the label (optional)

try:
    # Add a new label to a card
    api_instance.cards_id_labels_post(id, color, name=name)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **color** | **str**| A valid label color or null. See labels | 
 **name** | **str**| A name for the label | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_list_get**
> cards_id_list_get(id, fields=fields)

Get the list a card is in

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of list fields (optional)

try:
    # Get the list a card is in
    api_instance.cards_id_list_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of list fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_mark_associated_notifications_read_post**
> cards_id_mark_associated_notifications_read_post(id)

Mark notifications about this card as read

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card

try:
    # Mark notifications about this card as read
    api_instance.cards_id_mark_associated_notifications_read_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_mark_associated_notifications_read_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_members_get**
> cards_id_members_get(id, fields=fields)

Get the members on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Get the members on a card
    api_instance.cards_id_members_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_members_voted_get**
> cards_id_members_voted_get(id, fields=fields)

Get the members who have voted on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Get the members who have voted on a card
    api_instance.cards_id_members_voted_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_members_voted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_members_voted_id_member_delete**
> cards_id_members_voted_id_member_delete(id, id_member)

Remove a member's vote from a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_member = 'id_member_example' # str | The ID of the member whose vote to remove

try:
    # Remove a member's vote from a card
    api_instance.cards_id_members_voted_id_member_delete(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_members_voted_id_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_member** | **str**| The ID of the member whose vote to remove | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_members_voted_post**
> cards_id_members_voted_post(id, value)

Vote on the card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
value = 'value_example' # str | The ID of the member to vote 'yes' on the card

try:
    # Vote on the card
    api_instance.cards_id_members_voted_post(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_members_voted_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **value** | **str**| The ID of the member to vote &#39;yes&#39; on the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_plugin_data_get**
> cards_id_plugin_data_get(id)

Get any shared pluginData on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card

try:
    # Get any shared pluginData on a card
    api_instance.cards_id_plugin_data_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_plugin_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_put**
> cards_id_put(id, name=name, desc=desc, closed=closed, id_members=id_members, id_attachment_cover=id_attachment_cover, id_list=id_list, id_labels=id_labels, id_board=id_board, pos=pos, due=due, due_complete=due_complete, subscribed=subscribed)

Update a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card to update
name = 'name_example' # str | The new name for the card (optional)
desc = 'desc_example' # str | The new description for the card (optional)
closed = 'closed_example' # str | Whether the card should be archived (closed: true) (optional)
id_members = 'id_members_example' # str | Comma-separated list of member IDs (optional)
id_attachment_cover = 'id_attachment_cover_example' # str | The ID of the image attachment the card should use as its cover, or null for none (optional)
id_list = 'id_list_example' # str | The ID of the list the card should be in (optional)
id_labels = 'id_labels_example' # str | Comma-separated list of label IDs (optional)
id_board = 'id_board_example' # str | The ID of the board the card should be on (optional)
pos = 'pos_example' # str | The position of the card in its list. top, bottom, or a positive float (optional)
due = 'due_example' # str | When the card is due, or null (optional)
due_complete = 'due_complete_example' # str | Whether the due date should be marked complete (optional)
subscribed = 'subscribed_example' # str | Whether the member is should be subscribed to the card (optional)

try:
    # Update a card
    api_instance.cards_id_put(id, name=name, desc=desc, closed=closed, id_members=id_members, id_attachment_cover=id_attachment_cover, id_list=id_list, id_labels=id_labels, id_board=id_board, pos=pos, due=due, due_complete=due_complete, subscribed=subscribed)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card to update | 
 **name** | **str**| The new name for the card | [optional] 
 **desc** | **str**| The new description for the card | [optional] 
 **closed** | **str**| Whether the card should be archived (closed: true) | [optional] 
 **id_members** | **str**| Comma-separated list of member IDs | [optional] 
 **id_attachment_cover** | **str**| The ID of the image attachment the card should use as its cover, or null for none | [optional] 
 **id_list** | **str**| The ID of the list the card should be in | [optional] 
 **id_labels** | **str**| Comma-separated list of label IDs | [optional] 
 **id_board** | **str**| The ID of the board the card should be on | [optional] 
 **pos** | **str**| The position of the card in its list. top, bottom, or a positive float | [optional] 
 **due** | **str**| When the card is due, or null | [optional] 
 **due_complete** | **str**| Whether the due date should be marked complete | [optional] 
 **subscribed** | **str**| Whether the member is should be subscribed to the card | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_stickers_get**
> cards_id_stickers_get(id, fields=fields)

Get the stickers on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
fields = 'fields_example' # str | all or a comma-separated list of sticker fields (optional)

try:
    # Get the stickers on a card
    api_instance.cards_id_stickers_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_stickers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **fields** | **str**| all or a comma-separated list of sticker fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_stickers_id_sticker_delete**
> cards_id_stickers_id_sticker_delete(id, id_sticker)

Remove a sticker from the card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_sticker = 'id_sticker_example' # str | The ID of the sticker to remove from the card

try:
    # Remove a sticker from the card
    api_instance.cards_id_stickers_id_sticker_delete(id, id_sticker)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_stickers_id_sticker_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_sticker** | **str**| The ID of the sticker to remove from the card | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_stickers_id_sticker_get**
> cards_id_stickers_id_sticker_get(id, id_sticker, fields=fields)

Get a specific sticker on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_sticker = 'id_sticker_example' # str | The ID of the sticker
fields = 'fields_example' # str | all or a comma-separated list of sticker fields (optional)

try:
    # Get a specific sticker on a card
    api_instance.cards_id_stickers_id_sticker_get(id, id_sticker, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_stickers_id_sticker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_sticker** | **str**| The ID of the sticker | 
 **fields** | **str**| all or a comma-separated list of sticker fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_id_stickers_id_sticker_put**
> cards_id_stickers_id_sticker_put(id, id_sticker, top=top, left=left, z_index=z_index, rotate=rotate)

Update a sticker on a card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the card
id_sticker = 'id_sticker_example' # str | The ID of the sticker to update
top = 'top_example' # str |  (optional)
left = 'left_example' # str |  (optional)
z_index = 'z_index_example' # str |  (optional)
rotate = 'rotate_example' # str |  (optional)

try:
    # Update a sticker on a card
    api_instance.cards_id_stickers_id_sticker_put(id, id_sticker, top=top, left=left, z_index=z_index, rotate=rotate)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_id_stickers_id_sticker_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the card | 
 **id_sticker** | **str**| The ID of the sticker to update | 
 **top** | **str**|  | [optional] 
 **left** | **str**|  | [optional] 
 **z_index** | **str**|  | [optional] 
 **rotate** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_post**
> cards_post(id_list, name=name, desc=desc, pos=pos, due=due, due_complete=due_complete, id_members=id_members, id_labels=id_labels, url_source=url_source, file_source=file_source, id_card_source=id_card_source, keep_from_source=keep_from_source)

Create a new card

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_list = 'id_list_example' # str | The ID of the list the card should be created in
name = 'name_example' # str | The name for the card (optional)
desc = 'desc_example' # str | The description for the card (optional)
pos = 'pos_example' # str | The position of the new card. top, bottom, or a positive float (optional)
due = 'due_example' # str | A due date for the card (optional)
due_complete = 'due_complete_example' # str |  (optional)
id_members = 'id_members_example' # str | Comma-separated list of member IDs to add to the card (optional)
id_labels = 'id_labels_example' # str | Comma-separated list of label IDs to add to the card (optional)
url_source = 'url_source_example' # str | A URL starting with http:// or https:// (optional)
file_source = 'file_source_example' # str |  (optional)
id_card_source = 'id_card_source_example' # str | The ID of a card to copy into the new card (optional)
keep_from_source = 'keep_from_source_example' # str | If using idCardSource you can specify which properties to copy over. all or comma-separated list of: attachments,checklists,comments,due,labels,members,stickers (optional)

try:
    # Create a new card
    api_instance.cards_post(id_list, name=name, desc=desc, pos=pos, due=due, due_complete=due_complete, id_members=id_members, id_labels=id_labels, url_source=url_source, file_source=file_source, id_card_source=id_card_source, keep_from_source=keep_from_source)
except ApiException as e:
    print("Exception when calling DefaultApi->cards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_list** | **str**| The ID of the list the card should be created in | 
 **name** | **str**| The name for the card | [optional] 
 **desc** | **str**| The description for the card | [optional] 
 **pos** | **str**| The position of the new card. top, bottom, or a positive float | [optional] 
 **due** | **str**| A due date for the card | [optional] 
 **due_complete** | **str**|  | [optional] 
 **id_members** | **str**| Comma-separated list of member IDs to add to the card | [optional] 
 **id_labels** | **str**| Comma-separated list of label IDs to add to the card | [optional] 
 **url_source** | **str**| A URL starting with http:// or https:// | [optional] 
 **file_source** | **str**|  | [optional] 
 **id_card_source** | **str**| The ID of a card to copy into the new card | [optional] 
 **keep_from_source** | **str**| If using idCardSource you can specify which properties to copy over. all or comma-separated list of: attachments,checklists,comments,due,labels,members,stickers | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_board_get**
> checklists_id_board_get(id, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
fields = 'fields_example' # str | all or a comma-separated list of board fields (optional)

try:
    api_instance.checklists_id_board_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_board_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **fields** | **str**| all or a comma-separated list of board fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_cards_get**
> checklists_id_cards_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.

try:
    api_instance.checklists_id_cards_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_cards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_check_items_get**
> checklists_id_check_items_get(id, filter=filter, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
filter = 'filter_example' # str | One of: all, none. (optional)
fields = 'fields_example' # str | One of: all, name, nameData, pos, state, type. (optional)

try:
    api_instance.checklists_id_check_items_get(id, filter=filter, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_check_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **filter** | **str**| One of: all, none. | [optional] 
 **fields** | **str**| One of: all, name, nameData, pos, state, type. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_check_items_id_check_item_delete**
> checklists_id_check_items_id_check_item_delete(id, id_check_item)

Remove an item from a checklist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
id_check_item = 'id_check_item_example' # str | ID of the checklist item to delete.

try:
    # Remove an item from a checklist
    api_instance.checklists_id_check_items_id_check_item_delete(id, id_check_item)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_check_items_id_check_item_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **id_check_item** | **str**| ID of the checklist item to delete. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_check_items_id_check_item_get**
> checklists_id_check_items_id_check_item_get(id, id_check_item, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
id_check_item = 'id_check_item_example' # str | ID of the check item to retrieve.
fields = 'fields_example' # str | One of: all, name, nameData, pos, state, type. (optional)

try:
    api_instance.checklists_id_check_items_id_check_item_get(id, id_check_item, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_check_items_id_check_item_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **id_check_item** | **str**| ID of the check item to retrieve. | 
 **fields** | **str**| One of: all, name, nameData, pos, state, type. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_check_items_id_check_item_put**
> checklists_id_check_items_id_check_item_put(id, id_check_item, pos)

Update check item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
id_check_item = 'id_check_item_example' # str | ID of the check item to retrieve.
pos = 'pos_example' # str | Position to move check item to.

try:
    # Update check item.
    api_instance.checklists_id_check_items_id_check_item_put(id, id_check_item, pos)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_check_items_id_check_item_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **id_check_item** | **str**| ID of the check item to retrieve. | 
 **pos** | **str**| Position to move check item to. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_check_items_post**
> checklists_id_check_items_post(id, name, pos=pos, checked=checked)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
name = 'name_example' # str | The name of the new check item on the checklist. Should be a string of length 1 to 16384.
pos = 'pos_example' # str | The position of the check item in the checklist. One of: top, bottom, or a positive number. (optional)
checked = 'checked_example' # str | Determines whether the check item is already checked when created. (optional)

try:
    api_instance.checklists_id_check_items_post(id, name, pos=pos, checked=checked)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_check_items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **name** | **str**| The name of the new check item on the checklist. Should be a string of length 1 to 16384. | 
 **pos** | **str**| The position of the check item in the checklist. One of: top, bottom, or a positive number. | [optional] 
 **checked** | **str**| Determines whether the check item is already checked when created. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_delete**
> checklists_id_delete(id)

Delete a checklist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.

try:
    # Delete a checklist
    api_instance.checklists_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_field_get**
> checklists_id_field_get(id, field)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
field = 'field_example' # str | A checklist field

try:
    api_instance.checklists_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **field** | **str**| A checklist field | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_get**
> checklists_id_get(id, cards=cards, check_items=check_items, check_item_fields=check_item_fields, fields=fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
cards = 'cards_example' # str | Valid values: all, closed, none, open, visible. Cards is a nested resource. The additional query params available are documented at Cards Nested Resource. (optional)
check_items = 'check_items_example' # str | The check items on the list to return. One of: all, none. (optional)
check_item_fields = 'check_item_fields_example' # str | The fields on the checkItem to return if checkItems are being returned. all or a comma-separated list of: name, nameData, pos, state, type (optional)
fields = 'fields_example' # str | all or a comma-separated list of checklist fields (optional)

try:
    api_instance.checklists_id_get(id, cards=cards, check_items=check_items, check_item_fields=check_item_fields, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **cards** | **str**| Valid values: all, closed, none, open, visible. Cards is a nested resource. The additional query params available are documented at Cards Nested Resource. | [optional] 
 **check_items** | **str**| The check items on the list to return. One of: all, none. | [optional] 
 **check_item_fields** | **str**| The fields on the checkItem to return if checkItems are being returned. all or a comma-separated list of: name, nameData, pos, state, type | [optional] 
 **fields** | **str**| all or a comma-separated list of checklist fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_name_put**
> checklists_id_name_put(id, value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
value = 'value_example' # str | The value to change the checklist name to. Should be a string of length 1 to 16384.

try:
    api_instance.checklists_id_name_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **value** | **str**| The value to change the checklist name to. Should be a string of length 1 to 16384. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_id_put**
> checklists_id_put(id, name=name, pos=pos)

Update an existing checklist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of a checklist.
name = 'name_example' # str | Name of the new checklist being created. Should be length of 1 to 16384. (optional)
pos = 'pos_example' # str | Determines the position of the checklist on the card. One of: top, bottom, or a positive number. (optional)

try:
    # Update an existing checklist.
    api_instance.checklists_id_put(id, name=name, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of a checklist. | 
 **name** | **str**| Name of the new checklist being created. Should be length of 1 to 16384. | [optional] 
 **pos** | **str**| Determines the position of the checklist on the card. One of: top, bottom, or a positive number. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checklists_post**
> checklists_post(id_card, name=name, pos=pos, id_checklist_source=id_checklist_source)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id_card = 'id_card_example' # str | The ID of the card that the checklist should be added to.
name = 'name_example' # str | The name of the checklist. Should be a string of length 1 to 16384. (optional)
pos = 'pos_example' # str | The position of the checklist on the card. One of: top, bottom, or a positive number. (optional)
id_checklist_source = 'id_checklist_source_example' # str | The ID of a checklist to copy into the new checklist. (optional)

try:
    api_instance.checklists_post(id_card, name=name, pos=pos, id_checklist_source=id_checklist_source)
except ApiException as e:
    print("Exception when calling DefaultApi->checklists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_card** | **str**| The ID of the card that the checklist should be added to. | 
 **name** | **str**| The name of the checklist. Should be a string of length 1 to 16384. | [optional] 
 **pos** | **str**| The position of the checklist on the card. One of: top, bottom, or a positive number. | [optional] 
 **id_checklist_source** | **str**| The ID of a checklist to copy into the new checklist. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_delete**
> custom_fields_id_delete(id)

Delete a Custom Field from a board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the customfield to delete.

try:
    # Delete a Custom Field from a board.
    api_instance.custom_fields_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->custom_fields_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the customfield to delete. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_get**
> custom_fields_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the customfield to retrieve.

try:
    api_instance.custom_fields_id_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->custom_fields_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the customfield to retrieve. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_options_get**
> custom_fields_id_options_get(id)

Get the options of a drop down Custom Field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the customfield.

try:
    # Get the options of a drop down Custom Field
    api_instance.custom_fields_id_options_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->custom_fields_id_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the customfield. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_options_id_custom_field_option_get**
> custom_fields_id_options_id_custom_field_option_get(id, id_custom_field_option)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the customfielditem.
id_custom_field_option = 'id_custom_field_option_example' # str | ID of the customfieldoption to retrieve.

try:
    api_instance.custom_fields_id_options_id_custom_field_option_get(id, id_custom_field_option)
except ApiException as e:
    print("Exception when calling DefaultApi->custom_fields_id_options_id_custom_field_option_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the customfielditem. | 
 **id_custom_field_option** | **str**| ID of the customfieldoption to retrieve. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_options_post**
> custom_fields_id_options_post(id)

Add an option to a dropdown Custom Field

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the customfield.

try:
    # Add an option to a dropdown Custom Field
    api_instance.custom_fields_id_options_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->custom_fields_id_options_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the customfield. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_put**
> custom_fields_id_put(id)

Update a Custom Field definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the customfield to update.

try:
    # Update a Custom Field definition.
    api_instance.custom_fields_id_put(id)
except ApiException as e:
    print("Exception when calling DefaultApi->custom_fields_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the customfield to update. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_post**
> custom_fields_post()

Create a new Custom Field on a board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Create a new Custom Field on a board.
    api_instance.custom_fields_post()
except ApiException as e:
    print("Exception when calling DefaultApi->custom_fields_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customfields_id_options_id_custom_field_option_delete**
> customfields_id_options_id_custom_field_option_delete(id, id_custom_field_option)

Delete an option from a Custom Field dropdown.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the customfielditem.
id_custom_field_option = 'id_custom_field_option_example' # str | ID of the customfieldoption to delete.

try:
    # Delete an option from a Custom Field dropdown.
    api_instance.customfields_id_options_id_custom_field_option_delete(id, id_custom_field_option)
except ApiException as e:
    print("Exception when calling DefaultApi->customfields_id_options_id_custom_field_option_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the customfielditem. | 
 **id_custom_field_option** | **str**| ID of the customfieldoption to delete. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emoji_get**
> emoji_get(locale=locale, spritesheets=spritesheets)

List available emoji

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The locale to return emoji descriptions and names in. Defaults to the logged in member's locale. (optional)
spritesheets = 'spritesheets_example' # str | true to return spritesheet URLs in the response (optional)

try:
    # List available emoji
    api_instance.emoji_get(locale=locale, spritesheets=spritesheets)
except ApiException as e:
    print("Exception when calling DefaultApi->emoji_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The locale to return emoji descriptions and names in. Defaults to the logged in member&#39;s locale. | [optional] 
 **spritesheets** | **str**| true to return spritesheet URLs in the response | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_admins_get**
> enterprises_id_admins_get(id, fields=fields)

Get an enterprise's admin members.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
fields = 'fields_example' # str | Any valid value that the nested member field resource accepts. (optional)

try:
    # Get an enterprise's admin members.
    api_instance.enterprises_id_admins_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_admins_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **fields** | **str**| Any valid value that the nested member field resource accepts. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_admins_id_member_delete**
> enterprises_id_admins_id_member_delete(id, id_member)

Remove an member as admin from an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
id_member = 'id_member_example' # str | ID of the member to be removed as an admin from enterprise.

try:
    # Remove an member as admin from an enterprise.
    api_instance.enterprises_id_admins_id_member_delete(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_admins_id_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **id_member** | **str**| ID of the member to be removed as an admin from enterprise. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_admins_id_member_put**
> enterprises_id_admins_id_member_put(id, id_member)

Make member an admin of enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
id_member = 'id_member_example' # str | ID of member to be made an admin of enterprise.

try:
    # Make member an admin of enterprise.
    api_instance.enterprises_id_admins_id_member_put(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_admins_id_member_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **id_member** | **str**| ID of member to be made an admin of enterprise. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_get**
> enterprises_id_get(id, fields=fields, members=members, member_fields=member_fields, member_filter=member_filter, member_sort=member_sort, member_sort_by=member_sort_by, member_sort_order=member_sort_order, member_start_index=member_start_index, member_count=member_count, organizations=organizations, organization_fields=organization_fields, organization_paid_accounts=organization_paid_accounts, organization_memberships=organization_memberships)

Get an enterprise by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
fields = 'fields_example' # str | Comma-separated list of: id, name, displayName, prefs, ssoActivationFailed, idAdmins, idMembers (Note that the members array returned will be paginated if members is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. Read the SCIM documentation here for more information on filtering), idOrganizations, products, userTypes, idMembers, idOrganizations (optional)
members = 'members_example' # str | One of: none, normal, admins, owners, all (optional)
member_fields = 'member_fields_example' # str | One of: avatarHash, fullName, initials, username (optional)
member_filter = 'member_filter_example' # str | Pass a SCIM-style query to filter members. This takes precedence over the all/normal/admins value of members. If any of the member_* args are set, the member array will be paginated. (optional)
member_sort = 'member_sort_example' # str | This parameter expects a SCIM-style sorting value prefixed by a - to sort descending. If no - is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if members is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. (optional)
member_sort_by = 'member_sort_by_example' # str | Deprecated: Please use member_sort. This parameter expects a SCIM-style sorting value. Note that the members array returned will be paginated if members is normal or admins. Pagination can be controlled with member_startIndex, etc, and the API response's header will contain the total count and pagination state. (optional)
member_sort_order = 'member_sort_order_example' # str | Deprecated: Please use member_sort. One of: ascending, descending, asc, desc (optional)
member_start_index = 'member_start_index_example' # str | Any integer between 0 and 100. (optional)
member_count = 'member_count_example' # str | 0 to 100 (optional)
organizations = 'organizations_example' # str | One of: none, members, public, all (optional)
organization_fields = 'organization_fields_example' # str | Any valid value that the nested organization field resource accepts. (optional)
organization_paid_accounts = 'organization_paid_accounts_example' # str |  (optional)
organization_memberships = 'organization_memberships_example' # str | Comma-seperated list of: me, normal, admin, active, deactivated (optional)

try:
    # Get an enterprise by its ID.
    api_instance.enterprises_id_get(id, fields=fields, members=members, member_fields=member_fields, member_filter=member_filter, member_sort=member_sort, member_sort_by=member_sort_by, member_sort_order=member_sort_order, member_start_index=member_start_index, member_count=member_count, organizations=organizations, organization_fields=organization_fields, organization_paid_accounts=organization_paid_accounts, organization_memberships=organization_memberships)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **fields** | **str**| Comma-separated list of: id, name, displayName, prefs, ssoActivationFailed, idAdmins, idMembers (Note that the members array returned will be paginated if members is &#39;normal&#39; or &#39;admins&#39;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. Read the SCIM documentation here for more information on filtering), idOrganizations, products, userTypes, idMembers, idOrganizations | [optional] 
 **members** | **str**| One of: none, normal, admins, owners, all | [optional] 
 **member_fields** | **str**| One of: avatarHash, fullName, initials, username | [optional] 
 **member_filter** | **str**| Pass a SCIM-style query to filter members. This takes precedence over the all/normal/admins value of members. If any of the member_* args are set, the member array will be paginated. | [optional] 
 **member_sort** | **str**| This parameter expects a SCIM-style sorting value prefixed by a - to sort descending. If no - is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if members is &#39;normal&#39; or &#39;admins&#39;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. | [optional] 
 **member_sort_by** | **str**| Deprecated: Please use member_sort. This parameter expects a SCIM-style sorting value. Note that the members array returned will be paginated if members is normal or admins. Pagination can be controlled with member_startIndex, etc, and the API response&#39;s header will contain the total count and pagination state. | [optional] 
 **member_sort_order** | **str**| Deprecated: Please use member_sort. One of: ascending, descending, asc, desc | [optional] 
 **member_start_index** | **str**| Any integer between 0 and 100. | [optional] 
 **member_count** | **str**| 0 to 100 | [optional] 
 **organizations** | **str**| One of: none, members, public, all | [optional] 
 **organization_fields** | **str**| Any valid value that the nested organization field resource accepts. | [optional] 
 **organization_paid_accounts** | **str**|  | [optional] 
 **organization_memberships** | **str**| Comma-seperated list of: me, normal, admin, active, deactivated | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_members_get**
> enterprises_id_members_get(id, fields=fields, filter=filter, sort=sort, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count, organization_fields=organization_fields, board_fields=board_fields)

Get the members of an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
fields = 'fields_example' # str | A comma-seperated list of valid member fields. (optional)
filter = 'filter_example' # str | Pass a SCIM-style query to filter members. This takes precedence over the all/normal/admins value of members. If any of the below member_* args are set, the member array will be paginated. (optional)
sort = 'sort_example' # str | This parameter expects a SCIM-style sorting value prefixed by a - to sort descending. If no - is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if members is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. (optional)
sort_by = 'sort_by_example' # str | Deprecated: Please use sort instead. This parameter expects a SCIM-style sorting value. Note that the members array returned will be paginated if members is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. (optional)
sort_order = 'sort_order_example' # str | Deprecated: Please use sort instead. One of: ascending, descending, asc, desc. (optional)
start_index = 'start_index_example' # str | Any integer between 0 and 9999. (optional)
count = 'count_example' # str | SCIM-style filter. (optional)
organization_fields = 'organization_fields_example' # str | Any valid value that the nested organization field resource accepts. (optional)
board_fields = 'board_fields_example' # str | Any valid value that the nested board resource accepts. (optional)

try:
    # Get the members of an enterprise.
    api_instance.enterprises_id_members_get(id, fields=fields, filter=filter, sort=sort, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count, organization_fields=organization_fields, board_fields=board_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **fields** | **str**| A comma-seperated list of valid member fields. | [optional] 
 **filter** | **str**| Pass a SCIM-style query to filter members. This takes precedence over the all/normal/admins value of members. If any of the below member_* args are set, the member array will be paginated. | [optional] 
 **sort** | **str**| This parameter expects a SCIM-style sorting value prefixed by a - to sort descending. If no - is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if members is &#39;normal&#39; or &#39;admins&#39;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. | [optional] 
 **sort_by** | **str**| Deprecated: Please use sort instead. This parameter expects a SCIM-style sorting value. Note that the members array returned will be paginated if members is &#39;normal&#39; or &#39;admins&#39;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. | [optional] 
 **sort_order** | **str**| Deprecated: Please use sort instead. One of: ascending, descending, asc, desc. | [optional] 
 **start_index** | **str**| Any integer between 0 and 9999. | [optional] 
 **count** | **str**| SCIM-style filter. | [optional] 
 **organization_fields** | **str**| Any valid value that the nested organization field resource accepts. | [optional] 
 **board_fields** | **str**| Any valid value that the nested board resource accepts. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_members_id_member_deactivated_put**
> enterprises_id_members_id_member_deactivated_put(id, id_member, value, fields=fields, organization_fields=organization_fields, board_fields=board_fields)

Deactivate a member of an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
id_member = 'id_member_example' # str | ID of the member to deactive.
value = 'value_example' # str | Determines whether the user is deactivated or not.
fields = 'fields_example' # str | A comma separated list of any valid values that the nested member field resource accepts. (optional)
organization_fields = 'organization_fields_example' # str | Any valid value that the nested organization resource accepts. (optional)
board_fields = 'board_fields_example' # str | Any valid value that the nested board resource accepts. (optional)

try:
    # Deactivate a member of an enterprise.
    api_instance.enterprises_id_members_id_member_deactivated_put(id, id_member, value, fields=fields, organization_fields=organization_fields, board_fields=board_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_members_id_member_deactivated_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **id_member** | **str**| ID of the member to deactive. | 
 **value** | **str**| Determines whether the user is deactivated or not. | 
 **fields** | **str**| A comma separated list of any valid values that the nested member field resource accepts. | [optional] 
 **organization_fields** | **str**| Any valid value that the nested organization resource accepts. | [optional] 
 **board_fields** | **str**| Any valid value that the nested board resource accepts. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_members_id_member_get**
> enterprises_id_members_id_member_get(id, id_member=id_member, fields=fields, organization_fields=organization_fields, board_fields=board_fields)

Get a specific member of an enterprise by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
id_member = 'id_member_example' # str | An ID of a member resource. (optional)
fields = 'fields_example' # str | A comma separated list of any valid values that the nested member field resource accepts. (optional)
organization_fields = 'organization_fields_example' # str | Any valid value that the nested organization field resource accepts. (optional)
board_fields = 'board_fields_example' # str | Any valid value that the nested board resource accepts. (optional)

try:
    # Get a specific member of an enterprise by ID.
    api_instance.enterprises_id_members_id_member_get(id, id_member=id_member, fields=fields, organization_fields=organization_fields, board_fields=board_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_members_id_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **id_member** | **str**| An ID of a member resource. | [optional] 
 **fields** | **str**| A comma separated list of any valid values that the nested member field resource accepts. | [optional] 
 **organization_fields** | **str**| Any valid value that the nested organization field resource accepts. | [optional] 
 **board_fields** | **str**| Any valid value that the nested board resource accepts. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_organizations_id_organization_delete**
> enterprises_id_organizations_id_organization_delete(id, id_member)

Remove an organization from an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
id_member = 'id_member_example' # str | ID of the member to be removed as an admin from enterprise.

try:
    # Remove an organization from an enterprise.
    api_instance.enterprises_id_organizations_id_organization_delete(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_organizations_id_organization_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **id_member** | **str**| ID of the member to be removed as an admin from enterprise. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_organizations_put**
> enterprises_id_organizations_put(id, id_organization)

Transfer an organization to an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
id_organization = 'id_organization_example' # str | ID of organization to be transferred to enterprise.

try:
    # Transfer an organization to an enterprise.
    api_instance.enterprises_id_organizations_put(id, id_organization)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_organizations_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **id_organization** | **str**| ID of organization to be transferred to enterprise. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_signup_url_get**
> enterprises_id_signup_url_get(id, authenticate=authenticate, confirmation_accepted=confirmation_accepted, return_url=return_url, tos_accepted=tos_accepted)

Get the signup URL for an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
authenticate = 'authenticate_example' # str |  (optional)
confirmation_accepted = 'confirmation_accepted_example' # str |  (optional)
return_url = 'return_url_example' # str | Any valid URL. (optional)
tos_accepted = 'tos_accepted_example' # str | Designates whether the user has seen/consented to the Trello ToS prior to being redirected to the enterprise signup page/their IdP. (optional)

try:
    # Get the signup URL for an enterprise.
    api_instance.enterprises_id_signup_url_get(id, authenticate=authenticate, confirmation_accepted=confirmation_accepted, return_url=return_url, tos_accepted=tos_accepted)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_signup_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **authenticate** | **str**|  | [optional] 
 **confirmation_accepted** | **str**|  | [optional] 
 **return_url** | **str**| Any valid URL. | [optional] 
 **tos_accepted** | **str**| Designates whether the user has seen/consented to the Trello ToS prior to being redirected to the enterprise signup page/their IdP. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_tokens_post**
> enterprises_id_tokens_post(id, expiration=expiration)

Generate an auth token for an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
expiration = 'expiration_example' # str | One of: 1hour, 1day, 30days, never (optional)

try:
    # Generate an auth token for an enterprise.
    api_instance.enterprises_id_tokens_post(id, expiration=expiration)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_tokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **expiration** | **str**| One of: 1hour, 1day, 30days, never | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_transferrable_organization_id_organization_get**
> enterprises_id_transferrable_organization_id_organization_get(id, id_organization)

Get whether an organization can be transferred to an enterprise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
id_organization = 'id_organization_example' # str | An ID of an Organization resource.

try:
    # Get whether an organization can be transferred to an enterprise.
    api_instance.enterprises_id_transferrable_organization_id_organization_get(id, id_organization)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_transferrable_organization_id_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **id_organization** | **str**| An ID of an Organization resource. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_color_put**
> labels_id_color_put(id, value)

Update the color of a label by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the label
value = 'value_example' # str | The new color for the label. See: fields for color options.

try:
    # Update the color of a label by ID.
    api_instance.labels_id_color_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->labels_id_color_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the label | 
 **value** | **str**| The new color for the label. See: fields for color options. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_delete**
> labels_id_delete(id)

Delete a label by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the label to delete.

try:
    # Delete a label by ID.
    api_instance.labels_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->labels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the label to delete. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_get**
> labels_id_get(id, fields=fields)

Get information about a label by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str | all or a comma-separated list of fields (optional)

try:
    # Get information about a label by ID.
    api_instance.labels_id_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->labels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**| all or a comma-separated list of fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_name_put**
> labels_id_name_put(id, value)

Update the name of a label by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the label to update
value = 'value_example' # str | The new name for the label

try:
    # Update the name of a label by ID.
    api_instance.labels_id_name_put(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->labels_id_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the label to update | 
 **value** | **str**| The new name for the label | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_id_put**
> labels_id_put(id, name=name, color=color)

Update a label by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id of the label to update
name = 'name_example' # str | The new name for the label (optional)
color = 'color_example' # str | The new color for the label. See: fields for color options (optional)

try:
    # Update a label by ID.
    api_instance.labels_id_put(id, name=name, color=color)
except ApiException as e:
    print("Exception when calling DefaultApi->labels_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the label to update | 
 **name** | **str**| The new name for the label | [optional] 
 **color** | **str**| The new color for the label. See: fields for color options | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labels_post**
> labels_post(name, color, id_board)

Create a new label on a board.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name for the label
color = 'color_example' # str | The color for the label. See fields for color options.
id_board = 'id_board_example' # str | The ID of the board to create the label on.

try:
    # Create a new label on a board.
    api_instance.labels_post(name, color, id_board)
except ApiException as e:
    print("Exception when calling DefaultApi->labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for the label | 
 **color** | **str**| The color for the label. See fields for color options. | 
 **id_board** | **str**| The ID of the board to create the label on. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_actions_get**
> lists_id_actions_get(id)

List the actions on a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list

try:
    # List the actions on a list
    api_instance.lists_id_actions_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_archive_all_cards_post**
> lists_id_archive_all_cards_post(id)

Archive all cards in a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list

try:
    # Archive all cards in a list
    api_instance.lists_id_archive_all_cards_post(id)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_archive_all_cards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_board_get**
> lists_id_board_get(id, fields=fields)

Get the board a list is on

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
fields = 'fields_example' # str | all or a comma-separated list of board fields (optional)

try:
    # Get the board a list is on
    api_instance.lists_id_board_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_board_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **fields** | **str**| all or a comma-separated list of board fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_cards_get**
> lists_id_cards_get(id)

List the cards in a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list

try:
    # List the cards in a list
    api_instance.lists_id_cards_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_cards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_closed_put**
> lists_id_closed_put(id, value=value)

Archive or unarchive a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
value = 'value_example' # str | Set to true to close (archive) the list (optional)

try:
    # Archive or unarchive a list
    api_instance.lists_id_closed_put(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_closed_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **value** | **str**| Set to true to close (archive) the list | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_field_get**
> lists_id_field_get(id, field)

Get a specific property of a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
field = 'field_example' # str | The field to return. See fields

try:
    # Get a specific property of a list
    api_instance.lists_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **field** | **str**| The field to return. See fields | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_get**
> lists_id_get(id, fields=fields)

Get information about a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
fields = 'fields_example' # str | all or a comma separated list of fields (optional)

try:
    # Get information about a list
    api_instance.lists_id_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **fields** | **str**| all or a comma separated list of fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_id_board_put**
> lists_id_id_board_put(id, value=value)

Move a list to a new board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
value = 'value_example' # str | The ID of the board to move the list to (optional)

try:
    # Move a list to a new board
    api_instance.lists_id_id_board_put(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_id_board_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **value** | **str**| The ID of the board to move the list to | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_move_all_cards_post**
> lists_id_move_all_cards_post(id, id_board, id_list)

Move all cards in a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
id_board = 'id_board_example' # str | The ID of the board the cards should be moved to
id_list = 'id_list_example' # str | The ID of the list that the cards should be moved to

try:
    # Move all cards in a list
    api_instance.lists_id_move_all_cards_post(id, id_board, id_list)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_move_all_cards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **id_board** | **str**| The ID of the board the cards should be moved to | 
 **id_list** | **str**| The ID of the list that the cards should be moved to | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_name_put**
> lists_id_name_put(id, value=value)

Rename a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
value = 'value_example' # str | The new name for the list (optional)

try:
    # Rename a list
    api_instance.lists_id_name_put(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **value** | **str**| The new name for the list | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_pos_put**
> lists_id_pos_put(id, value=value)

Change the position of a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
value = 'value_example' # str | top, bottom, or a positive float (optional)

try:
    # Change the position of a list
    api_instance.lists_id_pos_put(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_pos_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **value** | **str**| top, bottom, or a positive float | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_put**
> lists_id_put(id, name=name, closed=closed, id_board=id_board, pos=pos, subscribed=subscribed)

Update the properties of a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list to update
name = 'name_example' # str | New name for the list (optional)
closed = 'closed_example' # str | Whether the list should be closed (archived) (optional)
id_board = 'id_board_example' # str | ID of a board the list should be moved to (optional)
pos = 'pos_example' # str | New position for the list: top, bottom, or a positive floating point number (optional)
subscribed = 'subscribed_example' # str | Whether the active member is subscribed to this list (optional)

try:
    # Update the properties of a list
    api_instance.lists_id_put(id, name=name, closed=closed, id_board=id_board, pos=pos, subscribed=subscribed)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list to update | 
 **name** | **str**| New name for the list | [optional] 
 **closed** | **str**| Whether the list should be closed (archived) | [optional] 
 **id_board** | **str**| ID of a board the list should be moved to | [optional] 
 **pos** | **str**| New position for the list: top, bottom, or a positive floating point number | [optional] 
 **subscribed** | **str**| Whether the active member is subscribed to this list | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_id_subscribed_put**
> lists_id_subscribed_put(id, value=value)

Subscribe or unsubscribe from a list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
value = 'value_example' # str | true to subscribe, false to unsubscribe (optional)

try:
    # Subscribe or unsubscribe from a list
    api_instance.lists_id_subscribed_put(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_id_subscribed_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **value** | **str**| true to subscribe, false to unsubscribe | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_post**
> lists_post(name, id_board, id_list_source=id_list_source, pos=pos)

Create a new list on a board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name for the list
id_board = 'id_board_example' # str | The long ID of the board the list should be created on
id_list_source = 'id_list_source_example' # str | ID of the list to copy into the new list (optional)
pos = 'pos_example' # str | Position of the list. top, bottom, or a positive floating point number (optional)

try:
    # Create a new list on a board
    api_instance.lists_post(name, id_board, id_list_source=id_list_source, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->lists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for the list | 
 **id_board** | **str**| The long ID of the board the list should be created on | 
 **id_list_source** | **str**| ID of the list to copy into the new list | [optional] 
 **pos** | **str**| Position of the list. top, bottom, or a positive floating point number | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_actions_get**
> members_id_actions_get(id)

List the actions for a member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member

try:
    # List the actions for a member
    api_instance.members_id_actions_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_avatar_post**
> members_id_avatar_post(id, file)

Create a new avatar for a member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
file = 'file_example' # str | 

try:
    # Create a new avatar for a member
    api_instance.members_id_avatar_post(id, file)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_avatar_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_backgrounds_get**
> members_id_board_backgrounds_get(id, filter=filter)

Get a member's custom board backgrounds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
filter = 'filter_example' # str | One of: all, custom, default, none, premium (optional)

try:
    # Get a member's custom board backgrounds
    api_instance.members_id_board_backgrounds_get(id, filter=filter)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_backgrounds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **filter** | **str**| One of: all, custom, default, none, premium | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_backgrounds_id_background_delete**
> members_id_board_backgrounds_id_background_delete(id, id_background)

Delete a board background

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_background = 'id_background_example' # str | The ID of the board background to delete

try:
    # Delete a board background
    api_instance.members_id_board_backgrounds_id_background_delete(id, id_background)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_backgrounds_id_background_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_background** | **str**| The ID of the board background to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_backgrounds_id_background_get**
> members_id_board_backgrounds_id_background_get(id, id_background, fields=fields)

Get a member's board background

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_background = 'id_background_example' # str | The ID of the board background
fields = 'fields_example' # str | all or a comma-separated list of: brightness, fullSizeUrl, scaled, tile (optional)

try:
    # Get a member's board background
    api_instance.members_id_board_backgrounds_id_background_get(id, id_background, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_backgrounds_id_background_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_background** | **str**| The ID of the board background | 
 **fields** | **str**| all or a comma-separated list of: brightness, fullSizeUrl, scaled, tile | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_backgrounds_id_background_put**
> members_id_board_backgrounds_id_background_put(id, id_background, brightness=brightness, tile=tile)

Update a board background

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_background = 'id_background_example' # str | The ID of the board background to update
brightness = 'brightness_example' # str | One of: dark, light, unknown (optional)
tile = 'tile_example' # str | Whether the background should be tiled (optional)

try:
    # Update a board background
    api_instance.members_id_board_backgrounds_id_background_put(id, id_background, brightness=brightness, tile=tile)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_backgrounds_id_background_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_background** | **str**| The ID of the board background to update | 
 **brightness** | **str**| One of: dark, light, unknown | [optional] 
 **tile** | **str**| Whether the background should be tiled | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_backgrounds_post**
> members_id_board_backgrounds_post(id, file)

Upload a new boardBackground

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
file = 'file_example' # str | 

try:
    # Upload a new boardBackground
    api_instance.members_id_board_backgrounds_post(id, file)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_backgrounds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_stars_get**
> members_id_board_stars_get(id)

List a member's board stars

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member

try:
    # List a member's board stars
    api_instance.members_id_board_stars_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_stars_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_stars_id_star_delete**
> members_id_board_stars_id_star_delete(id, id_star)

Unstar a board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_star = 'id_star_example' # str | The ID of the board star to remove

try:
    # Unstar a board
    api_instance.members_id_board_stars_id_star_delete(id, id_star)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_stars_id_star_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_star** | **str**| The ID of the board star to remove | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_stars_id_star_get**
> members_id_board_stars_id_star_get(id, id_star)

Get a specific boardStar

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_star = 'id_star_example' # str | The ID of the board star

try:
    # Get a specific boardStar
    api_instance.members_id_board_stars_id_star_get(id, id_star)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_stars_id_star_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_star** | **str**| The ID of the board star | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_stars_id_star_put**
> members_id_board_stars_id_star_put(id, id_star, pos=pos)

Update the position of a starred board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_star = 'id_star_example' # str | The ID of the board star to update
pos = 'pos_example' # str | New position for the starred board. top, bottom, or a positive float. (optional)

try:
    # Update the position of a starred board
    api_instance.members_id_board_stars_id_star_put(id, id_star, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_stars_id_star_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_star** | **str**| The ID of the board star to update | 
 **pos** | **str**| New position for the starred board. top, bottom, or a positive float. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_board_stars_post**
> members_id_board_stars_post(id, id_board, pos)

Star a new board

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_board = 'id_board_example' # str | The ID of the board to star
pos = 'pos_example' # str | The position of the newly starred board. top, bottom, or a positive float.

try:
    # Star a new board
    api_instance.members_id_board_stars_post(id, id_board, pos)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_board_stars_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_board** | **str**| The ID of the board to star | 
 **pos** | **str**| The position of the newly starred board. top, bottom, or a positive float. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_boards_get**
> members_id_boards_get(id, filter=filter, fields=fields, lists=lists, memberships=memberships, organization=organization, organization_fields=organization_fields)

Lists the boards a member has access to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
filter = 'filter_example' # str | all or a comma-separated list of: closed, members, open, organization, public, starred (optional)
fields = 'fields_example' # str | all or a comma-separated list of board fields (optional)
lists = 'lists_example' # str | Which lists to include with the boards. One of: all, closed, none, open (optional)
memberships = 'memberships_example' # str | all or a comma-separated list of active, admin, deactivated, me, normal (optional)
organization = 'organization_example' # str | Whether to include the organization object with the boards (optional)
organization_fields = 'organization_fields_example' # str | all or a comma-separated list of organization fields (optional)

try:
    # Lists the boards a member has access to
    api_instance.members_id_boards_get(id, filter=filter, fields=fields, lists=lists, memberships=memberships, organization=organization, organization_fields=organization_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_boards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **filter** | **str**| all or a comma-separated list of: closed, members, open, organization, public, starred | [optional] 
 **fields** | **str**| all or a comma-separated list of board fields | [optional] 
 **lists** | **str**| Which lists to include with the boards. One of: all, closed, none, open | [optional] 
 **memberships** | **str**| all or a comma-separated list of active, admin, deactivated, me, normal | [optional] 
 **organization** | **str**| Whether to include the organization object with the boards | [optional] 
 **organization_fields** | **str**| all or a comma-separated list of organization fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_boards_invited_get**
> members_id_boards_invited_get(id, fields=fields)

Get the boards the member has been invited to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
fields = 'fields_example' # str | all or a comma-separated list of board fields (optional)

try:
    # Get the boards the member has been invited to
    api_instance.members_id_boards_invited_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_boards_invited_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **fields** | **str**| all or a comma-separated list of board fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_cards_get**
> members_id_cards_get(id, filter=filter)

Gets the cards a member is on

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
filter = 'filter_example' # str | One of: all, closed, none, open, visible (optional)

try:
    # Gets the cards a member is on
    api_instance.members_id_cards_get(id, filter=filter)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_cards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **filter** | **str**| One of: all, closed, none, open, visible | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_board_backgrounds_get**
> members_id_custom_board_backgrounds_get(id)

Get a member's custom board backgrounds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member

try:
    # Get a member's custom board backgrounds
    api_instance.members_id_custom_board_backgrounds_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_board_backgrounds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_board_backgrounds_id_background_delete**
> members_id_custom_board_backgrounds_id_background_delete(id, id_background)

Delete a custom board background

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_background = 'id_background_example' # str | The ID of the custom board background to delete

try:
    # Delete a custom board background
    api_instance.members_id_custom_board_backgrounds_id_background_delete(id, id_background)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_board_backgrounds_id_background_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_background** | **str**| The ID of the custom board background to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_board_backgrounds_id_background_get**
> members_id_custom_board_backgrounds_id_background_get(id, fields=fields)

Get a specific custom board background

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
fields = 'fields_example' # str | all or a comma-separated list of brightness, fullSizeUrl, scaled, tile (optional)

try:
    # Get a specific custom board background
    api_instance.members_id_custom_board_backgrounds_id_background_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_board_backgrounds_id_background_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **fields** | **str**| all or a comma-separated list of brightness, fullSizeUrl, scaled, tile | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_board_backgrounds_id_background_put**
> members_id_custom_board_backgrounds_id_background_put(id, brightness=brightness, tile=tile)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
brightness = 'brightness_example' # str | One of: dark, light, unknown (optional)
tile = 'tile_example' # str | Whether to tile the background (optional)

try:
    api_instance.members_id_custom_board_backgrounds_id_background_put(id, brightness=brightness, tile=tile)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_board_backgrounds_id_background_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **brightness** | **str**| One of: dark, light, unknown | [optional] 
 **tile** | **str**| Whether to tile the background | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_board_backgrounds_post**
> members_id_custom_board_backgrounds_post(id, file)

Upload a new custom board background

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
file = 'file_example' # str | 

try:
    # Upload a new custom board background
    api_instance.members_id_custom_board_backgrounds_post(id, file)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_board_backgrounds_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_emoji_get**
> members_id_custom_emoji_get(id)

Get a member's uploaded custom emoji

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member

try:
    # Get a member's uploaded custom emoji
    api_instance.members_id_custom_emoji_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_emoji_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_emoji_id_emoji_get**
> members_id_custom_emoji_id_emoji_get(id, id_emoji, fields=fields)

Get a custom emoji

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_emoji = 'id_emoji_example' # str | The ID of the custom emoji
fields = 'fields_example' # str | all or a comma-separated list of name, url (optional)

try:
    # Get a custom emoji
    api_instance.members_id_custom_emoji_id_emoji_get(id, id_emoji, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_emoji_id_emoji_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_emoji** | **str**| The ID of the custom emoji | 
 **fields** | **str**| all or a comma-separated list of name, url | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_emoji_post**
> members_id_custom_emoji_post(id, file, name)

Upload a new custom emoji

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
file = 'file_example' # str | 
name = 'name_example' # str | Name for the emoji. 2 - 64 characters

try:
    # Upload a new custom emoji
    api_instance.members_id_custom_emoji_post(id, file, name)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_emoji_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **file** | **str**|  | 
 **name** | **str**| Name for the emoji. 2 - 64 characters | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_stickers_get**
> members_id_custom_stickers_get(id)

Get a member's uploaded stickers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member

try:
    # Get a member's uploaded stickers
    api_instance.members_id_custom_stickers_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_stickers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_stickers_id_sticker_delete**
> members_id_custom_stickers_id_sticker_delete(id, id_sticker)

Delete a custom sticker

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_sticker = 'id_sticker_example' # str | The ID of the custom sticker to delete

try:
    # Delete a custom sticker
    api_instance.members_id_custom_stickers_id_sticker_delete(id, id_sticker)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_stickers_id_sticker_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_sticker** | **str**| The ID of the custom sticker to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_stickers_id_sticker_get**
> members_id_custom_stickers_id_sticker_get(id, id_sticker, fields=fields)

Get an uploaded sticker

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_sticker = 'id_sticker_example' # str | The ID of the uploaded sticker
fields = 'fields_example' # str | all or a comma-separated list of scaled, url (optional)

try:
    # Get an uploaded sticker
    api_instance.members_id_custom_stickers_id_sticker_get(id, id_sticker, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_stickers_id_sticker_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_sticker** | **str**| The ID of the uploaded sticker | 
 **fields** | **str**| all or a comma-separated list of scaled, url | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_custom_stickers_post**
> members_id_custom_stickers_post(id, file)

Upload a new custom sticker

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
file = 'file_example' # str | 

try:
    # Upload a new custom sticker
    api_instance.members_id_custom_stickers_post(id, file)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_custom_stickers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_enterprises_get**
> members_id_enterprises_get(id, id_sticker, fields=fields)

Get the enterprises that a member belongs to.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_sticker = 'id_sticker_example' # str | The ID of the uploaded sticker
fields = 'fields_example' # str | all or a comma-separated list of scaled, url (optional)

try:
    # Get the enterprises that a member belongs to.
    api_instance.members_id_enterprises_get(id, id_sticker, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_enterprises_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_sticker** | **str**| The ID of the uploaded sticker | 
 **fields** | **str**| all or a comma-separated list of scaled, url | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_field_get**
> members_id_field_get(id, field)

Get a particular property of a member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
field = 'field_example' # str | One of the member fields

try:
    # Get a particular property of a member
    api_instance.members_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **field** | **str**| One of the member fields | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_get**
> members_id_get(id, actions=actions, boards=boards, board_backgrounds=board_backgrounds, boards_invited=boards_invited, boards_invited_fields=boards_invited_fields, board_stars=board_stars, cards=cards, custom_board_backgrounds=custom_board_backgrounds, custom_emoji=custom_emoji, custom_stickers=custom_stickers, fields=fields, notifications=notifications, organizations=organizations, organization_fields=organization_fields, organization_paid_account=organization_paid_account, organizations_invited=organizations_invited, organizations_invited_fields=organizations_invited_fields, paid_account=paid_account, saved_searches=saved_searches, tokens=tokens)

Get a member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
actions = 'actions_example' # str | See the Actions Nested Resource (optional)
boards = 'boards_example' # str | See the Boards Nested Resource (optional)
board_backgrounds = 'board_backgrounds_example' # str | One of: all, custom, default, none, premium (optional)
boards_invited = 'boards_invited_example' # str | all or a comma-separated list of: closed, members, open, organization, pinned, public, starred, unpinned (optional)
boards_invited_fields = 'boards_invited_fields_example' # str | all or a comma-separated list of board fields (optional)
board_stars = 'board_stars_example' # str |  (optional)
cards = 'cards_example' # str | See the Cards Nested Resource for additional options (optional)
custom_board_backgrounds = 'custom_board_backgrounds_example' # str | all or none (optional)
custom_emoji = 'custom_emoji_example' # str | all or none (optional)
custom_stickers = 'custom_stickers_example' # str | all or none (optional)
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)
notifications = 'notifications_example' # str | See the Notifications Nested Resource (optional)
organizations = 'organizations_example' # str | One of: all, members, none, public (optional)
organization_fields = 'organization_fields_example' # str | all or a comma-separated list of organization fields (optional)
organization_paid_account = 'organization_paid_account_example' # str |  (optional)
organizations_invited = 'organizations_invited_example' # str | One of: all, members, none, public (optional)
organizations_invited_fields = 'organizations_invited_fields_example' # str | all or a comma-separated list of organization fields (optional)
paid_account = 'paid_account_example' # str |  (optional)
saved_searches = 'saved_searches_example' # str |  (optional)
tokens = 'tokens_example' # str | all or none (optional)

try:
    # Get a member
    api_instance.members_id_get(id, actions=actions, boards=boards, board_backgrounds=board_backgrounds, boards_invited=boards_invited, boards_invited_fields=boards_invited_fields, board_stars=board_stars, cards=cards, custom_board_backgrounds=custom_board_backgrounds, custom_emoji=custom_emoji, custom_stickers=custom_stickers, fields=fields, notifications=notifications, organizations=organizations, organization_fields=organization_fields, organization_paid_account=organization_paid_account, organizations_invited=organizations_invited, organizations_invited_fields=organizations_invited_fields, paid_account=paid_account, saved_searches=saved_searches, tokens=tokens)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **actions** | **str**| See the Actions Nested Resource | [optional] 
 **boards** | **str**| See the Boards Nested Resource | [optional] 
 **board_backgrounds** | **str**| One of: all, custom, default, none, premium | [optional] 
 **boards_invited** | **str**| all or a comma-separated list of: closed, members, open, organization, pinned, public, starred, unpinned | [optional] 
 **boards_invited_fields** | **str**| all or a comma-separated list of board fields | [optional] 
 **board_stars** | **str**|  | [optional] 
 **cards** | **str**| See the Cards Nested Resource for additional options | [optional] 
 **custom_board_backgrounds** | **str**| all or none | [optional] 
 **custom_emoji** | **str**| all or none | [optional] 
 **custom_stickers** | **str**| all or none | [optional] 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 
 **notifications** | **str**| See the Notifications Nested Resource | [optional] 
 **organizations** | **str**| One of: all, members, none, public | [optional] 
 **organization_fields** | **str**| all or a comma-separated list of organization fields | [optional] 
 **organization_paid_account** | **str**|  | [optional] 
 **organizations_invited** | **str**| One of: all, members, none, public | [optional] 
 **organizations_invited_fields** | **str**| all or a comma-separated list of organization fields | [optional] 
 **paid_account** | **str**|  | [optional] 
 **saved_searches** | **str**|  | [optional] 
 **tokens** | **str**| all or none | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_notifications_get**
> members_id_notifications_get(id, entities=entities, display=display, filter=filter, read_filter=read_filter, fields=fields, limit=limit, page=page, before=before, since=since, member_creator=member_creator, member_creator_fields=member_creator_fields)

Get a member's notifications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
entities = 'entities_example' # str |  (optional)
display = 'display_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
read_filter = 'read_filter_example' # str | One of: all, read, unread (optional)
fields = 'fields_example' # str | all or a comma-separated list of notification fields (optional)
limit = 'limit_example' # str | Max 1000 (optional)
page = 'page_example' # str | Max 100 (optional)
before = 'before_example' # str | A notification ID (optional)
since = 'since_example' # str | A notification ID (optional)
member_creator = 'member_creator_example' # str |  (optional)
member_creator_fields = 'member_creator_fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Get a member's notifications
    api_instance.members_id_notifications_get(id, entities=entities, display=display, filter=filter, read_filter=read_filter, fields=fields, limit=limit, page=page, before=before, since=since, member_creator=member_creator, member_creator_fields=member_creator_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_notifications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **entities** | **str**|  | [optional] 
 **display** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **read_filter** | **str**| One of: all, read, unread | [optional] 
 **fields** | **str**| all or a comma-separated list of notification fields | [optional] 
 **limit** | **str**| Max 1000 | [optional] 
 **page** | **str**| Max 100 | [optional] 
 **before** | **str**| A notification ID | [optional] 
 **since** | **str**| A notification ID | [optional] 
 **member_creator** | **str**|  | [optional] 
 **member_creator_fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_one_time_messages_dismissed_post**
> members_id_one_time_messages_dismissed_post(id, value)

Dismiss a message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
value = 'value_example' # str | The message to dismiss

try:
    # Dismiss a message
    api_instance.members_id_one_time_messages_dismissed_post(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_one_time_messages_dismissed_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **value** | **str**| The message to dismiss | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_organizations_get**
> members_id_organizations_get(id, filter=filter, fields=fields, paid_account=paid_account)

Get a member's teams

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
filter = 'filter_example' # str | One of: all, members, none, public (Note: members filters to only private teams) (optional)
fields = 'fields_example' # str | all or a comma-separated list of organization fields (optional)
paid_account = 'paid_account_example' # str |  (optional)

try:
    # Get a member's teams
    api_instance.members_id_organizations_get(id, filter=filter, fields=fields, paid_account=paid_account)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **filter** | **str**| One of: all, members, none, public (Note: members filters to only private teams) | [optional] 
 **fields** | **str**| all or a comma-separated list of organization fields | [optional] 
 **paid_account** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_organizations_invited_get**
> members_id_organizations_invited_get(id, fields=fields)

Get a member's teams they have been invited to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
fields = 'fields_example' # str | all or a comma-separated list of organization fields (optional)

try:
    # Get a member's teams they have been invited to
    api_instance.members_id_organizations_invited_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_organizations_invited_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **fields** | **str**| all or a comma-separated list of organization fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_put**
> members_id_put(id, full_name=full_name, initials=initials, username=username, bio=bio, avatar_source=avatar_source, prefscolor_blind=prefscolor_blind, prefslocale=prefslocale, prefsminutes_between_summaries=prefsminutes_between_summaries)

Update a member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
full_name = 'full_name_example' # str | New name for the member. Cannot begin or end with a space. (optional)
initials = 'initials_example' # str | New initials for the member. 1-4 characters long. (optional)
username = 'username_example' # str | New username for the member. At least 3 characters long, only lowercase letters, underscores, and numbers. Must be unique. (optional)
bio = 'bio_example' # str |  (optional)
avatar_source = 'avatar_source_example' # str | One of: gravatar, none, upload (optional)
prefscolor_blind = 'prefscolor_blind_example' # str |  (optional)
prefslocale = 'prefslocale_example' # str |  (optional)
prefsminutes_between_summaries = 'prefsminutes_between_summaries_example' # str | -1 for disabled, 1, or 60 (optional)

try:
    # Update a member
    api_instance.members_id_put(id, full_name=full_name, initials=initials, username=username, bio=bio, avatar_source=avatar_source, prefscolor_blind=prefscolor_blind, prefslocale=prefslocale, prefsminutes_between_summaries=prefsminutes_between_summaries)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **full_name** | **str**| New name for the member. Cannot begin or end with a space. | [optional] 
 **initials** | **str**| New initials for the member. 1-4 characters long. | [optional] 
 **username** | **str**| New username for the member. At least 3 characters long, only lowercase letters, underscores, and numbers. Must be unique. | [optional] 
 **bio** | **str**|  | [optional] 
 **avatar_source** | **str**| One of: gravatar, none, upload | [optional] 
 **prefscolor_blind** | **str**|  | [optional] 
 **prefslocale** | **str**|  | [optional] 
 **prefsminutes_between_summaries** | **str**| -1 for disabled, 1, or 60 | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_saved_searches_get**
> members_id_saved_searches_get(id)

List the saved searches of a member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member

try:
    # List the saved searches of a member
    api_instance.members_id_saved_searches_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_saved_searches_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_saved_searches_id_search_delete**
> members_id_saved_searches_id_search_delete(id, id_search)

Delete a saved search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_search = 'id_search_example' # str | The ID of the saved search to delete

try:
    # Delete a saved search
    api_instance.members_id_saved_searches_id_search_delete(id, id_search)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_saved_searches_id_search_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_search** | **str**| The ID of the saved search to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_saved_searches_id_search_get**
> members_id_saved_searches_id_search_get(id)

Get a saved search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member

try:
    # Get a saved search
    api_instance.members_id_saved_searches_id_search_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_saved_searches_id_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_saved_searches_id_search_put**
> members_id_saved_searches_id_search_put(id, name=name, query=query, pos=pos)

Update a saved search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
name = 'name_example' # str | The new name for the saved search (optional)
query = 'query_example' # str | The new search query (optional)
pos = 'pos_example' # str | New position for saves search. top, bottom, or a positive float. (optional)

try:
    # Update a saved search
    api_instance.members_id_saved_searches_id_search_put(id, name=name, query=query, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_saved_searches_id_search_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **name** | **str**| The new name for the saved search | [optional] 
 **query** | **str**| The new search query | [optional] 
 **pos** | **str**| New position for saves search. top, bottom, or a positive float. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_saved_searches_post**
> members_id_saved_searches_post(id, name, query, pos)

Create a new saved search

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
name = 'name_example' # str | The name for the saved search
query = 'query_example' # str | The search query
pos = 'pos_example' # str | The position of the saved search. top, bottom, or a positive float.

try:
    # Create a new saved search
    api_instance.members_id_saved_searches_post(id, name, query, pos)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_saved_searches_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **name** | **str**| The name for the saved search | 
 **query** | **str**| The search query | 
 **pos** | **str**| The position of the saved search. top, bottom, or a positive float. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **members_id_tokens_get**
> members_id_tokens_get(id, webhooks=webhooks)

List a members app tokens

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
webhooks = 'webhooks_example' # str | Whether to include webhooks (optional)

try:
    # List a members app tokens
    api_instance.members_id_tokens_get(id, webhooks=webhooks)
except ApiException as e:
    print("Exception when calling DefaultApi->members_id_tokens_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **webhooks** | **str**| Whether to include webhooks | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_all_read_post**
> notifications_all_read_post()

Mark all notifications as read

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Mark all notifications as read
    api_instance.notifications_all_read_post()
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_all_read_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_board_get**
> notifications_id_board_get(id, fields=fields)

Get the board a notification is associated with

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
fields = 'fields_example' # str | all or a comma-separated list of boardfields (optional)

try:
    # Get the board a notification is associated with
    api_instance.notifications_id_board_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_board_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **fields** | **str**| all or a comma-separated list of boardfields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_card_get**
> notifications_id_card_get(id, fields=fields)

Get the card a notification is associated with

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
fields = 'fields_example' # str | all or a comma-separated list of card fields (optional)

try:
    # Get the card a notification is associated with
    api_instance.notifications_id_card_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_card_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **fields** | **str**| all or a comma-separated list of card fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_field_get**
> notifications_id_field_get(id, field)

Get a specific property of a notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
field = 'field_example' # str | A notification field

try:
    # Get a specific property of a notification
    api_instance.notifications_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **field** | **str**| A notification field | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_get**
> notifications_id_get(id, board=board, board_fields=board_fields, card=card, card_fields=card_fields, display=display, entities=entities, fields=fields, list=list, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, organization=organization, organization_fields=organization_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
board = 'board_example' # str | Whether to include the board object (optional)
board_fields = 'board_fields_example' # str | all or a comma-separated list of board fields (optional)
card = 'card_example' # str | Whether to include the card object (optional)
card_fields = 'card_fields_example' # str | all or a comma-separated list of card fields (optional)
display = 'display_example' # str | Whether to include the display object with the results (optional)
entities = 'entities_example' # str | Whether to include the entities object with the results (optional)
fields = 'fields_example' # str | all or a comma-separated list of notification fields (optional)
list = 'list_example' # str | Whether to include the list object (optional)
member = 'member_example' # str | Whether to include the member object (optional)
member_fields = 'member_fields_example' # str | all or a comma-separated list of member fields (optional)
member_creator = 'member_creator_example' # str | Whether to include the member object of the creator (optional)
member_creator_fields = 'member_creator_fields_example' # str | all or a comma-separated list of member fields (optional)
organization = 'organization_example' # str | Whether to include the organization object (optional)
organization_fields = 'organization_fields_example' # str | all or a comma-separated list of organization fields (optional)

try:
    api_instance.notifications_id_get(id, board=board, board_fields=board_fields, card=card, card_fields=card_fields, display=display, entities=entities, fields=fields, list=list, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, organization=organization, organization_fields=organization_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **board** | **str**| Whether to include the board object | [optional] 
 **board_fields** | **str**| all or a comma-separated list of board fields | [optional] 
 **card** | **str**| Whether to include the card object | [optional] 
 **card_fields** | **str**| all or a comma-separated list of card fields | [optional] 
 **display** | **str**| Whether to include the display object with the results | [optional] 
 **entities** | **str**| Whether to include the entities object with the results | [optional] 
 **fields** | **str**| all or a comma-separated list of notification fields | [optional] 
 **list** | **str**| Whether to include the list object | [optional] 
 **member** | **str**| Whether to include the member object | [optional] 
 **member_fields** | **str**| all or a comma-separated list of member fields | [optional] 
 **member_creator** | **str**| Whether to include the member object of the creator | [optional] 
 **member_creator_fields** | **str**| all or a comma-separated list of member fields | [optional] 
 **organization** | **str**| Whether to include the organization object | [optional] 
 **organization_fields** | **str**| all or a comma-separated list of organization fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_list_get**
> notifications_id_list_get(id, fields=fields)

Get the list a notification is associated with

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
fields = 'fields_example' # str | all or a comma-separated list of list fields (optional)

try:
    # Get the list a notification is associated with
    api_instance.notifications_id_list_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **fields** | **str**| all or a comma-separated list of list fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_member_creator_get**
> notifications_id_member_creator_get(id, fields=fields)

Get the member who created the notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Get the member who created the notification
    api_instance.notifications_id_member_creator_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_member_creator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_member_get**
> notifications_id_member_get(id, fields=fields)

Get the member (not the creator) a notification is about

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # Get the member (not the creator) a notification is about
    api_instance.notifications_id_member_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_organization_get**
> notifications_id_organization_get(id, fields=fields)

Get the organization a notification is associated with

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
fields = 'fields_example' # str | all or a comma-separated list of organization fields (optional)

try:
    # Get the organization a notification is associated with
    api_instance.notifications_id_organization_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_organization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **fields** | **str**| all or a comma-separated list of organization fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_put**
> notifications_id_put(id, unread=unread)

Update the read status of a notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
unread = 'unread_example' # str |  (optional)

try:
    # Update the read status of a notification
    api_instance.notifications_id_put(id, unread=unread)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **unread** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_id_unread_put**
> notifications_id_unread_put(id, value=value)

Update the read status of a notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the notification
value = 'value_example' # str |  (optional)

try:
    # Update the read status of a notification
    api_instance.notifications_id_unread_put(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_id_unread_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the notification | 
 **value** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_actions_get**
> organizations_id_actions_get(id)

List the actions on a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # List the actions on a team
    api_instance.organizations_id_actions_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_boards_get**
> organizations_id_boards_get(id, filter=filter, fields=fields)

List the boards in a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
filter = 'filter_example' # str | all or a comma-separated list of: open, closed, members, organization, public (optional)
fields = 'fields_example' # str | all or a comma-separated list of board fields (optional)

try:
    # List the boards in a team
    api_instance.organizations_id_boards_get(id, filter=filter, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_boards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **filter** | **str**| all or a comma-separated list of: open, closed, members, organization, public | [optional] 
 **fields** | **str**| all or a comma-separated list of board fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_delete**
> organizations_id_delete(id)

Delete a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # Delete a team
    api_instance.organizations_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_exports_get**
> organizations_id_exports_get(id)

Retrieve the exports that exist for the given organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # Retrieve the exports that exist for the given organization
    api_instance.organizations_id_exports_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_exports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_exports_post**
> organizations_id_exports_post(id, attachments=attachments)

Kick off CSV export for an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the team
attachments = 'attachments_example' # str | Whether the CSV should include attachments or not. (optional)

try:
    # Kick off CSV export for an organization
    api_instance.organizations_id_exports_post(id, attachments=attachments)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_exports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the team | 
 **attachments** | **str**| Whether the CSV should include attachments or not. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_field_get**
> organizations_id_field_get(id, field)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
field = 'field_example' # str | An organization field

try:
    api_instance.organizations_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **field** | **str**| An organization field | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_get**
> organizations_id_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    api_instance.organizations_id_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_logo_delete**
> organizations_id_logo_delete(id)

Delete a the logo from a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # Delete a the logo from a team
    api_instance.organizations_id_logo_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_logo_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_logo_post**
> organizations_id_logo_post(id, file=file)

Set the logo image for a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the team
file = 'file_example' # str | Image file for the logo (optional)

try:
    # Set the logo image for a team
    api_instance.organizations_id_logo_post(id, file=file)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_logo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the team | 
 **file** | **str**| Image file for the logo | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_filter_get**
> organizations_id_members_filter_get(id, filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
filter = 'filter_example' # str | One of: all, admins, normal

try:
    api_instance.organizations_id_members_filter_get(id, filter)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_filter_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **filter** | **str**| One of: all, admins, normal | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_get**
> organizations_id_members_get(id)

List the members in a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # List the members in a team
    api_instance.organizations_id_members_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_id_member_all_delete**
> organizations_id_members_id_member_all_delete(id, id_member)

Remove a member from a team and from all team boards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_member = 'id_member_example' # str | The ID of the member to remove from the team

try:
    # Remove a member from a team and from all team boards
    api_instance.organizations_id_members_id_member_all_delete(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_id_member_all_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_member** | **str**| The ID of the member to remove from the team | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_id_member_deactivated_put**
> organizations_id_members_id_member_deactivated_put(id, id_member, value=value)

Deactivate or reactivate a member of a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_member = 'id_member_example' # str | The ID or username of the member to update
value = 'value_example' # str |  (optional)

try:
    # Deactivate or reactivate a member of a team
    api_instance.organizations_id_members_id_member_deactivated_put(id, id_member, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_id_member_deactivated_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_member** | **str**| The ID or username of the member to update | 
 **value** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_id_member_delete**
> organizations_id_members_id_member_delete(id, id_member)

Remove a member from a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_member = 'id_member_example' # str | The ID of the member to remove from the team

try:
    # Remove a member from a team
    api_instance.organizations_id_members_id_member_delete(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_id_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_member** | **str**| The ID of the member to remove from the team | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_id_member_put**
> organizations_id_members_id_member_put(id, id_member, type)

Add a member to a team or update their member type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_member = 'id_member_example' # str | The ID or username of the member to update
type = 'type_example' # str | One of: admin, normal

try:
    # Add a member to a team or update their member type.
    api_instance.organizations_id_members_id_member_put(id, id_member, type)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_id_member_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_member** | **str**| The ID or username of the member to update | 
 **type** | **str**| One of: admin, normal | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_invited_get**
> organizations_id_members_invited_get(id, fields=fields)

List the members with pending invites to a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
fields = 'fields_example' # str | all or a comma-separated list of member fields (optional)

try:
    # List the members with pending invites to a team
    api_instance.organizations_id_members_invited_get(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_invited_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **fields** | **str**| all or a comma-separated list of member fields | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_put**
> organizations_id_members_put(id, email, full_name, type=type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
email = 'email_example' # str | An email address
full_name = 'full_name_example' # str | Name for the member, at least 1 character not beginning or ending with a space
type = 'type_example' # str | One of: admin, normal (optional)

try:
    api_instance.organizations_id_members_put(id, email, full_name, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **email** | **str**| An email address | 
 **full_name** | **str**| Name for the member, at least 1 character not beginning or ending with a space | 
 **type** | **str**| One of: admin, normal | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_memberships_get**
> organizations_id_memberships_get(id, filter=filter, member=member)

List the memberships of a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
filter = 'filter_example' # str | all or a comma-separated list of: active, admin, deactivated, me, normal (optional)
member = 'member_example' # str | Whether to include the member objects with the memberships (optional)

try:
    # List the memberships of a team
    api_instance.organizations_id_memberships_get(id, filter=filter, member=member)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_memberships_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **filter** | **str**| all or a comma-separated list of: active, admin, deactivated, me, normal | [optional] 
 **member** | **str**| Whether to include the member objects with the memberships | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_memberships_id_membership_get**
> organizations_id_memberships_id_membership_get(id, id_membership, member=member)

List the memberships of a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_membership = 'id_membership_example' # str | The ID of the membership to load
member = 'member_example' # str | Whether to include the member object in the response (optional)

try:
    # List the memberships of a team
    api_instance.organizations_id_memberships_id_membership_get(id, id_membership, member=member)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_memberships_id_membership_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_membership** | **str**| The ID of the membership to load | 
 **member** | **str**| Whether to include the member object in the response | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_new_billable_guests_id_board_get**
> organizations_id_new_billable_guests_id_board_get(id, id_board)

Used to check whether the given board has new billable guests on it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_board = 'id_board_example' # str | The ID of the board to check for new billable guests.

try:
    # Used to check whether the given board has new billable guests on it.
    api_instance.organizations_id_new_billable_guests_id_board_get(id, id_board)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_new_billable_guests_id_board_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_board** | **str**| The ID of the board to check for new billable guests. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_plugin_data_get**
> organizations_id_plugin_data_get(id)

Get organization scoped pluginData on this team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # Get organization scoped pluginData on this team
    api_instance.organizations_id_plugin_data_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_plugin_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_prefs_associated_domain_delete**
> organizations_id_prefs_associated_domain_delete(id)

Remove the associated Google Apps domain from a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # Remove the associated Google Apps domain from a team
    api_instance.organizations_id_prefs_associated_domain_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_prefs_associated_domain_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_prefs_org_invite_restrict_delete**
> organizations_id_prefs_org_invite_restrict_delete(id)

Remove the email domain restriction on who can be invited to the team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # Remove the email domain restriction on who can be invited to the team
    api_instance.organizations_id_prefs_org_invite_restrict_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_prefs_org_invite_restrict_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_put**
> organizations_id_put(id, name=name, display_name=display_name, desc=desc, website=website, prefsassociated_domain=prefsassociated_domain, prefsexternal_members_disabled=prefsexternal_members_disabled, prefsgoogle_apps_version=prefsgoogle_apps_version, prefsboard_visibility_restrictorg=prefsboard_visibility_restrictorg, prefsboard_visibility_restrictprivate=prefsboard_visibility_restrictprivate, prefsboard_visibility_restrictpublic=prefsboard_visibility_restrictpublic, prefsorg_invite_restrict=prefsorg_invite_restrict, prefspermission_level=prefspermission_level)

Update an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The id or name of the organization to update
name = 'name_example' # str | A new name for the organization. At least 3 lowercase letters, underscores, and numbers. Must be unique (optional)
display_name = 'display_name_example' # str | A new displayName for the organization. Must be at least 1 character long and not begin or end with a space. (optional)
desc = 'desc_example' # str | A new description for the organization (optional)
website = 'website_example' # str | A URL starting with http://, https://, or null (optional)
prefsassociated_domain = 'prefsassociated_domain_example' # str | The Google Apps domain to link this org to. (optional)
prefsexternal_members_disabled = 'prefsexternal_members_disabled_example' # str | Whether non-team members can be added to boards inside the team (optional)
prefsgoogle_apps_version = 'prefsgoogle_apps_version_example' # str | 1 or 2 (optional)
prefsboard_visibility_restrictorg = 'prefsboard_visibility_restrictorg_example' # str | Who on the team can make team visible boards. One of admin, none, org (optional)
prefsboard_visibility_restrictprivate = 'prefsboard_visibility_restrictprivate_example' # str | Who can make private boards. One of: admin, none, org (optional)
prefsboard_visibility_restrictpublic = 'prefsboard_visibility_restrictpublic_example' # str | Who on the team can make public boards. One of: admin, none, org (optional)
prefsorg_invite_restrict = 'prefsorg_invite_restrict_example' # str | An email address with optional wildcard characters. (E.g. subdomain.*.trello.com) (optional)
prefspermission_level = 'prefspermission_level_example' # str | Whether the team page is publicly visible. One of: private, public (optional)

try:
    # Update an organization
    api_instance.organizations_id_put(id, name=name, display_name=display_name, desc=desc, website=website, prefsassociated_domain=prefsassociated_domain, prefsexternal_members_disabled=prefsexternal_members_disabled, prefsgoogle_apps_version=prefsgoogle_apps_version, prefsboard_visibility_restrictorg=prefsboard_visibility_restrictorg, prefsboard_visibility_restrictprivate=prefsboard_visibility_restrictprivate, prefsboard_visibility_restrictpublic=prefsboard_visibility_restrictpublic, prefsorg_invite_restrict=prefsorg_invite_restrict, prefspermission_level=prefspermission_level)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id or name of the organization to update | 
 **name** | **str**| A new name for the organization. At least 3 lowercase letters, underscores, and numbers. Must be unique | [optional] 
 **display_name** | **str**| A new displayName for the organization. Must be at least 1 character long and not begin or end with a space. | [optional] 
 **desc** | **str**| A new description for the organization | [optional] 
 **website** | **str**| A URL starting with http://, https://, or null | [optional] 
 **prefsassociated_domain** | **str**| The Google Apps domain to link this org to. | [optional] 
 **prefsexternal_members_disabled** | **str**| Whether non-team members can be added to boards inside the team | [optional] 
 **prefsgoogle_apps_version** | **str**| 1 or 2 | [optional] 
 **prefsboard_visibility_restrictorg** | **str**| Who on the team can make team visible boards. One of admin, none, org | [optional] 
 **prefsboard_visibility_restrictprivate** | **str**| Who can make private boards. One of: admin, none, org | [optional] 
 **prefsboard_visibility_restrictpublic** | **str**| Who on the team can make public boards. One of: admin, none, org | [optional] 
 **prefsorg_invite_restrict** | **str**| An email address with optional wildcard characters. (E.g. subdomain.*.trello.com) | [optional] 
 **prefspermission_level** | **str**| Whether the team page is publicly visible. One of: private, public | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tags_get**
> organizations_id_tags_get(id)

List the organization's collections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization

try:
    # List the organization's collections
    api_instance.organizations_id_tags_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tags_id_tag_delete**
> organizations_id_tags_id_tag_delete(id, id_tag)

Delete an organization's tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_tag = 'id_tag_example' # str | The ID of the tag to delete

try:
    # Delete an organization's tag
    api_instance.organizations_id_tags_id_tag_delete(id, id_tag)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_tags_id_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_tag** | **str**| The ID of the tag to delete | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_tags_post**
> organizations_id_tags_post(id, name)

Create a new collection in a team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the team
name = 'name_example' # str | The name for the new collection

try:
    # Create a new collection in a team
    api_instance.organizations_id_tags_post(id, name)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the team | 
 **name** | **str**| The name for the new collection | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_post**
> organizations_post(display_name, desc=desc, name=name, website=website)

Create a new team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
display_name = 'display_name_example' # str | 
desc = 'desc_example' # str | The description for the team (optional)
name = 'name_example' # str | A string with a length of at least 3. Only lowercase letters, underscores, and numbers are allowed. Must be unique. (optional)
website = 'website_example' # str | A URL starting with http:// or https:// (optional)

try:
    # Create a new team
    api_instance.organizations_post(display_name, desc=desc, name=name, website=website)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**|  | 
 **desc** | **str**| The description for the team | [optional] 
 **name** | **str**| A string with a length of at least 3. Only lowercase letters, underscores, and numbers are allowed. Must be unique. | [optional] 
 **website** | **str**| A URL starting with http:// or https:// | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_get**
> search_get(query, id_boards=id_boards, id_organizations=id_organizations, id_cards=id_cards, model_types=model_types, board_fields=board_fields, boards_limit=boards_limit, card_fields=card_fields, cards_limit=cards_limit, cards_page=cards_page, card_board=card_board, card_list=card_list, card_members=card_members, card_stickers=card_stickers, card_attachments=card_attachments, organization_fields=organization_fields, organizations_limit=organizations_limit, member_fields=member_fields, members_limit=members_limit, partial=partial)

Find what you're looking for in Trello

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | The search query with a length of 1 to 16384 characters
id_boards = 'id_boards_example' # str | mine or a comma-separated list of board ids (optional)
id_organizations = 'id_organizations_example' # str | A comma-separated list of team ids (optional)
id_cards = 'id_cards_example' # str | A comma-separated list of card ids (optional)
model_types = 'model_types_example' # str | What type or types of Trello objects you want to search. all or a comma-separated list of: actions, boards, cards, members, organizations (optional)
board_fields = 'board_fields_example' # str | all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url (optional)
boards_limit = 'boards_limit_example' # str | The maximum number of boards returned. Maximum: 1000 (optional)
card_fields = 'card_fields_example' # str | all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed, url (optional)
cards_limit = 'cards_limit_example' # str | The maximum number of cards to return. Maximum: 1000 (optional)
cards_page = 'cards_page_example' # str | The page of results for cards. Maximum: 100 (optional)
card_board = 'card_board_example' # str | Whether to include the parent board with card results (optional)
card_list = 'card_list_example' # str | Whether to include the parent list with card results (optional)
card_members = 'card_members_example' # str | Whether to include member objects with card results (optional)
card_stickers = 'card_stickers_example' # str | Whether to include sticker objects with card results (optional)
card_attachments = 'card_attachments_example' # str | Whether to include attachment objects with card results. A boolean value (true or false) or cover for only card cover attachments. (optional)
organization_fields = 'organization_fields_example' # str | all or a comma-separated list of billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url, website (optional)
organizations_limit = 'organizations_limit_example' # str | The maximum number of teams to return. Maximum 1000 (optional)
member_fields = 'member_fields_example' # str | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username (optional)
members_limit = 'members_limit_example' # str | The maximum number of members to return. Maximum 1000 (optional)
partial = 'partial_example' # str | By default, Trello searches for each word in your query against exactly matching words within Member content. Specifying partial to be true means that we will look for content that starts with any of the words in your query.  If you are looking for a Card titled \"My Development Status Report\", by default you would need to search for \"Development\". If you have partial enabled, you will be able to search for \"dev\" but not \"velopment\". (optional)

try:
    # Find what you're looking for in Trello
    api_instance.search_get(query, id_boards=id_boards, id_organizations=id_organizations, id_cards=id_cards, model_types=model_types, board_fields=board_fields, boards_limit=boards_limit, card_fields=card_fields, cards_limit=cards_limit, cards_page=cards_page, card_board=card_board, card_list=card_list, card_members=card_members, card_stickers=card_stickers, card_attachments=card_attachments, organization_fields=organization_fields, organizations_limit=organizations_limit, member_fields=member_fields, members_limit=members_limit, partial=partial)
except ApiException as e:
    print("Exception when calling DefaultApi->search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query with a length of 1 to 16384 characters | 
 **id_boards** | **str**| mine or a comma-separated list of board ids | [optional] 
 **id_organizations** | **str**| A comma-separated list of team ids | [optional] 
 **id_cards** | **str**| A comma-separated list of card ids | [optional] 
 **model_types** | **str**| What type or types of Trello objects you want to search. all or a comma-separated list of: actions, boards, cards, members, organizations | [optional] 
 **board_fields** | **str**| all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url | [optional] 
 **boards_limit** | **str**| The maximum number of boards returned. Maximum: 1000 | [optional] 
 **card_fields** | **str**| all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed, url | [optional] 
 **cards_limit** | **str**| The maximum number of cards to return. Maximum: 1000 | [optional] 
 **cards_page** | **str**| The page of results for cards. Maximum: 100 | [optional] 
 **card_board** | **str**| Whether to include the parent board with card results | [optional] 
 **card_list** | **str**| Whether to include the parent list with card results | [optional] 
 **card_members** | **str**| Whether to include member objects with card results | [optional] 
 **card_stickers** | **str**| Whether to include sticker objects with card results | [optional] 
 **card_attachments** | **str**| Whether to include attachment objects with card results. A boolean value (true or false) or cover for only card cover attachments. | [optional] 
 **organization_fields** | **str**| all or a comma-separated list of billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url, website | [optional] 
 **organizations_limit** | **str**| The maximum number of teams to return. Maximum 1000 | [optional] 
 **member_fields** | **str**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username | [optional] 
 **members_limit** | **str**| The maximum number of members to return. Maximum 1000 | [optional] 
 **partial** | **str**| By default, Trello searches for each word in your query against exactly matching words within Member content. Specifying partial to be true means that we will look for content that starts with any of the words in your query.  If you are looking for a Card titled \&quot;My Development Status Report\&quot;, by default you would need to search for \&quot;Development\&quot;. If you have partial enabled, you will be able to search for \&quot;dev\&quot; but not \&quot;velopment\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_members_get**
> search_members_get(query, limit=limit, id_board=id_board, id_organization=id_organization, only_org_members=only_org_members)

Search for Trello members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Search query 1 to 16384 characters long
limit = 'limit_example' # str | The maximum number of results to return. Maximum of 20. (optional)
id_board = 'id_board_example' # str |  (optional)
id_organization = 'id_organization_example' # str |  (optional)
only_org_members = 'only_org_members_example' # str |  (optional)

try:
    # Search for Trello members
    api_instance.search_members_get(query, limit=limit, id_board=id_board, id_organization=id_organization, only_org_members=only_org_members)
except ApiException as e:
    print("Exception when calling DefaultApi->search_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query 1 to 16384 characters long | 
 **limit** | **str**| The maximum number of results to return. Maximum of 20. | [optional] 
 **id_board** | **str**|  | [optional] 
 **id_organization** | **str**|  | [optional] 
 **only_org_members** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_delete**
> tokens_token_delete(token)

Delete a token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Delete a token.
    api_instance.tokens_token_delete(token)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_get**
> tokens_token_get(token, fields=fields, webhooks=webhooks)

Retrieve information about a token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
fields = 'fields_example' # str | all or a comma-separated list of dateCreated, dateExpires, idMember, identifier, permissions (optional)
webhooks = 'webhooks_example' # str | Determines whether to include webhooks. (optional)

try:
    # Retrieve information about a token.
    api_instance.tokens_token_get(token, fields=fields, webhooks=webhooks)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **fields** | **str**| all or a comma-separated list of dateCreated, dateExpires, idMember, identifier, permissions | [optional] 
 **webhooks** | **str**| Determines whether to include webhooks. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_member_get**
> tokens_token_member_get(token, fields=fields)

Retrieve information about a token's owner by token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
fields = 'fields_example' # str | all or a comma-separated list of valid fields for Member Object. (optional)

try:
    # Retrieve information about a token's owner by token.
    api_instance.tokens_token_member_get(token, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_member_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **fields** | **str**| all or a comma-separated list of valid fields for Member Object. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_webhooks_get**
> tokens_token_webhooks_get(token)

Retrieve all webhooks created with a token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Retrieve all webhooks created with a token.
    api_instance.tokens_token_webhooks_get(token)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_webhooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_webhooks_id_webhook_delete**
> tokens_token_webhooks_id_webhook_delete(token, id_webhook)

Delete a webhook created with given token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
id_webhook = 'id_webhook_example' # str | ID of the webhook to delete.

try:
    # Delete a webhook created with given token.
    api_instance.tokens_token_webhooks_id_webhook_delete(token, id_webhook)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_webhooks_id_webhook_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **id_webhook** | **str**| ID of the webhook to delete. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_webhooks_id_webhook_get**
> tokens_token_webhooks_id_webhook_get(token, id_webhook)

Retrieve a webhook created with a token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
id_webhook = 'id_webhook_example' # str | ID of the Webhooks to retrieve.

try:
    # Retrieve a webhook created with a token.
    api_instance.tokens_token_webhooks_id_webhook_get(token, id_webhook)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_webhooks_id_webhook_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **id_webhook** | **str**| ID of the Webhooks to retrieve. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_webhooks_post**
> tokens_token_webhooks_post(token, callback_url, id_model, description=description)

Create a new webhook for a token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
callback_url = 'callback_url_example' # str | The URL that the webhook should POST information to.
id_model = 'id_model_example' # str | ID of the object to create a webhook on.
description = 'description_example' # str | A description to be displayed when retrieving information about the webhook. (optional)

try:
    # Create a new webhook for a token.
    api_instance.tokens_token_webhooks_post(token, callback_url, id_model, description=description)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_webhooks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **callback_url** | **str**| The URL that the webhook should POST information to. | 
 **id_model** | **str**| ID of the object to create a webhook on. | 
 **description** | **str**| A description to be displayed when retrieving information about the webhook. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokens_token_webhooks_webhook_id_put**
> tokens_token_webhooks_webhook_id_put(token, webhook_id, callback_url, id_model, description=description)

Update an existing webhook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | The token to which the webhook belongs
webhook_id = 'webhook_id_example' # str | ID of the webhook to update
callback_url = 'callback_url_example' # str | The URL that the webhook should POST information to.
id_model = 'id_model_example' # str | ID of the object to create a webhook on.
description = 'description_example' # str | A description to be displayed when retrieving information about the webhook. (optional)

try:
    # Update an existing webhook.
    api_instance.tokens_token_webhooks_webhook_id_put(token, webhook_id, callback_url, id_model, description=description)
except ApiException as e:
    print("Exception when calling DefaultApi->tokens_token_webhooks_webhook_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token to which the webhook belongs | 
 **webhook_id** | **str**| ID of the webhook to update | 
 **callback_url** | **str**| The URL that the webhook should POST information to. | 
 **id_model** | **str**| ID of the object to create a webhook on. | 
 **description** | **str**| A description to be displayed when retrieving information about the webhook. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_delete**
> webhooks_id_delete(id)

Delete a webhook by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the webhook to delete.

try:
    # Delete a webhook by ID.
    api_instance.webhooks_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the webhook to delete. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_field_get**
> webhooks_id_field_get(id, field)

Get a webhook's field.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the webhook.
field = 'field_example' # str | Field to retrieve. One of: active, callbackURL, description, idModel

try:
    # Get a webhook's field.
    api_instance.webhooks_id_field_get(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooks_id_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the webhook. | 
 **field** | **str**| Field to retrieve. One of: active, callbackURL, description, idModel | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_get**
> webhooks_id_get(id)

Get a webhook by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the webhook to retrieve.

try:
    # Get a webhook by ID.
    api_instance.webhooks_id_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the webhook to retrieve. | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_put**
> webhooks_id_put(id, description=description, callback_url=callback_url, id_model=id_model, active=active)

Update a webhook by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the webhook to update.
description = 'description_example' # str | A string with a length from 0 to 16384. (optional)
callback_url = 'callback_url_example' # str | A valid URL that is reachable with a HEAD and POST request. (optional)
id_model = 'id_model_example' # str | ID of the model to be monitored (optional)
active = 'active_example' # str | Determines whether the webhook is active and sending POST requests. (optional)

try:
    # Update a webhook by ID.
    api_instance.webhooks_id_put(id, description=description, callback_url=callback_url, id_model=id_model, active=active)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooks_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the webhook to update. | 
 **description** | **str**| A string with a length from 0 to 16384. | [optional] 
 **callback_url** | **str**| A valid URL that is reachable with a HEAD and POST request. | [optional] 
 **id_model** | **str**| ID of the model to be monitored | [optional] 
 **active** | **str**| Determines whether the webhook is active and sending POST requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_post**
> webhooks_post(callback_url, id_model, description=description, active=active)

Create a new webhook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: oauth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
callback_url = 'callback_url_example' # str | A valid URL that is reachable with a HEAD and POST request.
id_model = 'id_model_example' # str | ID of the model to be monitored
description = 'description_example' # str | A string with a length from 0 to 16384. (optional)
active = 'active_example' # str | Determines whether the webhook is active and sending POST requests. (optional)

try:
    # Create a new webhook.
    api_instance.webhooks_post(callback_url, id_model, description=description, active=active)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_url** | **str**| A valid URL that is reachable with a HEAD and POST request. | 
 **id_model** | **str**| ID of the model to be monitored | 
 **description** | **str**| A string with a length from 0 to 16384. | [optional] 
 **active** | **str**| Determines whether the webhook is active and sending POST requests. | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

