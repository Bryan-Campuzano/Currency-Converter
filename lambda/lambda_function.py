import json

def lambda_handler(event, context):
    try:
        # Obtener los parámetros de la solicitud, amount = 0 si no encuetra este valor
        body = json.loads(event['body'])
        amount = float(body.get('amount', 0))
        from_currency = body.get('from_currency')
        to_currency = body.get('to_currency')

        # Verificamos que todos los parámetros necesarios están presentes
        if not from_currency or not to_currency or amount <= 0:
            raise ValueError("Invalid input parameters")

        # Tasa de cambio fija para el ejemplo
        exchange_rates = {
            'USD': {'EUR': 0.93, 'JPY': 159}
        }

        # Calcular la conversión, si se encuentran las divisas de conversion dentro del diccionario
        if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
            converted_amount = amount * exchange_rates[from_currency][to_currency]
            response = {
        # generamos el vuerpo de la respuesta del endpoint
                'converted_amount': converted_amount,
                'from_currency': from_currency,
                'to_currency': to_currency
            }
        else:
            response = {
                'error': 'Unsupported currency pair'
            }
        # manejamos los codigos de estatus html
        status_code = 200
    except (ValueError, KeyError, json.JSONDecodeError) as e:
        response = {
            'error': str(e)
        }
        status_code = 400
        # retornamos el codigo del status y el json de respuesta
    return {
        'statusCode': status_code,
        'body': json.dumps(response)
    }
