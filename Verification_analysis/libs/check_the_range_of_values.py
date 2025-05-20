from libs.change_cell_color import change_cell_color_orange, change_cell_color


def check_the_range_of_values(point_unit, counter_index):
    coefficient = 0.7
    value = float(point_unit.value)
    column = point_unit.column
    minimum = point_unit.minimum
    maximum = point_unit.maximum
    if minimum <= value <= coefficient * minimum or maximum * coefficient <= value <= maximum:
        change_cell_color_orange(f'{column}{counter_index}')
    elif not minimum <= value <= maximum:
        change_cell_color(f'{column}{counter_index}')
