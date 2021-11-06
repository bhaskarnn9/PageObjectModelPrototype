class Locator(object):
    # ###########################################################################################################
    # ########################################## Project constants ##############################################
    TIME_OUT = 30
    PAGE_WAIT = 3

    # ###########################################################################################################

    # ###########################################################################################################
    # ########################################## Home Page Objects ##############################################

    # Gemini Sandbox url
    base_url = 'https://exchange.sandbox.gemini.com'

    # Home Page Title
    home_page_title = '[Sandbox] Gemini - Sign In'

    # Gemini - Logo
    logo = '//*[@id="gemini-logo-cyan_svg__Layer_1"]'

    # Enter Email - Error Message
    error_msg = '//*[@id="container"]/div/div/div/div/div/div[3]/form/label[1]/div[3]'

    # ###########################################################################################################

    # ###########################################################################################################
    # ################################# Registration Page Objects ###################################

    # Create New Account
    create_new_account = '//*[@id="container"]/div/div/div/div/div/div[3]/form/div/div/a[1]'

    # Cookie Policy Agree
    cookie_policy_agree = '//*[@id="cookiePolicyAgreement"]/div/a'

    # Create Account Page Title
    create_acc_page_title = '[Sandbox] Gemini - Institutional Client Registration'

    # Create a Business Account
    create_business_acc = '//*[@id="container"]/div/div/div/div/div/div[3]/form/div[4]/div/a[2]'

    # ###########################################################################################################

    # ###########################################################################################################
    # ############################## Institution Registration page objects ######################################

    # Business Url
    business_url = base_url + '/register/institution'

    # Business Name
    business_name = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/fieldset[1]/div/div[1]/label/div[2]/input'

    # company type
    company_type = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/fieldset[1]/div/div[2]/label/div[2]/div'

    # Broker-Dealer
    visible_text_type = 'Broker-Dealer'

    # state
    state = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/fieldset[2]/div/div[2]/label/div[2]/div'

    # State - AK
    visible_text_state = 'AK'

    # First Name
    first_name_box = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/span/fieldset/div[1]/div[1]/label/div[2]/input'

    # Middle Name
    middle_name_box = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/span/fieldset/div[1]/div[2]/label/div[2]/input'

    # Last Name
    last_name_box = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/span/fieldset/div[1]/div[3]/label/div[2]/input'

    # Email Address
    email_address_box = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/span/fieldset/div[2]/div/label/div[2]/input'

    # Continue Button
    continue_button = '//*[@id="container"]/div/div/div[2]/div/div[2]/form/div/button'

    # Thanks
    thanks_message = '//*[@id="container"]/div/div/div[2]/div/div[2]/div[1]/h3'

    # ###########################################################################################################
