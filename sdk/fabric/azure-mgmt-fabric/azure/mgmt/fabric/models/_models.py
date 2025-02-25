# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class CapacityAdministration(_model_base.Model):
    """The administration properties of the Fabric capacity resource.


    :ivar members: An array of administrator user identities. Required.
    :vartype members: list[str]
    """

    members: List[str] = rest_field()
    """An array of administrator user identities. Required."""

    @overload
    def __init__(
        self,
        *,
        members: List[str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CheckNameAvailabilityRequest(_model_base.Model):
    """The check availability request body.

    :ivar name: The name of the resource for which availability needs to be checked.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    """

    name: Optional[str] = rest_field()
    """The name of the resource for which availability needs to be checked."""
    type: Optional[str] = rest_field()
    """The resource type."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CheckNameAvailabilityResponse(_model_base.Model):
    """The check availability result.

    :ivar name_available: Indicates if the resource name is available.
    :vartype name_available: bool
    :ivar reason: The reason why the given name is not available. Known values are: "Invalid" and
     "AlreadyExists".
    :vartype reason: str or ~azure.mgmt.fabric.models.CheckNameAvailabilityReason
    :ivar message: Detailed reason why the given name is not available.
    :vartype message: str
    """

    name_available: Optional[bool] = rest_field(name="nameAvailable")
    """Indicates if the resource name is available."""
    reason: Optional[Union[str, "_models.CheckNameAvailabilityReason"]] = rest_field()
    """The reason why the given name is not available. Known values are: \"Invalid\" and
     \"AlreadyExists\"."""
    message: Optional[str] = rest_field()
    """Detailed reason why the given name is not available."""

    @overload
    def __init__(
        self,
        *,
        name_available: Optional[bool] = None,
        reason: Optional[Union[str, "_models.CheckNameAvailabilityReason"]] = None,
        message: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ErrorAdditionalInfo(_model_base.Model):
    """The resource management error additional info.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    type: Optional[str] = rest_field(visibility=["read"])
    """The additional info type."""
    info: Optional[Any] = rest_field(visibility=["read"])
    """The additional info."""


class ErrorDetail(_model_base.Model):
    """The error detail.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.fabric.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.fabric.models.ErrorAdditionalInfo]
    """

    code: Optional[str] = rest_field(visibility=["read"])
    """The error code."""
    message: Optional[str] = rest_field(visibility=["read"])
    """The error message."""
    target: Optional[str] = rest_field(visibility=["read"])
    """The error target."""
    details: Optional[List["_models.ErrorDetail"]] = rest_field(visibility=["read"])
    """The error details."""
    additional_info: Optional[List["_models.ErrorAdditionalInfo"]] = rest_field(
        name="additionalInfo", visibility=["read"]
    )
    """The error additional info."""


class ErrorResponse(_model_base.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations.

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.fabric.models.ErrorDetail
    """

    error: Optional["_models.ErrorDetail"] = rest_field()
    """The error object."""

    @overload
    def __init__(
        self,
        *,
        error: Optional["_models.ErrorDetail"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Resource(_model_base.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.fabric.models.SystemData
    """

    id: Optional[str] = rest_field(visibility=["read"])
    """Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long"""
    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the resource."""
    type: Optional[str] = rest_field(visibility=["read"])
    """The type of the resource. E.g. \"Microsoft.Compute/virtualMachines\" or
     \"Microsoft.Storage/storageAccounts\"."""
    system_data: Optional["_models.SystemData"] = rest_field(name="systemData", visibility=["read"])
    """Azure Resource Manager metadata containing createdBy and modifiedBy information."""


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.fabric.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    tags: Optional[Dict[str, str]] = rest_field()
    """Resource tags."""
    location: str = rest_field(visibility=["read", "create"])
    """The geo-location where the resource lives. Required."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FabricCapacity(TrackedResource):
    """Fabric Capacity resource.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.fabric.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar properties: The resource-specific properties for this resource. Required.
    :vartype properties: ~azure.mgmt.fabric.models.FabricCapacityProperties
    :ivar sku: The SKU details. Required.
    :vartype sku: ~azure.mgmt.fabric.models.RpSku
    """

    properties: "_models.FabricCapacityProperties" = rest_field()
    """The resource-specific properties for this resource. Required."""
    sku: "_models.RpSku" = rest_field()
    """The SKU details. Required."""

    @overload
    def __init__(
        self,
        *,
        location: str,
        properties: "_models.FabricCapacityProperties",
        sku: "_models.RpSku",
        tags: Optional[Dict[str, str]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FabricCapacityProperties(_model_base.Model):
    """The Microsoft Fabric capacity properties.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar provisioning_state: The current deployment state of Microsoft Fabric resource. The
     provisioningState is to indicate states for resource provisioning. Known values are:
     "Succeeded", "Failed", "Canceled", "Deleting", "Provisioning", and "Updating".
    :vartype provisioning_state: str or ~azure.mgmt.fabric.models.ProvisioningState
    :ivar state: The current state of Microsoft Fabric resource. The state is to indicate more
     states outside of resource provisioning. Known values are: "Active", "Provisioning", "Failed",
     "Updating", "Deleting", "Suspending", "Suspended", "Pausing", "Paused", "Resuming", "Scaling",
     and "Preparing".
    :vartype state: str or ~azure.mgmt.fabric.models.ResourceState
    :ivar administration: The capacity administration. Required.
    :vartype administration: ~azure.mgmt.fabric.models.CapacityAdministration
    """

    provisioning_state: Optional[Union[str, "_models.ProvisioningState"]] = rest_field(
        name="provisioningState", visibility=["read"]
    )
    """The current deployment state of Microsoft Fabric resource. The provisioningState is to indicate
     states for resource provisioning. Known values are: \"Succeeded\", \"Failed\", \"Canceled\",
     \"Deleting\", \"Provisioning\", and \"Updating\"."""
    state: Optional[Union[str, "_models.ResourceState"]] = rest_field(visibility=["read"])
    """The current state of Microsoft Fabric resource. The state is to indicate more states outside of
     resource provisioning. Known values are: \"Active\", \"Provisioning\", \"Failed\",
     \"Updating\", \"Deleting\", \"Suspending\", \"Suspended\", \"Pausing\", \"Paused\",
     \"Resuming\", \"Scaling\", and \"Preparing\"."""
    administration: "_models.CapacityAdministration" = rest_field()
    """The capacity administration. Required."""

    @overload
    def __init__(
        self,
        *,
        administration: "_models.CapacityAdministration",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FabricCapacityUpdate(_model_base.Model):
    """The type used for update operations of the FabricCapacity.

    :ivar sku: The SKU details.
    :vartype sku: ~azure.mgmt.fabric.models.RpSku
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar properties: The resource-specific properties for this resource.
    :vartype properties: ~azure.mgmt.fabric.models.FabricCapacityUpdateProperties
    """

    sku: Optional["_models.RpSku"] = rest_field()
    """The SKU details."""
    tags: Optional[Dict[str, str]] = rest_field()
    """Resource tags."""
    properties: Optional["_models.FabricCapacityUpdateProperties"] = rest_field()
    """The resource-specific properties for this resource."""

    @overload
    def __init__(
        self,
        *,
        sku: Optional["_models.RpSku"] = None,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.FabricCapacityUpdateProperties"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FabricCapacityUpdateProperties(_model_base.Model):
    """The updatable properties of the FabricCapacity.

    :ivar administration: The capacity administration.
    :vartype administration: ~azure.mgmt.fabric.models.CapacityAdministration
    """

    administration: Optional["_models.CapacityAdministration"] = rest_field()
    """The capacity administration."""

    @overload
    def __init__(
        self,
        *,
        administration: Optional["_models.CapacityAdministration"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Operation(_model_base.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for Azure Resource Manager/control-plane operations.
    :vartype is_data_action: bool
    :ivar display: Localized display information for this particular operation.
    :vartype display: ~azure.mgmt.fabric.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Known values are: "user", "system",
     and "user,system".
    :vartype origin: str or ~azure.mgmt.fabric.models.Origin
    :ivar action_type: Extensible enum. Indicates the action type. "Internal" refers to actions
     that are for internal only APIs. "Internal"
    :vartype action_type: str or ~azure.mgmt.fabric.models.ActionType
    """

    name: Optional[str] = rest_field(visibility=["read"])
    """The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     \"Microsoft.Compute/virtualMachines/write\",
     \"Microsoft.Compute/virtualMachines/capture/action\"."""
    is_data_action: Optional[bool] = rest_field(name="isDataAction", visibility=["read"])
    """Whether the operation applies to data-plane. This is \"true\" for data-plane operations and
     \"false\" for Azure Resource Manager/control-plane operations."""
    display: Optional["_models.OperationDisplay"] = rest_field(visibility=["read"])
    """Localized display information for this particular operation."""
    origin: Optional[Union[str, "_models.Origin"]] = rest_field(visibility=["read"])
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
     logs UX. Default value is \"user,system\". Known values are: \"user\", \"system\", and
     \"user,system\"."""
    action_type: Optional[Union[str, "_models.ActionType"]] = rest_field(name="actionType")
    """Extensible enum. Indicates the action type. \"Internal\" refers to actions that are for
     internal only APIs. \"Internal\""""

    @overload
    def __init__(
        self,
        *,
        action_type: Optional[Union[str, "_models.ActionType"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OperationDisplay(_model_base.Model):
    """Localized display information for and operation.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    provider: Optional[str] = rest_field(visibility=["read"])
    """The localized friendly form of the resource provider name, e.g. \"Microsoft Monitoring
     Insights\" or \"Microsoft Compute\"."""
    resource: Optional[str] = rest_field(visibility=["read"])
    """The localized friendly name of the resource type related to this operation. E.g. \"Virtual
     Machines\" or \"Job Schedule Collections\"."""
    operation: Optional[str] = rest_field(visibility=["read"])
    """The concise, localized friendly name for the operation; suitable for dropdowns. E.g. \"Create
     or Update Virtual Machine\", \"Restart Virtual Machine\"."""
    description: Optional[str] = rest_field(visibility=["read"])
    """The short, localized friendly description of the operation; suitable for tool tips and detailed
     views."""


class RpSku(_model_base.Model):
    """Represents the SKU name and Azure pricing tier for Microsoft Fabric capacity resource.


    :ivar name: The name of the SKU level. Required.
    :vartype name: str
    :ivar tier: The name of the Azure pricing tier to which the SKU applies. Required. "Fabric"
    :vartype tier: str or ~azure.mgmt.fabric.models.RpSkuTier
    """

    name: str = rest_field()
    """The name of the SKU level. Required."""
    tier: Union[str, "_models.RpSkuTier"] = rest_field()
    """The name of the Azure pricing tier to which the SKU applies. Required. \"Fabric\""""

    @overload
    def __init__(
        self,
        *,
        name: str,
        tier: Union[str, "_models.RpSkuTier"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class RpSkuDetailsForExistingResource(_model_base.Model):
    """An object that represents SKU details for existing resources.


    :ivar resource_type: The resource type. Required.
    :vartype resource_type: str
    :ivar sku: The SKU details. Required.
    :vartype sku: ~azure.mgmt.fabric.models.RpSku
    """

    resource_type: str = rest_field(name="resourceType")
    """The resource type. Required."""
    sku: "_models.RpSku" = rest_field()
    """The SKU details. Required."""

    @overload
    def __init__(
        self,
        *,
        resource_type: str,
        sku: "_models.RpSku",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class RpSkuDetailsForNewResource(_model_base.Model):
    """The SKU details.


    :ivar resource_type: The resource type. Required.
    :vartype resource_type: str
    :ivar name: The SKU's name. Required.
    :vartype name: str
    :ivar locations: The list of available locations for the SKU. Required.
    :vartype locations: list[str]
    """

    resource_type: str = rest_field(name="resourceType")
    """The resource type. Required."""
    name: str = rest_field()
    """The SKU's name. Required."""
    locations: List[str] = rest_field()
    """The list of available locations for the SKU. Required."""

    @overload
    def __init__(
        self,
        *,
        resource_type: str,
        name: str,
        locations: List[str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SystemData(_model_base.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.fabric.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.fabric.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    created_by: Optional[str] = rest_field(name="createdBy")
    """The identity that created the resource."""
    created_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(name="createdByType")
    """The type of identity that created the resource. Known values are: \"User\", \"Application\",
     \"ManagedIdentity\", and \"Key\"."""
    created_at: Optional[datetime.datetime] = rest_field(name="createdAt", format="rfc3339")
    """The timestamp of resource creation (UTC)."""
    last_modified_by: Optional[str] = rest_field(name="lastModifiedBy")
    """The identity that last modified the resource."""
    last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = rest_field(name="lastModifiedByType")
    """The type of identity that last modified the resource. Known values are: \"User\",
     \"Application\", \"ManagedIdentity\", and \"Key\"."""
    last_modified_at: Optional[datetime.datetime] = rest_field(name="lastModifiedAt", format="rfc3339")
    """The timestamp of resource last modification (UTC)."""

    @overload
    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
