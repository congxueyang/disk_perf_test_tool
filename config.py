import os
import yaml

from petname import Generate as pet_generate


cfg_dict = {}


def load_config(file_name, explicit_folder=None):
    global cfg_dict
    first_load = len(cfg_dict) == 0
    cfg_dict.update(yaml.load(open(file_name).read()))

    if first_load:
        var_dir = cfg_dict.get('internal', {}).get('var_dir_root', '/tmp')

    if explicit_folder is None:
        while True:
            dr = os.path.join(var_dir, pet_generate(2, "_"))
            if not os.path.exists(dr):
                break
    else:
        dr = explicit_folder

    cfg_dict['var_dir'] = dr
    if not os.path.exists(cfg_dict['var_dir']):
        os.makedirs(cfg_dict['var_dir'])

    def in_var_dir(fname):
        return os.path.join(cfg_dict['var_dir'], fname)

    charts_img_path = in_var_dir('charts')
    cfg_dict['charts_img_path'] = charts_img_path
    if not os.path.exists(charts_img_path):
        os.makedirs(charts_img_path)

    cfg_dict['vm_ids_fname'] = in_var_dir('os_vm_ids')
    cfg_dict['html_report_file'] = in_var_dir('report.html')
    cfg_dict['text_report_file'] = in_var_dir('report.txt')
    cfg_dict['log_file'] = in_var_dir('log.txt')
    cfg_dict['sensor_storage'] = in_var_dir('sensor_storage.txt')
    cfg_dict['test_log_directory'] = in_var_dir('test_logs')
    if not os.path.exists(cfg_dict['test_log_directory']):
        os.makedirs(cfg_dict['test_log_directory'])
