import os

from openpyxl.reader.excel import load_workbook
from libs.all_data_object import PathToFile, AllDataTT, AllData3PH, AllData1PH
from libs.energy_objects import ActiveEnergy, ReactiveEnergy
from libs.get_path_to_exel_file import get_device_type, get_number_of_files_in_directory_exel_file, \
    get_path_to_exel_file

index_of_the_first_meter_for_active_energy_table_for_1ph = 20
index_of_the_first_meter_for_reactive_energy_table_for_1ph = 44

index_of_the_first_meter_for_active_energy_import_table_for_3ph = 21
index_of_the_first_meter_for_active_energy_export_table_for_3ph = 41
index_of_the_first_meter_for_reactive_energy_import_table_for_3ph = 60
index_of_the_first_meter_for_reactive_energy_export_table_for_3ph = 80

try:
    number_of_files = get_number_of_files_in_directory_exel_file()
    for number_of_file in range(number_of_files):
        PathToFile.path = get_path_to_exel_file(number_of_file)
        sheet = load_workbook(PathToFile.path).active

        print(f"\n\n\n############################ В работе файл {PathToFile.path} #################################")

        device_type = get_device_type(number_of_file)
        if device_type == "1PH":
            for i in range(24):
                active_energy = ActiveEnergy(index_of_the_first_meter_for_active_energy_table_for_1ph + i, sheet)

                active_energy.read_exel_and_fill_serial_number(AllData1PH)
                if AllData1PH.serial_number.value is None:
                    break

                print(f'\n...................   В работе счетчик №{AllData1PH.serial_number.value}    .............................')
                print("Считываются данные по активной энергии...")
                active_energy.read_exel_and_fill_data_for_1ph_active_import()
                active_energy.read_exel_and_fill_data_for_1ph_active_export()
                print("\nПроверяются данные по активной энергии...")
                active_energy.check_data_for_1ph_active_energy_import()
                active_energy.check_data_for_1ph_active_energy_export()

                reactive_energy = ReactiveEnergy(index_of_the_first_meter_for_reactive_energy_table_for_1ph + i, sheet)

                print("\nСчитываются данные по реактивной энергии...")
                reactive_energy.read_exel_and_fill_data_for_1ph_reactive_import()
                reactive_energy.read_exel_and_fill_data_for_1ph_reactive_export()
                print("\nПроверяются данные по реактивной энергии...")
                reactive_energy.check_data_for_1ph_reactive_energy_import()
                reactive_energy.check_data_for_1ph_reactive_energy_export()
                print(f'...................   Проверка счетчика №{AllData1PH.serial_number.value} завершена   ...................')
        else:
            if device_type == "TT":
                data_object = AllDataTT
            elif device_type == "3PH":
                data_object = AllData3PH
            else:
                print("Тип счетчика идет нахуй")
                exit()

            for i in range(16):
                active_energy = ActiveEnergy(index_of_the_first_meter_for_active_energy_import_table_for_3ph + i, sheet)
                active_energy.read_exel_and_fill_serial_number(data_object)

                if data_object.serial_number.value is None:
                    break

                print(
                    f'\n\n\n...................   В работе счетчик №{data_object.serial_number.value}    .............................')
                print("Считываются данные по импортируемой активной энергии...")
                active_energy.read_exel_and_fill_data_for_3ph_active_import(data_object)
                print("\nПроверяются данные по импортируемой активной энергии...")
                active_energy.check_data_for_3ph_active_energy_import(data_object)

                active_energy = ActiveEnergy(index_of_the_first_meter_for_active_energy_export_table_for_3ph + i, sheet)

                print("Считываются данные по экспортируемой активной энергии...")
                active_energy.read_exel_and_fill_data_for_3ph_active_export(data_object)
                print("\nПроверяются данные по экспортируемой активной энергии...")
                active_energy.check_data_for_3ph_active_energy_export(data_object)

                reactive_energy = ReactiveEnergy(index_of_the_first_meter_for_reactive_energy_import_table_for_3ph + i, sheet)

                print("\nСчитываются данные по импортируемой реактивной энергии...")
                reactive_energy.read_exel_and_fill_data_for_3ph_reactive_import(data_object)
                print("\nПроверяются данные по импортируемой реактивной энергии...")
                reactive_energy.check_data_for_3ph_reactive_energy_import(data_object)

                reactive_energy = ReactiveEnergy(index_of_the_first_meter_for_reactive_energy_export_table_for_3ph + i, sheet)

                print("\nСчитываются данные по импортируемой реактивной энергии...")
                reactive_energy.read_exel_and_fill_data_for_3ph_reactive_export(data_object)
                print("\nПроверяются данные по импортируемой реактивной энергии...")
                reactive_energy.check_data_for_3ph_reactive_energy_export(data_object)

                print(
                    f'...................   Проверка счетчика №{data_object.serial_number.value} завершена   ...................')
            print(
                f"\n\n\n######################## Проверка файла {PathToFile.path} завершена #############################")
except Exception as e:
    print(e.args)

print("\nДанные в exel файле обновлены.\nПроверка завершена.  ")
