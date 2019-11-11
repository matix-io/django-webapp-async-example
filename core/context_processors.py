def check_async(request):
	ctx = {}
	if 'async' in request.GET:
		ctx['async'] = True
	return ctx
