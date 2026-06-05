#iconitodev/admin/view.py
#issue  dev           date       description
# na    Julio Conchas 06/04/2026 first creation

# Test dimensions data
DIMENSIONS = [
    {
        'id': 1,
        'title': 'Flujo de información',
        'description': 'Cómo fluye la información necesaria para comprender lo que ocurre en el negocio.',
        'low_exposure': 'La información relevante suele estar disponible, ser consistente y fácil de consultar cuando se necesita.',
        'high_exposure': 'La información suele estar dispersa, incompleta o ser difícil de obtener cuando se necesita.'
    },
    {
        'id': 2,
        'title': 'Conexión de decisiones',
        'description': 'Cómo se conectan las decisiones que impactan la creación, entrega y captura de valor dentro del negocio.',
        'low_exposure': 'Las decisiones suelen considerar sus efectos sobre las demás áreas involucradas.',
        'high_exposure': 'Las decisiones suelen tomarse de forma aislada, generando efectos no previstos en otras partes del negocio.'
    },
    {
        'id': 3,
        'title': 'Aprovechamiento de capacidades',
        'description': 'Cómo se aprovechan las capacidades, recursos, conocimientos y talento disponibles para generar resultados.',
        'low_exposure': 'Las capacidades disponibles suelen traducirse en resultados y generación de valor.',
        'high_exposure': 'Parte importante de las capacidades disponibles permanece sin aprovecharse o genera menos valor del esperado.'
    },
    {
        'id': 4,
        'title': 'Sincronización operativa',
        'description': 'Cómo coinciden en tiempo y forma las acciones necesarias para ejecutar la operación del negocio.',
        'low_exposure': 'Las acciones clave suelen ocurrir de forma coordinada y en el momento adecuado.',
        'high_exposure': 'Las acciones suelen ejecutarse fuera de tiempo o sin la coordinación necesaria.'
    },
    {
        'id': 5,
        'title': 'Adaptación al cambio',
        'description': 'Cómo ajusta el negocio su forma de operar cuando cambian las condiciones internas o externas.',
        'low_exposure': 'Los cambios suelen convertirse rápidamente en ajustes y acciones concretas.',
        'high_exposure': 'Los ajustes suelen ocurrir tarde o después de que los cambios ya impactaron los resultados.'
    },
    {
        'id': 6,
        'title': 'Dependencia de recursos',
        'description': 'Cómo evolucionan los resultados del negocio en relación con los recursos que requiere para sostenerlos.',
        'low_exposure': 'El negocio suele mejorar resultados aprovechando mejor los recursos ya disponibles.',
        'high_exposure': 'Mejorar resultados suele requerir incorporar más recursos para sostener el desempeño.'
    }
]
def get_exposure_category(score):
    """Translate numerical score to exposure category"""
    if score <= 20:
        return {'level': 'Muy Baja', 'class': 'exposure-very-low', 'value': score}
    elif score <= 40:
        return {'level': 'Baja', 'class': 'exposure-low', 'value': score}
    elif score <= 60:
        return {'level': 'Moderada', 'class': 'exposure-moderate', 'value': score}
    elif score <= 80:
        return {'level': 'Alta', 'class': 'exposure-high', 'value': score}
    else:
        return {'level': 'Muy Alta', 'class': 'exposure-very-high', 'value': score}

def get_result_interpretation(score):
    """Get interpretation text based on exposure index"""
    category = get_exposure_category(score)
    
    interpretations = {
        'Muy Baja': {
            'title': 'Exposición Muy Baja',
            'executive': 'La pérdida de valor estructural no parece ser una preocupación relevante en este momento.',
            'interpretation': 'Las condiciones observadas sugieren un sistema de negocio que, en términos generales, mantiene un comportamiento favorable para crear, entregar y capturar valor.'
        },
        'Baja': {
            'title': 'Exposición Baja',
            'executive': 'El resultado general es favorable, aunque existen algunas áreas que podrían optimizarse.',
            'interpretation': 'El negocio mantiene condiciones generalmente positivas, pero hay oportunidades de mejora en ciertas dimensiones estructurales.'
        },
        'Moderada': {
            'title': 'Exposición Moderada',
            'executive': 'Existen condiciones estructurales que están impactando el desempeño actual del negocio.',
            'interpretation': 'El sistema de negocio presenta vulnerabilidades en su estructura que podrían estar limitando el potencial de valor. Requiere atención estratégica.'
        },
        'Alta': {
            'title': 'Exposición Alta',
            'executive': 'La pérdida de valor estructural es probablemente un factor relevante en el desempeño actual del negocio.',
            'interpretation': 'Se han identificado condiciones estructurales significativas que están generando pérdida de valor. Requiere intervención inmediata.'
        },
        'Muy Alta': {
            'title': 'Exposición Muy Alta',
            'executive': 'La pérdida de valor estructural es un factor crítico en el desempeño del negocio.',
            'interpretation': 'Las condiciones estructurales observadas indican un alto riesgo de pérdida de valor continua. Requiere transformación urgente de los sistemas de negocio.'
        }
    }
    
    return interpretations.get(category['level'], interpretations['Moderada'])
