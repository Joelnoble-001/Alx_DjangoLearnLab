from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = 'Setup user groups and assign custom permissions'

    def handle(self, *args, **kwargs):
        Book = apps.get_model('bookshelf', 'Book')

        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"]
        }

        for group_name, perm_codenames in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perm_codenames:
                try:
                    permission = Permission.objects.get(
                        codename=codename,
                        content_type__app_label='bookshelf'
                    )
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Permission '{codename}' not found."))
            self.stdout.write(self.style.SUCCESS(f"{group_name} group created/updated with permissions."))