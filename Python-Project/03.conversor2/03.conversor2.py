EXCHANGE_RATES =  {
    "EUR": {
        "EUR": 1,
        "USD": 1.14,
        "GBP": 0.85
    },
    "USD": {
        "USD": 1,
        "EUR": 0.88,
        "GBP": 0.74
    },
    "GBP": {
        "GBP": 1,
        "USD": 1.34,
        "EUR": 1.18
    }
}

CURRENCY_OPTIONS = {
    "USD": "Dollar",
    "EUR": "Euro",
    "GBP": "British Pound"
}

# --- START Function currency options USD, GBP and EURO ---
def display_currency_options(options_dict):
    options_string = ""

    for key, value in options_dict.items():
        options_string += f"{key}) {value}\n"

    return options_string
# --- END ---

# --- START Function Menu ---
def get_conversion_inputs(options_dict):
    print("\n ------ Welcome to the Coin Converter App ------\n")

    source_currency = ""
    target_currency = ""
    amount = None

    while source_currency not in options_dict:
        source_currency = input("¿What currency do you bring?\n"
                                f"{display_currency_options(CURRENCY_OPTIONS)}\n"
                                ">> "
                                ).upper()
        if source_currency not in options_dict:
            print("¡Input not valid, please enter one of the listed codes!")

    while amount is None:
        amount_usr = input(f"\nEnter amount to change in {source_currency}: ")
        try:
            amount = float(amount_usr)
            if amount < 1:
                print("The amount can't be negative. Try again")
                amount = None
        except ValueError:
            print("Not valid! Please enter a valid number for quantity")

    while target_currency not in options_dict:
        target_currency = input("\n¿Which currency you will change?\n"
                                f"{display_currency_options(CURRENCY_OPTIONS)}\n"  
                                ">> "
                                ).upper()
        if target_currency not in options_dict:
           print("¡Input not valid, please enter one of the listed codes!")

    return source_currency, amount, target_currency
# --- END ---

def change_currency(exchange_rates_dict, source_curr, amount_val, target_curr):
    exchange_rate = exchange_rates_dict[source_curr][target_curr]
    converted_amount = exchange_rate * amount_val

    print(f"{amount_val} {source_curr} is {converted_amount: .2f} {target_curr}")

change_currency(EXCHANGE_RATES, *get_conversion_inputs(CURRENCY_OPTIONS))