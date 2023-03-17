resource "azurerm_managed_disk" "ifrcgo" {
  name                 = "${local.prefix}-disk"
  resource_group_name      = data.azurerm_resource_group.ifrcgo.name
  location                 = data.azurerm_resource_group.ifrcgo.location
  storage_account_type = "StandardSSD_LRS"
  create_option        = "Empty"
  disk_size_gb         = "20"
}