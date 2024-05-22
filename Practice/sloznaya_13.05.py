def find_fake_coin(coins):
    # Взвешивание первых двух групп монет
    if sum(coins[:3]) < sum(coins[3:6]):
        # Если первая группа легче, возвращаем индекс первой монеты в этой группе
        return coins.index(min(coins[:3]))
    elif sum(coins[:3]) > sum(coins[3:6]):
        # Если вторая группа легче, возвращаем индекс первой монеты в этой группе
        return coins.index(min(coins[3:6]))
    else:
        # Если обе группы весят одинаково, возвращаем индекс первой монеты в третьей группе
        return 6 if coins[6] < coins[7] else 7

# Пример использования
coins = [1, 7]  
fake_coin_index = find_fake_coin(coins)
print("Фальшивая монета находится под индексом:", fake_coin_index)
