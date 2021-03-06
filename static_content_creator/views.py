from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'static_content_creator'}


@view_config(route_name="manage",
             renderer='templates/manage.pt')
def management_view(request):
    return {'project': 'static_content_creator'}