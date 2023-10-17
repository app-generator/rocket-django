def product_filter(request):
    filter_string = {}
    filter_mappings = {
        'search': 'name__icontains'
    }
    for key in request.GET:
        if request.GET.get(key) and key != 'page':
            filter_string[filter_mappings[key]] = request.GET.get(key)

    return filter_string