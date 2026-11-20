def calculate_fee(scholarship, late_payment):
    fee = 1000

    if scholarship == True:
        fee = fee - (fee * 0.10)

    if late_payment == True:
        fee = fee + 100

    return fee
