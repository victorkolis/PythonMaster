def format_money(amount: float or int) -> str:
    if isinstance(amount, int):
        return f'${amount}.00'
    else:
        amount = str(amount)
        floating_point_index = amount.index('.') + 1
        if len(amount[floating_point_index:]) == 1:
            return f'${amount}0'
        else:
            return f'${amount}'


print(format_money(39.9))
