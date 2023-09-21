# trabalhando com números

def exchange_money(budget, exchange_rate):
    """ Estimar valor após a troca

    :param budget: float - quantidade de dinheiro que voce esta planejando trocar
    :param exchange_float: float - valor unitario da moeda estrangeira
    :return: float - valor que você receberá após a troca    
    """
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """ Calcular a moeda restante após uma troca

    :param budget: float - quantidade de dinheiro que voce tem
    :param exchanging_value: float - quantidade de dinheiro que vc quer trocar
    :return: float - valor restante da sua moeda inicial após a troca
    """

    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """ Calcular valor das notas

    :param denomination: float - valor de uma nota
    :param number_of_bills: float - quantidade de notas que vc recebeu
    :return: float total de dinheiro que vc tem
    """

    return denomination * number_of_bills

def get_number_of_bills(budget, denomination):
    """ Calcular número de notas

    :param budget: float - valor que vc planeja trocar
    :param denomination: int - valor de uma unica nota
    :return: int - numero de notas depois de trocar todo o seu dinheiro
    """
    return budget // denomination

def get_leftover_of_bills(budget, denomination):
    """ Calcular sobras depois de trocar por notas

    :param budget: float - valor que vc planeja trocar
    :param denomination: int - valor de uma unica nota
    :return: float - int - valor que sobrou e nao deu pra ser trocado
    """

    return budget % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """ Calcular valor máximo retornado após a compra

    :param budget: float - valor que vc planeja trocar
    :param exchange_rate: float - valor unitário da moeda estrangeira
    :param spread: int - porcentagem da taxa de cambio
    :param denomination: int - valor de uma unica nota
    :return: int - valor máximo que vc consegue trocar
    """

    spread_decimal = spread / 100
    exchange_rate_with_spread = exchange_rate + (exchange_rate * spread_decimal)

    max_value = exchange_money(budget, exchange_rate_with_spread)
    max_value = int(max_value // denomination) * denomination
   
    return max_value

# Executando funções
print(exchange_money(100000, 0.8))
print(get_change(127.5, 120))
print(get_value_of_bills(5, 128))
print(get_number_of_bills(127.5, 5))
print(get_leftover_of_bills(127.5, 20))
print(exchangeable_value(127.25, 1.20, 10, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))