from django.shortcuts import render_to_response

from .models import Competition
from .logic import calculate_table


def table(request):
    table = calculate_table()
    cols = ['total'] + [c.name for c in Competition.objects.all()]
    return render_to_response('table.html', {
        'tables': {c: [
            (r[c], r['name'])
            for r in sorted(table, key=(lambda x: -x[c]))
        ] for c in cols},
        'cols': cols,
        'cls': 'col-sm-%d' % (12 // len(cols),)
    })
