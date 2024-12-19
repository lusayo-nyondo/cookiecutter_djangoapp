from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


DASHBOARD_CALLBACK = 'apps.callbacks.branch_deliveries_callback'

SIDEBAR = {
    "show_search": False,
    "show_all_applications": True,
    "navigation": [
        {
            "title": _("Courier Management"),
            "separator": False,  # Top border
            "collapsible": False,  # Collapsible group of links
            "items": [
                {
                    "title": _("Dashboard"),
                    "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                    "link": reverse_lazy("admin:index"),
                    #"badge": "sample_app.badge_callback",
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("Parcels"),
                    "icon": "box",  # Supported icon set: https://fonts.google.com/icons
                    "link": '/admin/deliveries/parcel',
                    #"badge": "sample_app.badge_callback",
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("Internal Deliveries"),
                    "icon": "local_shipping",  # Supported icon set: https://fonts.google.com/icons
                    "link": '/admin/deliveries/internaldelivery',
                    #"badge": "sample_app.badge_callback",
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("Client Deliveries"),
                    "icon": "local_post_office",  # Supported icon set: https://fonts.google.com/icons
                    "link": '/admin/deliveries/clientdelivery',
                    #"badge": "sample_app.badge_callback",
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("Pickups"),
                    "icon": "orders",  # Supported icon set: https://fonts.google.com/icons
                    "link": '/admin/deliveries/pickup',
                    #"badge": "sample_app.badge_callback",
                    "permission": lambda request: request.user.is_superuser,
                },
            ],
        },
        {
            "title": _("Invoices and Reporting"),
            "separator": False,
            "collapsible": False,
            "items": [
                {
                    "title": _("Track Parcel"),
                    "icon": "travel_explore",
                    "link": "/admin/courier_management/track_parcel",
                },
                {
                    "title": _("Invoices"),
                    "icon": "money",
                    "link": "/admin/deliveries/invoice",
                },
                {
                    "title": _("Reports"),
                    "icon": "summarize",
                    "link": "/admin/courier_management/reports"
                },
            ]
        },
        {
            "title": _("Business"),
            "separator": True,
            "collapsible": True,
            "items": [
                {
                    "title": _("Clients"),
                    "icon": "face_4",  # Supported icon set: https://fonts.google.com/icons
                    "link": '/admin/kyc/client',
                    #"badge": "sample_app.badge_callback",
                    "permission": lambda request: request.user.is_superuser,
                },
                {
                    "title": _("Branches"),
                    "icon": "apartment",  # Supported icon set: https://fonts.google.com/icons
                    "link": '/admin/branches/branch',
                    #"badge": "sample_app.badge_callback",
                    "permission": lambda request: request.user.is_superuser,
                },
            ]  
        },
        {
            "title": _("User Management"),
            "separator": False,
            "collapsible": True,
            "items": [
                {
                    "title": _("Users"),
                    "icon": "person",
                    "link": '/admin/auth/user', #reverse_lazy("admin:users_user_changelist"),
                },
                {
                    "title": _("Groups"),
                    "icon": "people",
                    "link": '/admin/auth/group', #reverse_lazy("admin:users_user_changelist"),
                },
                {
                    "title": _("Email Addresses"),
                    "icon": "alternate_email",
                    "link": '/admin/account/emailaddress', #reverse_lazy("admin:users_user_changelist"),
                },
            ]
        }
    ],           
}
