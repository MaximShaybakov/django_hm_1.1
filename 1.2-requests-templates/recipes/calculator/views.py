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


def recipes(request, name_dish: str):
    if name_dish in DATA:
        recipe = DATA[name_dish]
    servings = int(request.GET.get('servings', 1))
    if name_dish == 'omlet':
        context = {
            'recipe': {
                'ингредиент1': recipe['яйца, шт'] * servings,
                'ингредиент2': recipe['молоко, л'] * servings,
                'ингредиент3': recipe['соль, ч.л.'] * servings,

            }
        }
    elif name_dish == 'pasta':
        context = {
            'recipe': {
                'ингредиент1': recipe['макароны, г'] * servings,
                'ингредиент2': recipe['сыр, г'] * servings,

            }
        }
    elif name_dish == 'buter':
        context = {
            'recipe': {
                'ингредиент1': recipe['хлеб, ломтик'] * servings,
                'ингредиент2': recipe['колбаса, ломтик'] * servings,
                'ингредиент3': recipe['сыр, ломтик'] * servings,
                'ингредиент4': recipe['помидор, ломтик'] * servings,

            }
        }
    return render(request, 'calculator/index.html', context)





# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
