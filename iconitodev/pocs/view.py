#iconitodev/POCs/view.py
#issue  dev           date       description
# na    Julio Conchas 06/04/2026 first creation

from flask import Blueprint,render_template, request, jsonify, session
from .exposicionPoc import *

pocs = Blueprint('pocs',__name__)

@pocs.route('/exposicion',methods=['GET','POST'])
def exposicion():
    """Landing page with initial form"""
    return render_template('exposicion/start.html')

@pocs.route('/start-test')
def start_test():
    """Landing page with initial form"""
    return render_template('exposicion/test.html', dimensions=DIMENSIONS)


@pocs.route('/exp-results', methods=['POST'])
def exp_results():
    """Calculate and display results"""
    try:
        data = request.get_json()
        responses = data.get('responses', {})

        # Calculate average exposure index
        if responses:
            scores = [int(v) for v in responses.values() if v]
            exposure_index = sum(scores) / len(scores) if scores else 0
        else:
            exposure_index = 0

        exposure_index = round(exposure_index, 1)
        category = get_exposure_category(exposure_index)
        interpretation = get_result_interpretation(exposure_index)

        # Store results in session
        if 'respondent' not in session:
            session['respondent'] = {}

        session['respondent']['responses'] = responses
        session['respondent']['exposure_index'] = exposure_index
        session['respondent']['category'] = category['level']

        result_data = {
            'exposure_index': exposure_index,
            'category': category,
            'interpretation': interpretation,
            'respondent': session.get('respondent', {})
        }

        return jsonify(result_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@pocs.route('/exp-results-page')
def exp_results_page():
    """Display results page"""
    respondent = session.get('respondent', {})
    exposure_index = respondent.get('exposure_index', 0)
    
    category = get_exposure_category(exposure_index)
    interpretation = get_result_interpretation(exposure_index)
    
    return render_template('exposicion/index.html', 
                         exposure_index=exposure_index,
                         category=category,
                         interpretation=interpretation,
                         respondent=respondent)