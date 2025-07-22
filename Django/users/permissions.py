from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Allow read only if authenticated.
    Allow write only for admin users.
    """
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        if request.method in SAFE_METHODS:
            return True
        
        return bool(request.user.is_superuser or getattr(request.user, 'role', None) == 'admin')
    