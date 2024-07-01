from .models import profesor

def profesor_context(request):
    profesor_id = request.session.get('profesor_id')
    if profesor_id:
        profesor_obj = profesor.objects.get(id=profesor_id)
        return {'profesor_logueado': profesor_obj}
    return {}
