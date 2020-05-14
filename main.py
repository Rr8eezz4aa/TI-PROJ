from program import *

info = get_informations()
info = remove_dublicate_projects(info)
write_projects_code(info)
write_project_informations(info)
