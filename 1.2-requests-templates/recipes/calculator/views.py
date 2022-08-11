from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def home_view(request):
    return render(request, 'calculator/index.html')


def recipes(request, recipe):
    servings = int(request.GET.get('servings', 1))
    context = {}
    tmp_dict = {}
    for key, val in DATA[recipe].items():
        tmp_dict.setdefault(key, round((val * servings), 2))
    context.setdefault('recipe', tmp_dict)
    return render(request, 'calculator/index.html', context)
