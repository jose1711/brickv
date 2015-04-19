#!/usr/bin/env python

import os

def system(command):
    if os.system(command) != 0:
        exit(1)

system("pyuic4 -o ui_red.py ui/red.ui")
system("pyuic4 -o ui_red_tab_overview.py ui/red_tab_overview.ui")
system("pyuic4 -o ui_red_tab_settings.py ui/red_tab_settings.ui")
system("pyuic4 -o ui_red_tab_settings_network.py ui/red_tab_settings_network.ui")
system("pyuic4 -o ui_red_tab_settings_mobile_internet.py ui/red_tab_settings_mobile_internet.ui")
system("pyuic4 -o ui_red_tab_settings_mobile_internet_puk_dialog.py ui/red_tab_settings_mobile_internet_puk_dialog.ui")
system("pyuic4 -o ui_red_tab_settings_mobile_internet_provider_preset_dialog.py ui/red_tab_settings_mobile_internet_provider_preset_dialog.ui")
system("pyuic4 -o ui_red_tab_settings_ap.py ui/red_tab_settings_ap.ui")
system("pyuic4 -o ui_red_tab_settings_ap_dhcp_leases_dialog.py ui/red_tab_settings_ap_dhcp_leases_dialog.ui")
system("pyuic4 -o ui_red_tab_settings_server_monitoring.py ui/red_tab_settings_server_monitoring.ui")
system("pyuic4 -o ui_red_tab_settings_server_monitoring_add_host_dialog.py ui/red_tab_settings_server_monitoring_add_host_dialog.ui")
system("pyuic4 -o ui_red_tab_settings_openhab.py ui/red_tab_settings_openhab.ui")
system("pyuic4 -o ui_red_tab_settings_brickd.py ui/red_tab_settings_brickd.ui")
system("pyuic4 -o ui_red_tab_settings_datetime.py ui/red_tab_settings_datetime.ui")
system("pyuic4 -o ui_red_tab_settings_filesystem.py ui/red_tab_settings_filesystem.ui")
system("pyuic4 -o ui_red_tab_settings_services.py ui/red_tab_settings_services.ui")
system("pyuic4 -o ui_red_tab_program.py ui/red_tab_program.ui")
system("pyuic4 -o ui_red_tab_console.py ui/red_tab_console.ui")
system("pyuic4 -o ui_red_tab_versions.py ui/red_tab_versions.ui")
system("pyuic4 -o ui_red_tab_extension.py ui/red_tab_extension.ui")
system("pyuic4 -o ui_red_tab_extension_ethernet.py ui/red_tab_extension_ethernet.ui")
system("pyuic4 -o ui_red_tab_importexport.py ui/red_tab_importexport.ui")
system("pyuic4 -o ui_red_tab_importexport_import.py ui/red_tab_importexport_import.ui")
system("pyuic4 -o ui_red_tab_importexport_export.py ui/red_tab_importexport_export.ui")
system("pyuic4 -o ui_red_tab_importexport_systemlogs.py ui/red_tab_importexport_systemlogs.ui")

system("pyuic4 -o ui_program_info_main.py ui/program_info_main.ui")
system("pyuic4 -o ui_program_info_files.py ui/program_info_files.ui")
system("pyuic4 -o ui_program_info_logs.py ui/program_info_logs.ui")
system("pyuic4 -o ui_program_info_logs_view.py ui/program_info_logs_view.ui")
system("pyuic4 -o ui_program_info_c.py ui/program_info_c.ui")
system("pyuic4 -o ui_program_info_c_compile.py ui/program_info_c_compile.ui")
system("pyuic4 -o ui_program_info_csharp.py ui/program_info_csharp.ui")
system("pyuic4 -o ui_program_info_delphi.py ui/program_info_delphi.ui")
system("pyuic4 -o ui_program_info_delphi_compile.py ui/program_info_delphi_compile.ui")
system("pyuic4 -o ui_program_info_java.py ui/program_info_java.ui")
system("pyuic4 -o ui_program_info_javascript.py ui/program_info_javascript.ui")
system("pyuic4 -o ui_program_info_octave.py ui/program_info_octave.ui")
system("pyuic4 -o ui_program_info_perl.py ui/program_info_perl.ui")
system("pyuic4 -o ui_program_info_php.py ui/program_info_php.ui")
system("pyuic4 -o ui_program_info_python.py ui/program_info_python.ui")
system("pyuic4 -o ui_program_info_ruby.py ui/program_info_ruby.ui")
system("pyuic4 -o ui_program_info_shell.py ui/program_info_shell.ui")
system("pyuic4 -o ui_program_info_vbnet.py ui/program_info_vbnet.ui")

system("pyuic4 -o ui_program_page_general.py ui/program_page_general.ui")
system("pyuic4 -o ui_program_page_files.py ui/program_page_files.ui")
system("pyuic4 -o ui_program_page_c.py ui/program_page_c.ui")
system("pyuic4 -o ui_program_page_csharp.py ui/program_page_csharp.ui")
system("pyuic4 -o ui_program_page_delphi.py ui/program_page_delphi.ui")
system("pyuic4 -o ui_program_page_java.py ui/program_page_java.ui")
system("pyuic4 -o ui_program_page_javascript.py ui/program_page_javascript.ui")
system("pyuic4 -o ui_program_page_octave.py ui/program_page_octave.ui")
system("pyuic4 -o ui_program_page_perl.py ui/program_page_perl.ui")
system("pyuic4 -o ui_program_page_php.py ui/program_page_php.ui")
system("pyuic4 -o ui_program_page_python.py ui/program_page_python.ui")
system("pyuic4 -o ui_program_page_ruby.py ui/program_page_ruby.ui")
system("pyuic4 -o ui_program_page_shell.py ui/program_page_shell.ui")
system("pyuic4 -o ui_program_page_vbnet.py ui/program_page_vbnet.ui")
system("pyuic4 -o ui_program_page_arguments.py ui/program_page_arguments.ui")
system("pyuic4 -o ui_program_page_stdio.py ui/program_page_stdio.ui")
system("pyuic4 -o ui_program_page_schedule.py ui/program_page_schedule.ui")
system("pyuic4 -o ui_program_page_summary.py ui/program_page_summary.ui")
system("pyuic4 -o ui_program_page_upload.py ui/program_page_upload.ui")
system("pyuic4 -o ui_program_page_download.py ui/program_page_download.ui")

system("python build_scripts.py")

system("python generate_mobile_internet_dicts.py")
