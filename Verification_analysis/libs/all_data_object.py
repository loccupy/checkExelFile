from libs.point_unit import PointUnit


class PathToFile:
    path = None


class AllData1PH:
    path_to_file = None

    serial_number = PointUnit('C', None, None)

    # Active Import
    ib_0_05_for_1_0_active_import = PointUnit('D', -1.5, 1.5)
    ib_0_1_for_1_0_active_import = PointUnit('E', -1, 1)
    ib_1_for_1_0_active_import = PointUnit('F', -1, 1)
    imax_for_1_0_active_import = PointUnit('G', -1, 1)

    ib_0_1_for_0_5_active_import = PointUnit('H', -1.5, 1.5)
    ib_0_2_for_0_5_active_import = PointUnit('I', -1, 1)
    ib_1_for_0_5_active_import = PointUnit('J', -1, 1)
    imax_for_0_5_active_import = PointUnit('K', -1, 1)

    ib_0_1_for_0_8_active_import = PointUnit('L', -1.5, 1.5)
    ib_0_2_for_0_8_active_import = PointUnit('M', -1, 1)
    ib_1_for_0_8_active_import = PointUnit('N', -1, 1)
    imax_for_0_8_active_import = PointUnit('O', -1, 1)

    # Active Export
    ib_0_05_for_1_0_active_export = PointUnit('T', -1.5, 1.5)
    ib_0_1_for_1_0_active_export = PointUnit('U', -1, 1)
    ib_1_for_1_0_active_export = PointUnit('V', -1, 1)
    imax_for_1_0_active_export = PointUnit('W', -1, 1)

    ib_0_1_for_0_5_active_export = PointUnit('X', -1.5, 1.5)
    ib_0_2_for_0_5_active_export = PointUnit('Y', -1, 1)
    ib_1_for_0_5_active_export = PointUnit('Z', -1, 1)
    imax_for_0_5_active_export = PointUnit('AA', -1, 1)

    ib_0_1_for_0_8_active_export = PointUnit('AB', -1.5, 1.5)
    ib_0_2_for_0_8_active_export = PointUnit('AC', -1, 1)
    ib_1_for_0_8_active_export = PointUnit('AD', -1, 1)
    imax_for_0_8_active_export = PointUnit('AE', -1, 1)

    # Reactive Import
    ib_0_05_for_1_0_reactive_import = PointUnit('D', -2.5, 2.5)
    ib_0_1_for_1_0_reactive_import = PointUnit('E', -2, 2)
    ib_1_for_1_0_reactive_import = PointUnit('F', -2, 2)
    imax_for_1_0_reactive_import = PointUnit('G', -2, 2)

    ib_0_1_for_0_5_reactive_import = PointUnit('H', -2.5, 2.5)
    ib_0_2_for_0_5_reactive_import = PointUnit('I', -2, 2)
    ib_1_for_0_5_reactive_import = PointUnit('J', -2, 2)
    imax_for_0_5_reactive_import = PointUnit('K', -2, 2)

    ib_0_2_for_0_25_reactive_import = PointUnit('L', -2.5, 2.5)
    ib_1_for_0_25_reactive_import = PointUnit('M', -2, 2)
    imax_for_0_25_reactive_import = PointUnit('N', -2, 2)

    # Reactive Export
    ib_0_05_for_1_0_reactive_export = PointUnit('S', -2.5, 2.5)
    ib_0_1_for_1_0_reactive_export = PointUnit('T', -2, 2)
    ib_1_for_1_0_reactive_export = PointUnit('U', -2, 2)
    imax_for_1_0_reactive_export = PointUnit('V', -2, 2)

    ib_0_1_for_0_5_reactive_export = PointUnit('W', -2.5, 2.5)
    ib_0_2_for_0_5_reactive_export = PointUnit('X', -2, 2)
    ib_1_for_0_5_reactive_export = PointUnit('Y', -2, 2)
    imax_for_0_5_reactive_export = PointUnit('Z', -2, 2)

    ib_0_2_for_0_25_reactive_export = PointUnit('AA', -2.5, 2.5)
    ib_1_for_0_25_reactive_export = PointUnit('AB', -2, 2)
    imax_for_0_25_reactive_export = PointUnit('AC', -2, 2)


class AllDataTT:
    path_to_file = None

    serial_number = PointUnit('C', None, None)

    # Active Import
    ib_0_05_for_1_0_active_import = PointUnit('D', -1, 1)
    ib_0_1_for_1_0_active_import = PointUnit('E', -1, 1)
    ib_1_for_1_0_active_import = PointUnit('F', -0.5, 0.5)
    imax_for_1_0_active_import = PointUnit('G', -0.5, 0.5)

    ib_0_1_for_0_5_active_import = PointUnit('H', -1, 1)
    ib_0_2_for_0_5_active_import = PointUnit('I', -1, 1)
    ib_1_for_0_5_active_import = PointUnit('J', -0.6, 0.6)
    imax_for_0_5_active_import = PointUnit('K', -0.6, 0.6)

    ib_0_1_for_0_8_active_import = PointUnit('L', -1.5, 1.5)
    ib_0_2_for_0_8_active_import = PointUnit('M', -1.5, 1.5)
    ib_1_for_0_8_active_import = PointUnit('N', -0.6, 0.6)
    imax_for_0_8_active_import = PointUnit('O', -0.6, 0.6)
    # Для фазы А
    ib_0_05_for_1_0_active_import_a = PointUnit('P', -0.6, 0.6)
    ib_1_for_1_0_active_import_a = PointUnit('Q', -0.6, 0.6)
    imax_for_1_0_active_import_a = PointUnit('R', -0.6, 0.6)

    ib_0_1_for_0_5_active_import_a = PointUnit('S', -1, 1)
    ib_1_for_0_5_active_import_a = PointUnit('T', -1, 1)
    imax_for_0_5_active_import_a = PointUnit('U', -1, 1)
    # Для фазы B
    ib_0_05_for_1_0_active_import_b = PointUnit('V', -0.6, 0.6)
    ib_1_for_1_0_active_import_b = PointUnit('W', -0.6, 0.6)
    imax_for_1_0_active_import_b = PointUnit('X', -0.6, 0.6)

    ib_0_1_for_0_5_active_import_b = PointUnit('Y', -1, 1)
    ib_1_for_0_5_active_import_b = PointUnit('Z', -1, 1)
    imax_for_0_5_active_import_b = PointUnit('AA', -1, 1)
    # Для фазы C
    ib_0_05_for_1_0_active_import_c = PointUnit('AB', -0.6, 0.6)
    ib_1_for_1_0_active_import_c = PointUnit('AC', -0.6, 0.6)
    imax_for_1_0_active_import_c = PointUnit('AD', -0.6, 0.6)

    ib_0_1_for_0_5_active_import_c = PointUnit('AE', -1, 1)
    ib_1_for_0_5_active_import_c = PointUnit('AF', -1, 1)
    imax_for_0_5_active_import_c = PointUnit('AG', -1, 1)

    # Active Export
    ib_0_05_for_1_0_active_export = PointUnit('D', -1, 1)
    ib_0_1_for_1_0_active_export = PointUnit('E', -1, 1)
    ib_1_for_1_0_active_export = PointUnit('F', -0.5, 0.5)
    imax_for_1_0_active_export = PointUnit('G', -0.5, 0.5)

    ib_0_1_for_0_5_active_export = PointUnit('H', -1, 1)
    ib_0_2_for_0_5_active_export = PointUnit('I', -1, 1)
    ib_1_for_0_5_active_export = PointUnit('J', -0.6, 0.6)
    imax_for_0_5_active_export = PointUnit('K', -0.6, 0.6)

    ib_0_1_for_0_8_active_export = PointUnit('L', -1, 1)
    ib_0_2_for_0_8_active_export = PointUnit('M', -1, 1)
    ib_1_for_0_8_active_export = PointUnit('N', -0.6, 0.6)
    imax_for_0_8_active_export = PointUnit('O', -0.6, 0.6)
    # Для фазы А
    ib_0_05_for_1_0_active_export_a = PointUnit('P', -0.6, 0.6)
    ib_1_for_1_0_active_export_a = PointUnit('Q', -0.6, 0.6)
    imax_for_1_0_active_export_a = PointUnit('R', -0.6, 0.6)

    ib_0_1_for_0_5_active_export_a = PointUnit('S', -1, 1)
    ib_1_for_0_5_active_export_a = PointUnit('T', -1, 1)
    imax_for_0_5_active_export_a = PointUnit('U', -1, 1)
    # Для фазы B
    ib_0_05_for_1_0_active_export_b = PointUnit('V', -0.6, 0.6)
    ib_1_for_1_0_active_export_b = PointUnit('W', -0.6, 0.6)
    imax_for_1_0_active_export_b = PointUnit('X', -0.6, 0.6)

    ib_0_1_for_0_5_active_export_b = PointUnit('Y', -1, 1)
    ib_1_for_0_5_active_export_b = PointUnit('Z', -1, 1)
    imax_for_0_5_active_export_b = PointUnit('AA', -1, 1)
    # Для фазы C
    ib_0_05_for_1_0_active_export_c = PointUnit('AB', -0.6, 0.6)
    ib_1_for_1_0_active_export_c = PointUnit('AC', -0.6, 0.6)
    imax_for_1_0_active_export_c = PointUnit('AD', -0.6, 0.6)

    ib_0_1_for_0_5_active_export_c = PointUnit('AE', -1, 1)
    ib_1_for_0_5_active_export_c = PointUnit('AF', -1, 1)
    imax_for_0_5_active_export_c = PointUnit('AG', -1, 1)

    # Reactive Import
    ib_0_02_for_1_0_reactive_import = PointUnit('D', -1.5, 1.5)
    ib_0_05_for_1_0_reactive_import = PointUnit('E', -1.5, 1.5)
    ib_1_for_1_0_reactive_import = PointUnit('F', -1, 1)
    imax_for_1_0_reactive_import = PointUnit('G', -1, 1)

    ib_0_05_for_0_5_reactive_import = PointUnit('H', -1.5, 1.5)
    ib_0_1_for_0_5_reactive_import = PointUnit('I', -1.5, 1.5)
    ib_1_for_0_5_reactive_import = PointUnit('J', -1, 1)
    imax_for_0_5_reactive_import = PointUnit('K', -1, 1)

    ib_0_1_for_0_25_reactive_import = PointUnit('L', -1.5, 1.5)
    ib_1_for_0_25_reactive_import = PointUnit('M', -1.5, 1.5)
    imax_for_0_25_reactive_import = PointUnit('N', -1.5, 1.5)
    # Для фазы А
    ib_0_05_for_1_0_reactive_import_a = PointUnit('O', -1.5, 1.5)
    ib_1_for_1_0_reactive_import_a = PointUnit('P', -1.5, 1.5)
    imax_for_1_0_reactive_import_a = PointUnit('Q', -1.5, 1.5)

    ib_0_1_for_0_5_reactive_import_a = PointUnit('R', -1.5, 1.5)
    ib_1_for_0_5_reactive_import_a = PointUnit('S', -1.5, 1.5)
    imax_for_0_5_reactive_import_a = PointUnit('T', -1.5, 1.5)
    # Для фазы В
    ib_0_05_for_1_0_reactive_import_b = PointUnit('U', -1.5, 1.5)
    ib_1_for_1_0_reactive_import_b = PointUnit('V', -1.5, 1.5)
    imax_for_1_0_reactive_import_b = PointUnit('W', -1.5, 1.5)

    ib_0_1_for_0_5_reactive_import_b = PointUnit('X', -1.5, 1.5)
    ib_1_for_0_5_reactive_import_b = PointUnit('Y', -1.5, 1.5)
    imax_for_0_5_reactive_import_b = PointUnit('Z', -1.5, 1.5)
    # Для фазы C
    ib_0_05_for_1_0_reactive_import_c = PointUnit('AA', -1.5, 1.5)
    ib_1_for_1_0_reactive_import_c = PointUnit('AB', -1.5, 1.5)
    imax_for_1_0_reactive_import_c = PointUnit('AC', -1.5, 1.5)

    ib_0_1_for_0_5_reactive_import_c = PointUnit('AD', -1.5, 1.5)
    ib_1_for_0_5_reactive_import_c = PointUnit('AE', -1.5, 1.5)
    imax_for_0_5_reactive_import_c = PointUnit('AF', -1.5, 1.5)

    # Reactive Export
    ib_0_02_for_1_0_reactive_export = PointUnit('D', -1.5, 1.5)
    ib_0_05_for_1_0_reactive_export = PointUnit('E', -1.5, 1.5)
    ib_1_for_1_0_reactive_export = PointUnit('F', -1, 1)
    imax_for_1_0_reactive_export = PointUnit('G', -1, 1)

    ib_0_05_for_0_5_reactive_export = PointUnit('H', -1.5, 1.5)
    ib_0_1_for_0_5_reactive_export = PointUnit('I', -1.5, 1.5)
    ib_1_for_0_5_reactive_export = PointUnit('J', -1, 1)
    imax_for_0_5_reactive_export = PointUnit('K', -1, 1)

    ib_0_1_for_0_25_reactive_export = PointUnit('L', -1.5, 1.5)
    ib_1_for_0_25_reactive_export = PointUnit('M', -1.5, 1.5)
    imax_for_0_25_reactive_export = PointUnit('N', -1.5, 1.5)
    # Для фазы А
    ib_0_05_for_1_0_reactive_export_a = PointUnit('O', -1.5, 1.5)
    ib_1_for_1_0_reactive_export_a = PointUnit('P', -1.5, 1.5)
    imax_for_1_0_reactive_export_a = PointUnit('Q', -1.5, 1.5)

    ib_0_1_for_0_5_reactive_export_a = PointUnit('R', -1.5, 1.5)
    ib_1_for_0_5_reactive_export_a = PointUnit('S', -1.5, 1.5)
    imax_for_0_5_reactive_export_a = PointUnit('T', -1.5, 1.5)
    # Для фазы B
    ib_0_05_for_1_0_reactive_export_b = PointUnit('U', -1.5, 1.5)
    ib_1_for_1_0_reactive_export_b = PointUnit('V', -1.5, 1.5)
    imax_for_1_0_reactive_export_b = PointUnit('W', -1.5, 1.5)

    ib_0_1_for_0_5_reactive_export_b = PointUnit('X', -1.5, 1.5)
    ib_1_for_0_5_reactive_export_b = PointUnit('Y', -1.5, 1.5)
    imax_for_0_5_reactive_export_b = PointUnit('Z', -1.5, 1.5)
    # Для фазы C
    ib_0_05_for_1_0_reactive_export_c = PointUnit('AA', -1.5, 1.5)
    ib_1_for_1_0_reactive_export_c = PointUnit('AB', -1.5, 1.5)
    imax_for_1_0_reactive_export_c = PointUnit('AC', -1.5, 1.5)

    ib_0_1_for_0_5_reactive_export_c = PointUnit('AD', -1.5, 1.5)
    ib_1_for_0_5_reactive_export_c = PointUnit('AE', -1.5, 1.5)
    imax_for_0_5_reactive_export_c = PointUnit('AF', -1.5, 1.5)


class AllData3PH:
    path_to_file = None

    serial_number = PointUnit('C', None, None)

    # Active Import
    ib_0_05_for_1_0_active_import = PointUnit('D', -1.5, 1.5)
    ib_0_1_for_1_0_active_import = PointUnit('E', -1.5, 1.5)
    ib_1_for_1_0_active_import = PointUnit('F', -1, 1)
    imax_for_1_0_active_import = PointUnit('G', -1, 1)

    ib_0_1_for_0_5_active_import = PointUnit('H', -1.5, 1.5)
    ib_0_2_for_0_5_active_import = PointUnit('I', -1.5, 1.5)
    ib_1_for_0_5_active_import = PointUnit('J', -1, 1)
    imax_for_0_5_active_import = PointUnit('K', -1, 1)

    ib_0_1_for_0_8_active_import = PointUnit('L', -1.5, 1.5)
    ib_0_2_for_0_8_active_import = PointUnit('M', -1.5, 1.5)
    ib_1_for_0_8_active_import = PointUnit('N', -1, 1)
    imax_for_0_8_active_import = PointUnit('O', -1, 1)
    # Для фазы А
    ib_0_05_for_1_0_active_import_a = PointUnit('P', -2, 2)
    ib_1_for_1_0_active_import_a = PointUnit('Q', -2, 2)
    imax_for_1_0_active_import_a = PointUnit('R', -2, 2)

    ib_0_1_for_0_5_active_import_a = PointUnit('S', -2, 2)
    ib_1_for_0_5_active_import_a = PointUnit('T', -2, 2)
    imax_for_0_5_active_import_a = PointUnit('U', -2, 2)
    # Для фазы B
    ib_0_05_for_1_0_active_import_b = PointUnit('V', -2, 2)
    ib_1_for_1_0_active_import_b = PointUnit('W', -2, 2)
    imax_for_1_0_active_import_b = PointUnit('X', -2, 2)

    ib_0_1_for_0_5_active_import_b = PointUnit('Y', -2, 2)
    ib_1_for_0_5_active_import_b = PointUnit('Z', -2, 2)
    imax_for_0_5_active_import_b = PointUnit('AA', -2, 2)
    # Для фазы C
    ib_0_05_for_1_0_active_import_c = PointUnit('AB', -2, 2)
    ib_1_for_1_0_active_import_c = PointUnit('AC', -2, 2)
    imax_for_1_0_active_import_c = PointUnit('AD', -2, 2)

    ib_0_1_for_0_5_active_import_c = PointUnit('AE', -2, 2)
    ib_1_for_0_5_active_import_c = PointUnit('AF', -2, 2)
    imax_for_0_5_active_import_c = PointUnit('AG', -2, 2)

    # Active Export
    ib_0_05_for_1_0_active_export = PointUnit('D', -1.5, 1.5)
    ib_0_1_for_1_0_active_export = PointUnit('E', -1.5, 1.5)
    ib_1_for_1_0_active_export = PointUnit('F', -1, 1)
    imax_for_1_0_active_export = PointUnit('G', -1, 1)

    ib_0_1_for_0_5_active_export = PointUnit('H', -1.5, 1.5)
    ib_0_2_for_0_5_active_export = PointUnit('I', -1.5, 1.5)
    ib_1_for_0_5_active_export = PointUnit('J', -1, 1)
    imax_for_0_5_active_export = PointUnit('K', -1, 1)

    ib_0_1_for_0_8_active_export = PointUnit('L', -1.5, 1.5)
    ib_0_2_for_0_8_active_export = PointUnit('M', -1.5, 1.5)
    ib_1_for_0_8_active_export = PointUnit('N', -1, 1)
    imax_for_0_8_active_export = PointUnit('O', -1, 1)
    # Для фазы А
    ib_0_05_for_1_0_active_export_a = PointUnit('P', -2, 2)
    ib_1_for_1_0_active_export_a = PointUnit('Q', -2, 2)
    imax_for_1_0_active_export_a = PointUnit('R', -2, 2)

    ib_0_1_for_0_5_active_export_a = PointUnit('S', -2, 2)
    ib_1_for_0_5_active_export_a = PointUnit('T', -2, 2)
    imax_for_0_5_active_export_a = PointUnit('U', -2, 2)
    # Для фазы B
    ib_0_05_for_1_0_active_export_b = PointUnit('V', -2, 2)
    ib_1_for_1_0_active_export_b = PointUnit('W', -2, 2)
    imax_for_1_0_active_export_b = PointUnit('X', -2, 2)

    ib_0_1_for_0_5_active_export_b = PointUnit('Y', -2, 2)
    ib_1_for_0_5_active_export_b = PointUnit('Z', -2, 2)
    imax_for_0_5_active_export_b = PointUnit('AA', -2, 2)
    # Для фазы C
    ib_0_05_for_1_0_active_export_c = PointUnit('AB', -2, 2)
    ib_1_for_1_0_active_export_c = PointUnit('AC', -2, 2)
    imax_for_1_0_active_export_c = PointUnit('AD', -2, 2)

    ib_0_1_for_0_5_active_export_c = PointUnit('AE', -2, 2)
    ib_1_for_0_5_active_export_c = PointUnit('AF', -2, 2)
    imax_for_0_5_active_export_c = PointUnit('AG', -2, 2)

    # Reactive Import
    ib_0_02_for_1_0_reactive_import = PointUnit('D', -2.5, 2.5)
    ib_0_05_for_1_0_reactive_import = PointUnit('E', -2.5, 2.5)
    ib_1_for_1_0_reactive_import = PointUnit('F', -2, 2)
    imax_for_1_0_reactive_import = PointUnit('G', -2, 2)

    ib_0_05_for_0_5_reactive_import = PointUnit('H', -2.5, 2.5)
    ib_0_1_for_0_5_reactive_import = PointUnit('I', -2.5, 2.5)
    ib_1_for_0_5_reactive_import = PointUnit('J', -2, 2)
    imax_for_0_5_reactive_import = PointUnit('K', -2, 2)

    ib_0_1_for_0_25_reactive_import = PointUnit('L', -2.5, 2.5)
    ib_1_for_0_25_reactive_import = PointUnit('M', -2.5, 2.5)
    imax_for_0_25_reactive_import = PointUnit('N', -2.5, 2.5)
    # Для фазы А
    ib_0_05_for_1_0_reactive_import_a = PointUnit('O', -3, 3)
    ib_1_for_1_0_reactive_import_a = PointUnit('P', -3, 3)
    imax_for_1_0_reactive_import_a = PointUnit('Q', -3, 3)

    ib_0_1_for_0_5_reactive_import_a = PointUnit('R', -3, 3)
    ib_1_for_0_5_reactive_import_a = PointUnit('S', -3, 3)
    imax_for_0_5_reactive_import_a = PointUnit('T', -3, 3)
    # Для фазы В
    ib_0_05_for_1_0_reactive_import_b = PointUnit('U', -3, 3)
    ib_1_for_1_0_reactive_import_b = PointUnit('V', -3, 3)
    imax_for_1_0_reactive_import_b = PointUnit('W', -3, 3)

    ib_0_1_for_0_5_reactive_import_b = PointUnit('X', -3, 3)
    ib_1_for_0_5_reactive_import_b = PointUnit('Y', -3, 3)
    imax_for_0_5_reactive_import_b = PointUnit('Z', -3, 3)
    # Для фазы C
    ib_0_05_for_1_0_reactive_import_c = PointUnit('AA', -3, 3)
    ib_1_for_1_0_reactive_import_c = PointUnit('AB', -3, 3)
    imax_for_1_0_reactive_import_c = PointUnit('AC', -3, 3)

    ib_0_1_for_0_5_reactive_import_c = PointUnit('AD', -3, 3)
    ib_1_for_0_5_reactive_import_c = PointUnit('AE', -3, 3)
    imax_for_0_5_reactive_import_c = PointUnit('AF', -3, 3)

    # Reactive Export
    ib_0_02_for_1_0_reactive_export = PointUnit('D', -2.5, 2.5)
    ib_0_05_for_1_0_reactive_export = PointUnit('E', -2.5, 2.5)
    ib_1_for_1_0_reactive_export = PointUnit('F', -2, 2)
    imax_for_1_0_reactive_export = PointUnit('G', -2, 2)

    ib_0_05_for_0_5_reactive_export = PointUnit('H', -2.5, 2.5)
    ib_0_1_for_0_5_reactive_export = PointUnit('I', -2.5, 2.5)
    ib_1_for_0_5_reactive_export = PointUnit('J', -2, 2)
    imax_for_0_5_reactive_export = PointUnit('K', -2, 2)

    ib_0_1_for_0_25_reactive_export = PointUnit('L', -2.5, 2.5)
    ib_1_for_0_25_reactive_export = PointUnit('M', -2.5, 2.5)
    imax_for_0_25_reactive_export = PointUnit('N', -2.5, 2.5)
    # Для фазы А
    ib_0_05_for_1_0_reactive_export_a = PointUnit('O', -3, 3)
    ib_1_for_1_0_reactive_export_a = PointUnit('P', -3, 3)
    imax_for_1_0_reactive_export_a = PointUnit('Q', -3, 3)

    ib_0_1_for_0_5_reactive_export_a = PointUnit('R', -3, 3)
    ib_1_for_0_5_reactive_export_a = PointUnit('S', -3, 3)
    imax_for_0_5_reactive_export_a = PointUnit('T', -3, 3)
    # Для фазы B
    ib_0_05_for_1_0_reactive_export_b = PointUnit('U', -3, 3)
    ib_1_for_1_0_reactive_export_b = PointUnit('V', -3, 3)
    imax_for_1_0_reactive_export_b = PointUnit('W', -3, 3)

    ib_0_1_for_0_5_reactive_export_b = PointUnit('X', -3, 3)
    ib_1_for_0_5_reactive_export_b = PointUnit('Y', -3, 3)
    imax_for_0_5_reactive_export_b = PointUnit('Z', -3, 3)
    # Для фазы C
    ib_0_05_for_1_0_reactive_export_c = PointUnit('AA', -3, 3)
    ib_1_for_1_0_reactive_export_c = PointUnit('AB', -3, 3)
    imax_for_1_0_reactive_export_c = PointUnit('AC', -3, 3)

    ib_0_1_for_0_5_reactive_export_c = PointUnit('AD', -3, 3)
    ib_1_for_0_5_reactive_export_c = PointUnit('AE', -3, 3)
    imax_for_0_5_reactive_export_c = PointUnit('AF', -3, 3)
