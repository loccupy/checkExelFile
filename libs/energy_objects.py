from libs.all_data_object import AllData1PH
from libs.check_the_range_of_values import check_the_range_of_values


class ActiveEnergy:
    def __init__(self, index, sheet):
        self.index = index
        # self.sheet = load_workbook(get_path_to_exel_file()).active
        self.sheet = sheet

    def _get_data_from_table(self, column):
        try:
            data = self.sheet[f"{column}{self.index}"]
            return data.value
        except Exception as e:
            print(e.args)

    def read_exel_and_fill_serial_number(self, data_object):
        try:
            data_object.serial_number.value = self._get_data_from_table(data_object.serial_number.column)
        except Exception as e:
            print(e.args)

    def read_exel_and_fill_data_for_1ph_active_import(self):
        # Для Cos=1.0
        AllData1PH.ib_0_05_for_1_0_active_import.value = self._get_data_from_table(AllData1PH.ib_0_05_for_1_0_active_import.column)
        AllData1PH.ib_0_1_for_1_0_active_import.value = self._get_data_from_table(AllData1PH.ib_0_1_for_1_0_active_import.column)
        AllData1PH.ib_1_for_1_0_active_import.value = self._get_data_from_table(AllData1PH.ib_1_for_1_0_active_import.column)
        AllData1PH.imax_for_1_0_active_import.value = self._get_data_from_table(AllData1PH.imax_for_1_0_active_import.column)
        # Для Cos=0.5L
        AllData1PH.ib_0_1_for_0_5_active_import.value = self._get_data_from_table(AllData1PH.ib_0_1_for_0_5_active_import.column)
        AllData1PH.ib_0_2_for_0_5_active_import.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_5_active_import.column)
        AllData1PH.ib_1_for_0_5_active_import.value = self._get_data_from_table(AllData1PH.ib_1_for_0_5_active_import.column)
        AllData1PH.imax_for_0_5_active_import.value = self._get_data_from_table(AllData1PH.imax_for_0_5_active_import.column)
        # Для Cos=0.8L
        AllData1PH.ib_0_1_for_0_8_active_import.value = self._get_data_from_table(AllData1PH.ib_0_1_for_0_8_active_import.column)
        AllData1PH.ib_0_2_for_0_8_active_import.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_8_active_import.column)
        AllData1PH.ib_1_for_0_8_active_import.value = self._get_data_from_table(AllData1PH.ib_1_for_0_8_active_import.column)
        AllData1PH.imax_for_0_8_active_import.value = self._get_data_from_table(AllData1PH.imax_for_0_8_active_import.column)

    def read_exel_and_fill_data_for_1ph_active_export(self):
        # Для Cos=1.0
        AllData1PH.ib_0_05_for_1_0_active_export.value = self._get_data_from_table(AllData1PH.ib_0_05_for_1_0_active_export.column)
        AllData1PH.ib_0_1_for_1_0_active_export.value = self._get_data_from_table(AllData1PH.ib_0_1_for_1_0_active_export.column)
        AllData1PH.ib_1_for_1_0_active_export.value = self._get_data_from_table(AllData1PH.ib_1_for_1_0_active_export.column)
        AllData1PH.imax_for_1_0_active_export.value = self._get_data_from_table(AllData1PH.imax_for_1_0_active_export.column)
        # Для Cos=0.5L
        AllData1PH.ib_0_1_for_0_5_active_export.value = self._get_data_from_table(AllData1PH.ib_0_1_for_0_5_active_export.column)
        AllData1PH.ib_0_2_for_0_5_active_export.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_5_active_export.column)
        AllData1PH.ib_1_for_0_5_active_export.value = self._get_data_from_table(AllData1PH.ib_1_for_0_5_active_export.column)
        AllData1PH.imax_for_0_5_active_export.value = self._get_data_from_table(AllData1PH.imax_for_0_5_active_export.column)
        # Для Cos=0.8L
        AllData1PH.ib_0_1_for_0_8_active_export.value = self._get_data_from_table(AllData1PH.ib_0_1_for_0_8_active_export.column)
        AllData1PH.ib_0_2_for_0_8_active_export.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_8_active_export.column)
        AllData1PH.ib_1_for_0_8_active_export.value = self._get_data_from_table(AllData1PH.ib_1_for_0_8_active_export.column)
        AllData1PH.imax_for_0_8_active_export.value = self._get_data_from_table(AllData1PH.imax_for_0_8_active_export.column)

    def read_exel_and_fill_data_for_3ph_active_import(self, data_object):
        # Для Cos=1.0
        data_object.ib_0_05_for_1_0_active_import.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_import.column)
        data_object.ib_0_1_for_1_0_active_import.value = self._get_data_from_table(data_object.ib_0_1_for_1_0_active_import.column)
        data_object.ib_1_for_1_0_active_import.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_import.column)
        data_object.imax_for_1_0_active_import.value = self._get_data_from_table(data_object.imax_for_1_0_active_import.column)
        # Для Cos=0.5L
        data_object.ib_0_1_for_0_5_active_import.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_import.column)
        data_object.ib_0_2_for_0_5_active_import.value = self._get_data_from_table(data_object.ib_0_2_for_0_5_active_import.column)
        data_object.ib_1_for_0_5_active_import.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_import.column)
        data_object.imax_for_0_5_active_import.value = self._get_data_from_table(data_object.imax_for_0_5_active_import.column)
        # Для Cos=0.8L
        data_object.ib_0_1_for_0_8_active_import.value = self._get_data_from_table(data_object.ib_0_1_for_0_8_active_import.column)
        data_object.ib_0_2_for_0_8_active_import.value = self._get_data_from_table(data_object.ib_0_2_for_0_8_active_import.column)
        data_object.ib_1_for_0_8_active_import.value = self._get_data_from_table(data_object.ib_1_for_0_8_active_import.column)
        data_object.imax_for_0_8_active_import.value = self._get_data_from_table(data_object.imax_for_0_8_active_import.column)

        # Для фазы А
        data_object.ib_0_05_for_1_0_active_import_a.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_import_a.column)
        data_object.ib_1_for_1_0_active_import_a.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_import_a.column)
        data_object.imax_for_1_0_active_import_a.value = self._get_data_from_table(data_object.imax_for_1_0_active_import_a.column)

        data_object.ib_0_1_for_0_5_active_import_a.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_import_a.column)
        data_object.ib_1_for_0_5_active_import_a.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_import_a.column)
        data_object.imax_for_0_5_active_import_a.value = self._get_data_from_table(data_object.imax_for_0_5_active_import_a.column)

        # Для фазы В
        data_object.ib_0_05_for_1_0_active_import_b.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_import_b.column)
        data_object.ib_1_for_1_0_active_import_b.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_import_b.column)
        data_object.imax_for_1_0_active_import_b.value = self._get_data_from_table(data_object.imax_for_1_0_active_import_b.column)

        data_object.ib_0_1_for_0_5_active_import_b.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_import_b.column)
        data_object.ib_1_for_0_5_active_import_b.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_import_b.column)
        data_object.imax_for_0_5_active_import_b.value = self._get_data_from_table(data_object.imax_for_0_5_active_import_b.column)
        # Для фазы C
        data_object.ib_0_05_for_1_0_active_import_c.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_import_c.column)
        data_object.ib_1_for_1_0_active_import_c.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_import_c.column)
        data_object.imax_for_1_0_active_import_c.value = self._get_data_from_table(data_object.imax_for_1_0_active_import_c.column)

        data_object.ib_0_1_for_0_5_active_import_c.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_import_c.column)
        data_object.ib_1_for_0_5_active_import_c.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_import_c.column)
        data_object.imax_for_0_5_active_import_c.value = self._get_data_from_table(data_object.imax_for_0_5_active_import_c.column)

    def read_exel_and_fill_data_for_3ph_active_export(self, data_object):
        # Для Cos=1.0
        data_object.ib_0_05_for_1_0_active_export.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_export.column)
        data_object.ib_0_1_for_1_0_active_export.value = self._get_data_from_table(data_object.ib_0_1_for_1_0_active_export.column)
        data_object.ib_1_for_1_0_active_export.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_export.column)
        data_object.imax_for_1_0_active_export.value = self._get_data_from_table(data_object.imax_for_1_0_active_export.column)
        # Для Cos=0.5L
        data_object.ib_0_1_for_0_5_active_export.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_export.column)
        data_object.ib_0_2_for_0_5_active_export.value = self._get_data_from_table(data_object.ib_0_2_for_0_5_active_export.column)
        data_object.ib_1_for_0_5_active_export.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_export.column)
        data_object.imax_for_0_5_active_export.value = self._get_data_from_table(data_object.imax_for_0_5_active_export.column)
        # Для Cos=0.8L
        data_object.ib_0_1_for_0_8_active_export.value = self._get_data_from_table(data_object.ib_0_1_for_0_8_active_export.column)
        data_object.ib_0_2_for_0_8_active_export.value = self._get_data_from_table(data_object.ib_0_2_for_0_8_active_export.column)
        data_object.ib_1_for_0_8_active_export.value = self._get_data_from_table(data_object.ib_1_for_0_8_active_export.column)
        data_object.imax_for_0_8_active_export.value = self._get_data_from_table(data_object.imax_for_0_8_active_export.column)

        # Для фазы А
        data_object.ib_0_05_for_1_0_active_export_a.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_export_a.column)
        data_object.ib_1_for_1_0_active_export_a.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_export_a.column)
        data_object.imax_for_1_0_active_export_a.value = self._get_data_from_table(data_object.imax_for_1_0_active_export_a.column)

        data_object.ib_0_1_for_0_5_active_export_a.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_export_a.column)
        data_object.ib_1_for_0_5_active_export_a.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_export_a.column)
        data_object.imax_for_0_5_active_export_a.value = self._get_data_from_table(data_object.imax_for_0_5_active_export_a.column)

        # Для фазы В
        data_object.ib_0_05_for_1_0_active_export_b.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_export_b.column)
        data_object.ib_1_for_1_0_active_export_b.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_export_b.column)
        data_object.imax_for_1_0_active_export_b.value = self._get_data_from_table(data_object.imax_for_1_0_active_export_b.column)

        data_object.ib_0_1_for_0_5_active_export_b.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_export_b.column)
        data_object.ib_1_for_0_5_active_export_b.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_export_b.column)
        data_object.imax_for_0_5_active_export_b.value = self._get_data_from_table(data_object.imax_for_0_5_active_export_b.column)
        # Для фазы C
        data_object.ib_0_05_for_1_0_active_export_c.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_active_export_c.column)
        data_object.ib_1_for_1_0_active_export_c.value = self._get_data_from_table(data_object.ib_1_for_1_0_active_export_c.column)
        data_object.imax_for_1_0_active_export_c.value = self._get_data_from_table(data_object.imax_for_1_0_active_export_c.column)

        data_object.ib_0_1_for_0_5_active_export_c.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_active_export_c.column)
        data_object.ib_1_for_0_5_active_export_c.value = self._get_data_from_table(data_object.ib_1_for_0_5_active_export_c.column)
        data_object.imax_for_0_5_active_export_c.value = self._get_data_from_table(data_object.imax_for_0_5_active_export_c.column)

    def check_data_for_1ph_active_energy_import(self):
        check_the_range_of_values(AllData1PH.ib_0_05_for_1_0_active_import, self.index)
        check_the_range_of_values(AllData1PH.ib_0_1_for_1_0_active_import, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_1_0_active_import, self.index)
        check_the_range_of_values(AllData1PH.imax_for_1_0_active_import, self.index)

        check_the_range_of_values(AllData1PH.ib_0_1_for_0_5_active_import, self.index)
        check_the_range_of_values(AllData1PH.ib_0_2_for_0_5_active_import, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_5_active_import, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_5_active_import, self.index)

        check_the_range_of_values(AllData1PH.ib_0_1_for_0_8_active_import, self.index)
        check_the_range_of_values(AllData1PH.ib_0_2_for_0_8_active_import, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_8_active_import, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_8_active_import, self.index)

    def check_data_for_1ph_active_energy_export(self):
        check_the_range_of_values(AllData1PH.ib_0_05_for_1_0_active_export, self.index)
        check_the_range_of_values(AllData1PH.ib_0_1_for_1_0_active_export, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_1_0_active_export, self.index)
        check_the_range_of_values(AllData1PH.imax_for_1_0_active_export, self.index)

        check_the_range_of_values(AllData1PH.ib_0_1_for_0_5_active_export, self.index)
        check_the_range_of_values(AllData1PH.ib_0_2_for_0_5_active_export, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_5_active_export, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_5_active_export, self.index)

        check_the_range_of_values(AllData1PH.ib_0_1_for_0_8_active_export, self.index)
        check_the_range_of_values(AllData1PH.ib_0_2_for_0_8_active_export, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_8_active_export, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_8_active_export, self.index)

    def check_data_for_3ph_active_energy_import(self, data_object):
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_import, self.index)
        check_the_range_of_values(data_object.ib_0_1_for_1_0_active_import, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_import, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_import, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_import, self.index)
        check_the_range_of_values(data_object.ib_0_2_for_0_5_active_import, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_import, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_import, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_8_active_import, self.index)
        check_the_range_of_values(data_object.ib_0_2_for_0_8_active_import, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_8_active_import, self.index)
        check_the_range_of_values(data_object.imax_for_0_8_active_import, self.index)
        # Для фазы А
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_import_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_import_a, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_import_a, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_import_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_import_a, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_import_a, self.index)
        # Для фазы B
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_import_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_import_b, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_import_b, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_import_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_import_b, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_import_b, self.index)
        # Для фазы C
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_import_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_import_c, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_import_c, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_import_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_import_c, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_import_c, self.index)

    def check_data_for_3ph_active_energy_export(self, data_object):
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_export, self.index)
        check_the_range_of_values(data_object.ib_0_1_for_1_0_active_export, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_export, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_export, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_export, self.index)
        check_the_range_of_values(data_object.ib_0_2_for_0_5_active_export, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_export, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_export, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_8_active_export, self.index)
        check_the_range_of_values(data_object.ib_0_2_for_0_8_active_export, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_8_active_export, self.index)
        check_the_range_of_values(data_object.imax_for_0_8_active_export, self.index)

        # Для фазы А
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_export_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_export_a, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_export_a, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_export_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_export_a, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_export_a, self.index)
        # Для фазы B
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_export_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_export_b, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_export_b, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_export_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_export_b, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_export_b, self.index)
        # Для фазы C
        check_the_range_of_values(data_object.ib_0_05_for_1_0_active_export_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_active_export_c, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_active_export_c, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_active_export_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_active_export_c, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_active_export_c, self.index)


class ReactiveEnergy:
    def __init__(self, index, sheet):
        self.index = index
        self.sheet = sheet

    def _get_data_from_table(self, column):
        try:
            data = self.sheet[f"{column}{self.index}"]
            return data.value
        except Exception as e:
            print(e.args)

    def read_exel_and_fill_data_for_1ph_reactive_import(self):
        # Для Sin=1.0
        AllData1PH.ib_0_05_for_1_0_reactive_import.value = self._get_data_from_table(AllData1PH.ib_0_05_for_1_0_reactive_import.column)
        AllData1PH.ib_0_1_for_1_0_reactive_import.value = self._get_data_from_table(AllData1PH.ib_0_1_for_1_0_reactive_import.column)
        AllData1PH.ib_1_for_1_0_reactive_import.value = self._get_data_from_table(AllData1PH.ib_1_for_1_0_reactive_import.column)
        AllData1PH.imax_for_1_0_reactive_import.value = self._get_data_from_table(AllData1PH.imax_for_1_0_reactive_import.column)
        # Для Sin=0.5L
        AllData1PH.ib_0_1_for_0_5_reactive_import.value = self._get_data_from_table(AllData1PH.ib_0_1_for_0_5_reactive_import.column)
        AllData1PH.ib_0_2_for_0_5_reactive_import.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_5_reactive_import.column)
        AllData1PH.ib_1_for_0_5_reactive_import.value = self._get_data_from_table(AllData1PH.ib_1_for_0_5_reactive_import.column)
        AllData1PH.imax_for_0_5_reactive_import.value = self._get_data_from_table(AllData1PH.imax_for_0_5_reactive_import.column)
        # Для Sin=0.25L
        AllData1PH.ib_0_2_for_0_25_reactive_import.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_25_reactive_import.column)
        AllData1PH.ib_1_for_0_25_reactive_import.value = self._get_data_from_table(AllData1PH.ib_1_for_0_25_reactive_import.column)
        AllData1PH.imax_for_0_25_reactive_import.value = self._get_data_from_table(AllData1PH.imax_for_0_25_reactive_import.column)

    def read_exel_and_fill_data_for_3ph_reactive_import(self, data_object):
        # Для Cos=1.0
        data_object.ib_0_02_for_1_0_reactive_import.value = self._get_data_from_table(data_object.ib_0_02_for_1_0_reactive_import.column)
        data_object.ib_0_05_for_1_0_reactive_import.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_import.column)
        data_object.ib_1_for_1_0_reactive_import.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_import.column)
        data_object.imax_for_1_0_reactive_import.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_import.column)
        # Для Cos=0.5L
        data_object.ib_0_05_for_0_5_reactive_import.value = self._get_data_from_table(data_object.ib_0_05_for_0_5_reactive_import.column)
        data_object.ib_0_1_for_0_5_reactive_import.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_import.column)
        data_object.ib_1_for_0_5_reactive_import.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_import.column)
        data_object.imax_for_0_5_reactive_import.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_import.column)
        # Для Cos=0.25L
        data_object.ib_0_1_for_0_25_reactive_import.value = self._get_data_from_table(data_object.ib_0_1_for_0_25_reactive_import.column)
        data_object.ib_1_for_0_25_reactive_import.value = self._get_data_from_table(data_object.ib_1_for_0_25_reactive_import.column)
        data_object.imax_for_0_25_reactive_import.value = self._get_data_from_table(data_object.imax_for_0_25_reactive_import.column)

        # Для фазы А
        data_object.ib_0_05_for_1_0_reactive_import_a.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_import_a.column)
        data_object.ib_1_for_1_0_reactive_import_a.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_import_a.column)
        data_object.imax_for_1_0_reactive_import_a.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_import_a.column)

        data_object.ib_0_1_for_0_5_reactive_import_a.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_import_a.column)
        data_object.ib_1_for_0_5_reactive_import_a.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_import_a.column)
        data_object.imax_for_0_5_reactive_import_a.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_import_a.column)

        # Для фазы В
        data_object.ib_0_05_for_1_0_reactive_import_b.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_import_b.column)
        data_object.ib_1_for_1_0_reactive_import_b.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_import_b.column)
        data_object.imax_for_1_0_reactive_import_b.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_import_b.column)

        data_object.ib_0_1_for_0_5_reactive_import_b.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_import_b.column)
        data_object.ib_1_for_0_5_reactive_import_b.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_import_b.column)
        data_object.imax_for_0_5_reactive_import_b.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_import_b.column)
        # Для фазы C
        data_object.ib_0_05_for_1_0_reactive_import_c.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_import_c.column)
        data_object.ib_1_for_1_0_reactive_import_c.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_import_c.column)
        data_object.imax_for_1_0_reactive_import_c.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_import_c.column)

        data_object.ib_0_1_for_0_5_reactive_import_c.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_import_c.column)
        data_object.ib_1_for_0_5_reactive_import_c.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_import_c.column)
        data_object.imax_for_0_5_reactive_import_c.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_import_c.column)

    def read_exel_and_fill_data_for_1ph_reactive_export(self):
        # Для Sin=1.0
        AllData1PH.ib_0_05_for_1_0_reactive_export.value = self._get_data_from_table(AllData1PH.ib_0_05_for_1_0_reactive_export.column)
        AllData1PH.ib_0_1_for_1_0_reactive_export.value = self._get_data_from_table(AllData1PH.ib_0_1_for_1_0_reactive_export.column)
        AllData1PH.ib_1_for_1_0_reactive_export.value = self._get_data_from_table(AllData1PH.ib_1_for_1_0_reactive_export.column)
        AllData1PH.imax_for_1_0_reactive_export.value = self._get_data_from_table(AllData1PH.imax_for_1_0_reactive_export.column)
        # Для Sin=0.5L
        AllData1PH.ib_0_1_for_0_5_reactive_export.value = self._get_data_from_table(AllData1PH.ib_0_1_for_0_5_reactive_export.column)
        AllData1PH.ib_0_2_for_0_5_reactive_export.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_5_reactive_export.column)
        AllData1PH.ib_1_for_0_5_reactive_export.value = self._get_data_from_table(AllData1PH.ib_1_for_0_5_reactive_export.column)
        AllData1PH.imax_for_0_5_reactive_export.value = self._get_data_from_table(AllData1PH.imax_for_0_5_reactive_export.column)
        # Для Sin=0.25L
        AllData1PH.ib_0_2_for_0_25_reactive_export.value = self._get_data_from_table(AllData1PH.ib_0_2_for_0_25_reactive_export.column)
        AllData1PH.ib_1_for_0_25_reactive_export.value = self._get_data_from_table(AllData1PH.ib_1_for_0_25_reactive_export.column)
        AllData1PH.imax_for_0_25_reactive_export.value = self._get_data_from_table(AllData1PH.imax_for_0_25_reactive_export.column)

    def read_exel_and_fill_data_for_3ph_reactive_export(self, data_object):
        # Для Cos=1.0
        data_object.ib_0_02_for_1_0_reactive_export.value = self._get_data_from_table(data_object.ib_0_02_for_1_0_reactive_export.column)
        data_object.ib_0_05_for_1_0_reactive_export.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_export.column)
        data_object.ib_1_for_1_0_reactive_export.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_export.column)
        data_object.imax_for_1_0_reactive_export.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_export.column)
        # Для Cos=0.5L
        data_object.ib_0_05_for_0_5_reactive_export.value = self._get_data_from_table(data_object.ib_0_05_for_0_5_reactive_export.column)
        data_object.ib_0_1_for_0_5_reactive_export.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_export.column)
        data_object.ib_1_for_0_5_reactive_export.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_export.column)
        data_object.imax_for_0_5_reactive_export.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_export.column)
        # Для Cos=0.25L
        data_object.ib_0_1_for_0_25_reactive_export.value = self._get_data_from_table(data_object.ib_0_1_for_0_25_reactive_export.column)
        data_object.ib_1_for_0_25_reactive_export.value = self._get_data_from_table(data_object.ib_1_for_0_25_reactive_export.column)
        data_object.imax_for_0_25_reactive_export.value = self._get_data_from_table(data_object.imax_for_0_25_reactive_export.column)

        # Для фазы А
        data_object.ib_0_05_for_1_0_reactive_export_a.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_export_a.column)
        data_object.ib_1_for_1_0_reactive_export_a.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_export_a.column)
        data_object.imax_for_1_0_reactive_export_a.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_export_a.column)

        data_object.ib_0_1_for_0_5_reactive_export_a.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_export_a.column)
        data_object.ib_1_for_0_5_reactive_export_a.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_export_a.column)
        data_object.imax_for_0_5_reactive_export_a.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_export_a.column)

        # Для фазы В
        data_object.ib_0_05_for_1_0_reactive_export_b.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_export_b.column)
        data_object.ib_1_for_1_0_reactive_export_b.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_export_b.column)
        data_object.imax_for_1_0_reactive_export_b.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_export_b.column)

        data_object.ib_0_1_for_0_5_reactive_export_b.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_export_b.column)
        data_object.ib_1_for_0_5_reactive_export_b.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_export_b.column)
        data_object.imax_for_0_5_reactive_export_b.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_export_b.column)
        # Для фазы C
        data_object.ib_0_05_for_1_0_reactive_export_c.value = self._get_data_from_table(data_object.ib_0_05_for_1_0_reactive_export_c.column)
        data_object.ib_1_for_1_0_reactive_export_c.value = self._get_data_from_table(data_object.ib_1_for_1_0_reactive_export_c.column)
        data_object.imax_for_1_0_reactive_export_c.value = self._get_data_from_table(data_object.imax_for_1_0_reactive_export_c.column)

        data_object.ib_0_1_for_0_5_reactive_export_c.value = self._get_data_from_table(data_object.ib_0_1_for_0_5_reactive_export_c.column)
        data_object.ib_1_for_0_5_reactive_export_c.value = self._get_data_from_table(data_object.ib_1_for_0_5_reactive_export_c.column)
        data_object.imax_for_0_5_reactive_export_c.value = self._get_data_from_table(data_object.imax_for_0_5_reactive_export_c.column)

    def check_data_for_1ph_reactive_energy_import(self):
        check_the_range_of_values(AllData1PH.ib_0_05_for_1_0_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.ib_0_1_for_1_0_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_1_0_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.imax_for_1_0_reactive_import, self.index)

        check_the_range_of_values(AllData1PH.ib_0_1_for_0_5_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.ib_0_2_for_0_5_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_5_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_5_reactive_import, self.index)

        check_the_range_of_values(AllData1PH.ib_0_2_for_0_25_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_25_reactive_import, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_25_reactive_import, self.index)

    def check_data_for_1ph_reactive_energy_export(self):
        check_the_range_of_values(AllData1PH.ib_0_05_for_1_0_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.ib_0_1_for_1_0_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_1_0_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.imax_for_1_0_reactive_export, self.index)

        check_the_range_of_values(AllData1PH.ib_0_1_for_0_5_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.ib_0_2_for_0_5_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_5_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_5_reactive_export, self.index)

        check_the_range_of_values(AllData1PH.ib_0_2_for_0_25_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.ib_1_for_0_25_reactive_export, self.index)
        check_the_range_of_values(AllData1PH.imax_for_0_25_reactive_export, self.index)

    def check_data_for_3ph_reactive_energy_import(self, data_object):
        check_the_range_of_values(data_object.ib_0_02_for_1_0_reactive_import, self.index)
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_import, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_import, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_import, self.index)

        check_the_range_of_values(data_object.ib_0_05_for_0_5_reactive_import, self.index)
        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_import, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_import, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_import, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_25_reactive_import, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_25_reactive_import, self.index)
        check_the_range_of_values(data_object.imax_for_0_25_reactive_import, self.index)

        # Для фазы А
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_import_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_import_a, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_import_a, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_import_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_import_a, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_import_a, self.index)
        # Для фазы B
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_import_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_import_b, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_import_b, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_import_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_import_b, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_import_b, self.index)
        # Для фазы C
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_import_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_import_c, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_import_c, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_import_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_import_c, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_import_c, self.index)

    def check_data_for_3ph_reactive_energy_export(self, data_object):
        check_the_range_of_values(data_object.ib_0_02_for_1_0_reactive_export, self.index)
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_export, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_export, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_export, self.index)

        check_the_range_of_values(data_object.ib_0_05_for_0_5_reactive_export, self.index)
        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_export, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_export, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_export, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_25_reactive_export, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_25_reactive_export, self.index)
        check_the_range_of_values(data_object.imax_for_0_25_reactive_export, self.index)

        # Для фазы А
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_export_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_export_a, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_export_a, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_export_a, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_export_a, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_export_a, self.index)
        # Для фазы B
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_export_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_export_b, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_export_b, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_export_b, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_export_b, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_export_b, self.index)
        # Для фазы C
        check_the_range_of_values(data_object.ib_0_05_for_1_0_reactive_export_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_1_0_reactive_export_c, self.index)
        check_the_range_of_values(data_object.imax_for_1_0_reactive_export_c, self.index)

        check_the_range_of_values(data_object.ib_0_1_for_0_5_reactive_export_c, self.index)
        check_the_range_of_values(data_object.ib_1_for_0_5_reactive_export_c, self.index)
        check_the_range_of_values(data_object.imax_for_0_5_reactive_export_c, self.index)
