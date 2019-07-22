# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erp_test"
app_title = "Erp Testing"
app_publisher = "Kalpit Shah"
app_description = "To test the ERP"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kalpits21@gmail.com"
app_license = "MIT"
# fixtures = ['Custom Field']
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erp_test/css/erp_test.css"
# app_include_js = "/assets/erp_test/js/erp_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/erp_test/css/erp_test.css"
# web_include_js = "/assets/erp_test/js/erp_test.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erp_test.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erp_test.install.before_install"
# after_install = "erp_test.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erp_test.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erp_test.tasks.all"
# 	],
# 	"daily": [
# 		"erp_test.tasks.daily"
# 	],
# 	"hourly": [
# 		"erp_test.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erp_test.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erp_test.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erp_test.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erp_test.event.get_events"
# }

