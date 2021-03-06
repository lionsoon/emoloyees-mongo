import json
from config.environ import get_env
from database.main import get_database
from database.scheme import SchemeConfig, EmployeeScheme


async def drop_employee():
    employee = get_database()[SchemeConfig.collection_employee]
    await employee.drop()


async def import_employee_json():
    employee = get_database()[SchemeConfig.collection_employee]
    with open(get_env().mongo_seed_json) as f:
        data = json.load(f)
    # validate
    data = [EmployeeScheme(**js).dict(by_alias=True) for js in data]
    await employee.insert_many(data)


async def create_employee_index():
    employee = get_database()[SchemeConfig.collection_employee]
    await employee.create_index(SchemeConfig.employee_indexes)
