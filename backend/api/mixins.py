from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class StaffEditorPermissionMixin:
    permission_class = [permissions.IsAdminUser, IsStaffEditorPermission]
