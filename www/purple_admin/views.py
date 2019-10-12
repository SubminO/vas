import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, Http404

from purple_admin.forms import RouteForm, RoutePlatformForm, PlatformTypeForm, BusModelForm, RoutePlatformFormset
from route.models import PlatformType, Route, RoutePlatform, BusModel, RoutePoint


@login_required
def cabinet(request):
    return render(request, 'admin_panel/cabinet.html')


@login_required
def cabinet_delete(request, pk, type):
    models_by_type = {
        'route': Route,
        'route_platform': RoutePlatform,
        'ts': BusModel
        # 'flat_type': RealEstateFlatTypeModel,
    }
    Model = models_by_type[type]
    objects = get_object_or_404(Model, pk=pk)
    objects.delete()
    if request.is_ajax():
        return JsonResponse({})
    return redirect('admin_panel_' + Model.model_type + '_list')


@login_required
def cabinet_add(request, type):
    models_by_type = {
        'route': Route,
        'route_platform': RoutePlatform,
        'route_platform_type': PlatformType,
        'ts': BusModel,
    }

    form_by_type = {
        'route': RouteForm,
        'route_platform': RoutePlatformForm,
        'route_platform_type': PlatformTypeForm,
        'ts': BusModelForm,
    }

    template_by_type = {
        'route': 'cabinet_form.html',
        'route_platform': 'cabinet_map_form.html',
        'route_platform_type': '_form.html',
    }

    Model = models_by_type[type]
    Form = form_by_type[type]
    template = template_by_type.get(type, 'cabinet_form.html')

    if request.method == 'POST':
        form = Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            config = form.save()
            if request.is_ajax():
                return JsonResponse({"id": config.id, "name": config.name})
            return redirect('admin_panel_' + Model.model_type + '_list')
    else:
        form = Form()
    context = {
        'form': form,
        'description': Model.model_description,
        'model_type': type,
    }
    return render(request, 'admin_panel/' + template, context=context)


@login_required
def cabinet_list(request, type):
    models_by_type = {
        'route': Route,
        'route_platform': RoutePlatform,
        'ts': BusModel,
        # 'flat_type': RealEstateFlatTypeModel,
    }
    model = models_by_type[type]
    objects = model.objects.all()
    context = {
        'objects': objects,
        'model_type': type,
    }
    return render(request, 'admin_panel/cabinet_list.html', context=context)


@login_required
def cabinet_edit(request, pk, type):
    models_by_type = {
        'route': Route,
        'route_platform': RoutePlatform,
        'route_platform_type': PlatformType,
        'ts': BusModel,
    }

    form_by_type = {
        'route': RouteForm,
        'route_platform': RoutePlatformForm,
        'route_platform_type': PlatformTypeForm,
        'ts': BusModelForm,
    }

    template_by_type = {
        'route': 'cabinet_form.html',
        'route_platform': 'cabinet_map_form.html',
        'route_platform_type': '_form.html',
    }

    Model = models_by_type[type]
    Form = form_by_type[type]
    template = template_by_type.get(type, 'cabinet_form.html')

    objects = get_object_or_404(Model, pk=pk)
    if request.method == 'POST':
        form = Form(request.POST or None, request.FILES or None, instance=objects)
        if form.is_valid():
            config = form.save()
            return redirect('admin_panel_' + Model.model_type + '_list')
    else:
        form = Form(instance=objects)
    context = {
        'form': form,
        'description': Model.model_description,
        'model_type': type,
    }
    return render(request, 'admin_panel/' + template, context=context)


@login_required
def ajax_add(request, type):
    # models_by_type = {
    #     'object': RealEstateObjectModel,
    #     'object_type': RealEstateObjectTypeModel,
    #     'flat_type': RealEstateFlatTypeModel,
    # }

    form_template_type = {
        'route': 'forms/_route_form.html',
        'route_platform': '_map_form.html',
        # 'flat_type': '_flat_form.html',
    }

    form_by_type = {
        'route': RouteForm,
        'route_platform': RoutePlatformForm,
        # 'flat_type': RealEstateFlatTypeForm,
    }

    # Model = models_by_type[type]
    Form = form_by_type[type]
    template = form_template_type[type]

    # type = 'realestate' if type == 'flat_type' else type

    if request.is_ajax():
        if request.method == 'POST':
            form = Form(request.POST, request.FILES)
            if form.is_valid():
                form = form.save()
                return JsonResponse(model_to_dict(form))
            else:
                form = Form()
        else:
            return
    else:
        if request.method == 'POST':
            form = Form(request.POST, request.FILES)
            if form.is_valid():
                form = form.save()
                # form.create_relations_by_string_ids(request.POST.get('flats', None))
                return redirect('admin_panel_' + type + '_list')
        return redirect('admin_panel_cabinet')
    context = {
        'form': form,
        'model_type': Form.Meta.model.model_type,
        'model_description': Form.Meta.model.model_description,
    }
    return render(request, 'admin_panel/' + template, context=context)


def mapped_route_add(request):
    """
    Страница конструктора, которая позволит задавать последовательность остановок,
    Далее, открыть карту и построить промежуточные маршруты,
    Подтвердить и исходранить маршрут в БД.
    :param request:
    :return: Template of constructor
    """

    template_name = 'admin_panel/mapper_route_add.html'
    if request.method == 'GET':
        # route_form = RouteSelectForm(request.GET or None)
        routes = Route.objects.all()
        formset = RoutePlatformFormset(queryset=RoutePoint.objects.none())
    elif request.method == 'POST':
        # route_form = RouteSelectForm(request.POST)
        route_id = request.POST.get('route')
        route = get_object_or_404(Route, pk=route_id)
        formset = RoutePlatformFormset(request.POST)
        platform = PlatformType.objects.get(pk=1)  # default platform name
        platform_endpoint = PlatformType.objects.get(pk=3)  # default platform endpoint name
        last_route_point = None
        if formset.is_valid():
            # route = route_form.save()
            for num, form in enumerate(formset, start=1):
                route_point = form.save(commit=False)
                route_point.latitude = route_point.route_platform.latitude
                route_point.longitude = route_point.route_platform.longitude
                route_point.route = route
                # first iteration
                if num == 1:
                    route_point.route_platform_type = platform_endpoint
                # last iteration
                if num == len(formset):
                    route_point.route_platform_type = platform_endpoint
                route_point.save()
                if last_route_point:
                    last_route_point.next = route_point
                    route_point.prev = last_route_point
                    last_route_point.save()
                    route_point.save()
                last_route_point = route_point
            if request.is_ajax():
                response = serializers.serialize("json", route.points.all())
                return JsonResponse(response, safe=False)
            return redirect('admin_panel_cabinet')
    return render(request, template_name, {
        'routes': routes,
        'formset': formset,
    })


def mapped_route_path_save(request):
    if request.method == 'POST' and request.is_ajax():
        points = json.loads(request.body)
        middle_point_state = False
        current_point = None
        last_point = None
        for p in points:
            if p.get('context') and not middle_point_state:
                middle_point_state = True
                current_point = get_object_or_404(RoutePoint, pk=p['context'].get('id'))
            elif p.get('context'):
                middle_point_state = False
                current_point = get_object_or_404(RoutePoint, pk=p['context'].get('id'))
            elif current_point:
                current_point = RoutePoint(route=current_point.route, latitude=p.get('latitude'), longitude=p.get('longitude'))
                current_point.save()
            if last_point:
                last_point.next = current_point
                current_point.prev = last_point
                last_point.save()
                current_point.save()
            last_point = current_point
        return JsonResponse({'status': 'success'})
    return Http404
