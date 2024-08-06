from modules.WebDriverInstaller import *

# Bypassing ESET antivirus detection
from modules.EsetTools import EsetRegister as ER
from modules.EsetTools import EsetKeygen as EK
#from modules.EsetTools import EsetBusinessRegister as EBR
#from modules.EsetTools import EsetBusinessKeygen as EBK

from modules.Statistics import Statistics
from modules.SharedTools import *
from modules.EmailAPIs import *
from modules.Updater import get_assets_from_version, parse_update_json, updater_main
from modules.MBCI import *

import traceback
import colorama
import platform
import datetime
import argparse
import time
import sys
import os
import re

VERSION = ['v1.4.9.6', 1496]
LOGO = f"""
███████╗███████╗███████╗████████╗   ██╗  ██╗███████╗██╗   ██╗ ██████╗ ███████╗███╗   ██╗
██╔════╝██╔════╝██╔════╝╚══██╔══╝   ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝ ██╔════╝████╗  ██║
█████╗  ███████╗█████╗     ██║      █████╔╝ █████╗   ╚████╔╝ ██║  ███╗█████╗  ██╔██╗ ██║
██╔══╝  ╚════██║██╔══╝     ██║      ██╔═██╗ ██╔══╝    ╚██╔╝  ██║   ██║██╔══╝  ██║╚██╗██║   
███████╗███████║███████╗   ██║      ██║  ██╗███████╗   ██║   ╚██████╔╝███████╗██║ ╚████║   
╚══════╝╚══════╝╚══════╝   ╚═╝      ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                                      
                                                Project Version: {VERSION[0]}
                                                Project Devs: rzc0d3r, AdityaGarg8, k0re,
                                                              Fasjeit, alejanpa17, Ischunddu,
                                                              soladify, AngryBonk, Xoncia
"""
if '--no-logo' in sys.argv:
    LOGO = f"ESET KeyGen {VERSION[0]} by rzc0d3r\n"
if datetime.datetime.now().day == 6 and datetime.datetime.now().month == 8: # Birthday of rzc0d3r
    colored_logo = ''
    colors = [getattr(Fore, attr) for attr in dir(Fore) if not attr.startswith('__')]
    colors.remove(Fore.BLACK)
    colors.remove(Fore.WHITE)
    colors.remove(Fore.LIGHTWHITE_EX)
    for line in LOGO.split('\n'):
        for ch in line:
            color = random.choice(colors)
            colored_logo += (color+ch+Fore.RESET)
        colored_logo += '\n'
    colored_logo += f'{Fore.GREEN}rzc0d3r{Fore.RESET} celebrates his {Fore.LIGHTRED_EX}birthday{Fore.RESET} today!!! :)\n'
    LOGO = colored_logo

# -- Quick settings [for Developers to quickly change behavior without changing all files] --
DEFAULT_EMAIL_API = 'developermail'
AVAILABLE_EMAIL_APIS = ['1secmail', 'hi2in', '10minutemail', 'tempmail', 'guerrillamail', 'developermail']
WEB_WRAPPER_EMAIL_APIS = ['10minutemail', 'hi2in', 'tempmail', 'guerrillamail']
EMAIL_API_CLASSES = {
    'guerrillamail': GuerRillaMailAPI,
    '10minutemail': TenMinuteMailAPI,
    'hi2in': Hi2inAPI,                  
    'tempmail': TempMailAPI,
    '1secmail': OneSecEmailAPI,
    'developermail': DeveloperMailAPI,
}

args = {
    'chrome': True,
    'firefox': False,
    'edge': False,

    'key': True,
    'account': False,
    'business_key': False,
    'business_account': False,
    'only_webdriver_update': False,
    'update': False,

    'skip_webdriver_menu': False,
    'no_headless': False,
    'custom_browser_location': '',
    'email_api': DEFAULT_EMAIL_API,
    'custom_email_api': False,
    'skip_update_check': False,
    'no_logo': False,
    'disable_progress_bar': False
}

def RunMenu():
    MainMenu = ViewMenu(LOGO+'\n---- Main Menu ----')

    SettingMenu = ViewMenu(LOGO+'\n---- Settings Menu ----')
    SettingMenu.add_item(
        OptionAction(
            args,
            title='Browsers',
            action='store_true',
            args_names=['chrome', 'firefox', 'edge'],
            default_value='chrome'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='Modes of operation',
            action='store_true',
            #args_names=['key', 'account', 'business-account', 'business-key', 'only-webdriver-update', 'update'],
            args_names=['key', 'account', 'only-webdriver-update', 'update'],
            default_value='key')
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='Email APIs',
            action='choice',
            args_names='email-api',
            choices=AVAILABLE_EMAIL_APIS,
            default_value=DEFAULT_EMAIL_API
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--skip-webdriver-menu',
            action='bool_switch',
            args_names='skip-webdriver-menu'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--no-headless',
            action='bool_switch',
            args_names='no-headless'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--custom-browser-location',
            action='manual_input',
            args_names='custom-browser-location',
            default_value=''
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--custom-email-api',
            action='bool_switch',
            args_names='custom-email-api'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--skip-update-check',
            action='bool_switch',
            args_names='skip_update_check'
        )
    )
    SettingMenu.add_item(
        OptionAction(
            args,
            title='--disable-progress-bar',
            action='bool_switch',
            args_names='disable_progress_bar'
        )
    )
    SettingMenu.add_item(MenuAction('Back', MainMenu))
    MainMenu.add_item(MenuAction('Settings', SettingMenu))
    MainMenu.add_item(MenuAction(f'Do it, damn it!', main))
    MainMenu.add_item(MenuAction('Exit', sys.exit))
    MainMenu.view()

def parse_argv():
    print(LOGO)
    if len(sys.argv) == 1: # Menu
        RunMenu()
    else: # CLI
        args_parser = argparse.ArgumentParser()
        # Required
        ## Browsers
        args_browsers = args_parser.add_mutually_exclusive_group(required=('--update' not in sys.argv))
        args_browsers.add_argument('--chrome', action='store_true', help='Launching the project via Google Chrome browser')
        args_browsers.add_argument('--firefox', action='store_true', help='Launching the project via Mozilla Firefox browser')
        args_browsers.add_argument('--edge', action='store_true', help='Launching the project via Microsoft Edge browser')
        ## Modes of operation
        args_modes = args_parser.add_mutually_exclusive_group(required=True)
        args_modes.add_argument('--key', action='store_true', help='Generating an ESET-HOME license key (example as AGNV-XA2V-EA89-U546-UVJP)')
        args_modes.add_argument('--account', action='store_true', help='Generating an ESET HOME Account (To activate the free trial version)')
        #args_modes.add_argument('--business-account', action='store_true', help='Generating an ESET BUSINESS Account (To huge businesses) - Requires manual captcha input!!!')
        #args_modes.add_argument('--business-key', action='store_true', help='Generating an ESET BUSINESS Account and creating a universal license key for ESET products (1 key - 75 devices) - Requires manual captcha input!!!')
        args_modes.add_argument('--only-webdriver-update', action='store_true', help='Updates/installs webdrivers and browsers without generating account and license key')
        args_modes.add_argument('--update', action='store_true', help='Switching to program update mode - Overrides all arguments that are available!!!')
        # Optional
        args_parser.add_argument('--skip-webdriver-menu', action='store_true', help='Skips installation/upgrade webdrivers through the my custom wrapper (The built-in selenium-manager will be used)')
        args_parser.add_argument('--no-headless', action='store_true', help='Shows the browser at runtime (The browser is hidden by default, but on Windows 7 this option is enabled by itself)')
        args_parser.add_argument('--custom-browser-location', type=str, default='', help='Set path to the custom browser (to the binary file, useful when using non-standard releases, for example, Firefox Developer Edition)')
        args_parser.add_argument('--email-api', choices=AVAILABLE_EMAIL_APIS, default=DEFAULT_EMAIL_API, help='Specify which api to use for mail')
        args_parser.add_argument('--custom-email-api', action='store_true', help='Allows you to manually specify any email, and all work will go through it. But you will also have to manually read inbox and do what is described in the documentation for this argument')
        args_parser.add_argument('--skip-update-check', action='store_true', help='Skips checking for program updates')
        args_parser.add_argument('--no-logo', action='store_true', help='Replaces ASCII-Art with plain text')
        args_parser.add_argument('--disable-progress-bar', action='store_true', help='Disables the webdriver download progress bar')
        #args_parser.add_argument('--try-auto-cloudflare',action='store_true', help='Removes the prompt for the user to press Enter when solving cloudflare captcha. In some cases it may go through automatically, which will give the opportunity to use tempmail in automatic mode!')
        try:
            global args
            args = vars(args_parser.parse_args())
        except:
            time.sleep(3)
            sys.exit(-1)

def send_statistics(statisctis_object: Statistics, name, value=''):
    # sending program {name}-statistics
    console_log(f'Sending {name}-statistics to the developer...', INFO, True)
    for _ in range(3):
        if statisctis_object.send_statistics(name, value):
            console_log('Successfully sent!\n', OK, False)
            break
        time.sleep(1)
    else:
        console_log('Sending error, skipped!\n', ERROR, False)

def main():
    if len(sys.argv) == 1: # for Menu
        print()
    try:
        # disabling the ability to use business generation (since that method is dead)
        args['business_key'] = False
        args['business_account'] = False
        # sending program runs-statistics
        if not args['update']:
            st = Statistics()
            send_statistics(st, 'runs')
        # check program updates
        if args['update']:
            print(f'{Fore.LIGHTMAGENTA_EX}-- Updater --{Fore.RESET}\n')
            updater_main(from_main=True) # from_main - changes the behavior in Updater so that everything works correctly from under main.py
            if len(sys.argv) == 1:
                input('\nPress Enter to exit...')
            else:
                time.sleep(3) # exit-delay
            sys.exit(0)
        if not args['skip_update_check'] and not args['update']:
            try:
                if parse_update_json(from_main=True) is not None:
                    print(f'{Fore.LIGHTMAGENTA_EX}-- Updater --{Fore.RESET}\n')
                    latest_cloud_version = get_assets_from_version(parse_update_json(from_main=True), 'latest')['version']
                    latest_cloud_version_int = latest_cloud_version[1:].split('.')
                    latest_cloud_version_int = int(''.join(latest_cloud_version_int[:-1])+latest_cloud_version_int[-1][0])
                    if VERSION[1] > latest_cloud_version_int:
                        console_log(f'The project has an unreleased version, maybe you are using a build from the developer?\n', WARN, True)
                    elif latest_cloud_version_int > VERSION[1]:
                        console_log(f'Project update is available up to version: {colorama.Fore.GREEN}{latest_cloud_version}{colorama.Fore.RESET}', WARN)
                        console_log('If you want to download the update run this file with --update argument\n', WARN)
                    else:
                        console_log('Project up to date!!!\n', OK)
            except:
                pass
        # initialization and configuration of everything necessary for work
        # changing input arguments for special cases
        if platform.release() == '7' and sys.platform.startswith('win'): # fix for Windows 7
            args['no_headless'] = True
        elif args['business_account'] or args['business_key'] or args['email_api'] in ['tempmail']:
            args['no_headless'] = True
        driver = None
        webdriver_path = None
        browser_name = GOOGLE_CHROME
        if args['firefox']:
            browser_name = MOZILLA_FIREFOX
        if args['edge']:
            browser_name = MICROSOFT_EDGE
        if not args['skip_webdriver_menu']: # updating or installing webdriver
            if args['custom_browser_location'] != '':
                webdriver_installer = WebDriverInstaller(browser_name, args['custom_browser_location'])
            else:
                webdriver_installer = WebDriverInstaller(browser_name)
            webdriver_path, args['custom_browser_location'] = webdriver_installer.menu(args['disable_progress_bar'])
        if not args['only_webdriver_update']:
            driver = initSeleniumWebDriver(browser_name, webdriver_path, args['custom_browser_location'], (not args['no_headless']))
            if driver is None:
                raise RuntimeError(f'{browser_name} initialization error!')
        else:
            sys.exit(0)

        # main part of the programd
        console_log(f'\n{Fore.LIGHTMAGENTA_EX}-- KeyGen --{Fore.RESET}\n')
        if not args['custom_email_api']:  
            console_log(f'[{args["email_api"]}] Mail registration...', INFO)
            if args['email_api'] in WEB_WRAPPER_EMAIL_APIS: # WebWrapper API, need to pass the selenium object to the class initialization
                email_obj = EMAIL_API_CLASSES[args['email_api']](driver)
            else: # real APIs without the need for a browser
                email_obj = EMAIL_API_CLASSES[args['email_api']]()
            email_obj.init()
            console_log('Mail registration completed successfully!', OK)
        else:
            email_obj = CustomEmailAPI()
            while True:
                email = input(f'[  {colorama.Fore.YELLOW}INPT{colorama.Fore.RESET}  ] {colorama.Fore.CYAN}Enter the email address you have access to: {colorama.Fore.RESET}').strip()
                try:
                    matched_email = re.match(r'[-a-z0-9+]+@[a-z]+(\.[a-z]+)+', email).group()
                    if matched_email == email:
                        email_obj.email = matched_email
                        console_log('Mail has the correct syntax!', OK)
                        break
                    else:
                        raise RuntimeError
                except:
                    console_log('Invalid email syntax!!!', ERROR)
        eset_password = dataGenerator(10)
        
        # standart generator
        if args['account'] or args['key']:
            ER_obj = ER(email_obj, eset_password, driver)
            ER_obj.createAccount()
            ER_obj.confirmAccount()
            output_line = '\n'.join([
                    '',
                    '----------------------------------',
                    f'Account Email: {email_obj.email}',
                    f'Account Password: {eset_password}',
                    '----------------------------------',
                    ''
            ])        
            output_filename = 'ESET ACCOUNTS.txt'
            if args['key']:
                output_filename = 'ESET KEYS.txt'
                EK_obj = EK(email_obj, driver)
                EK_obj.sendRequestForKey()
                license_name, license_key, license_out_date = EK_obj.getLicenseData()
                output_line = '\n'.join([
                    '',
                    '----------------------------------',
                    f'Account Email: {email_obj.email}',
                    f'Account Password: {eset_password}',
                    '',
                    f'License Name: {license_name}',
                    f'License Key: {license_key}',
                    f'License Out Date: {license_out_date}',
                    '----------------------------------',
                    ''
                ])
                
        """# new generator
        elif args['business_account'] or args['business_key']:
            EBR_obj = EBR(email_obj, eset_password, driver)
            EBR_obj.createAccount()
            EBR_obj.confirmAccount()
            output_line = '\n'.join([
                    '',
                    '----------------------------------',
                    f'Business Account Email: {email_obj.email}',
                    f'Business Account Password: {eset_password}',
                    '----------------------------------',
                    ''
            ])    
            output_filename = 'ESET ACCOUNTS.txt'
            if args['business_key']:
                output_filename = 'ESET KEYS.txt'
                EBK_obj = EBK(email_obj, eset_password, driver)
                EBK_obj.sendRequestForKey()
                license_name, license_key, license_out_date = EBK_obj.getLicenseData()
                output_line = '\n'.join([
                    '',
                    '----------------------------------',
                    f'Business Account Email: {email_obj.email}',
                    f'Business Account Password: {eset_password}',
                    '',
                    f'License Name: {license_name}',
                    f'License Key: {license_key}',
                    f'License Out Date: {license_out_date}',
                    '----------------------------------',
                    ''
                ])"""

        # end
        console_log(output_line)
        date = datetime.datetime.now()
        f = open(f"{str(date.day)}.{str(date.month)}.{str(date.year)} - "+output_filename, 'a')
        f.write(output_line)
        f.close()
        # sending program gens-statistics
        #st = Statistics()
        #send_statistics(st, 'gens')
    
    except Exception as E:
        traceback_string = traceback.format_exc()
        if str(type(E)).find('selenium') and traceback_string.find('Stacktrace:') != -1: # disabling stacktrace output
            traceback_string = traceback_string.split('Stacktrace:', 1)[0]
        console_log(traceback_string, ERROR)
    if len(sys.argv) == 1:
        input('Press Enter to exit...')
    else:
        time.sleep(3) # exit-delay
    if driver is not None:
        driver.quit()
    sys.exit()

if __name__ == '__main__':
    parse_argv() # if Menu, the main function will be called in automatic mode
    if len(sys.argv) > 1: # CLI
        main()
