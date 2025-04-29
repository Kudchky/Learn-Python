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

# --- START --- Func Validations ---

# --- END ---

# --- START Function Menu ---
def get_conversion_inputs():
    print("\n ------ Welcome to the Coin Converter App ------\n")

    source_currency = input("¿What currency do you bring?\n"
                            f"{display_currency_options(CURRENCY_OPTIONS)}\n"
                            ">> "
                            )

    amount = float(input("\nEnter amount to change: "))

    target_currency = input("\n¿Which currency you will change?\n"
                            f"{display_currency_options(CURRENCY_OPTIONS)}\n"  
                            ">> "
                            )

    return source_currency, amount, target_currency
# --- END ---

def change_currency(exchange_rates_dict, source_curr, amount_val, target_curr):
    exchange_rate = exchange_rates_dict[source_curr][target_curr]
    converted_amount = exchange_rate * amount_val

    print(f"{amount_val} {source_curr} is {converted_amount: .2f} {target_curr}")

change_currency(EXCHANGE_RATES, *get_conversion_inputs())