import json

def lambda_handler(event, context):
    # Obtener los parámetros de la solicitud, amount = 0 si no encuetra este valor
    body = json.loads(event['body'])
    amount = float(body.get('amount', 0))
    from_currency = body.get('from_currency','USD')
    to_currency = body.get('to_currency','EUR')

    # Tasa de cambio fija para el ejemplo
    exchange_rates = {
        'USD': {'EUR': 0.93},
    }
    
    # Verificamos que todos los parámetros necesarios están presentes
    if not from_currency or not to_currency or amount <= 0:
        raise ValueError("Invalid input parameters")

    # Calcular la conversión, si se encuentran las divisas de conversion dentro del diccionario
    converted_amount = amount * exchange_rates[from_currency][to_currency]
    response = {
    # generamos el vuerpo de la respuesta del endpoint
        'converted_amount': converted_amount,
        'from_currency': from_currency,
        'to_currency': to_currency
        }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
