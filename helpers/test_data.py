def success_data():
    return [
        ({
            "id": "gf564-3456fb",
            "method": "add",
            "name": "TestName",
            "surname": "TestSurname",
            "phone": "21285072",
            "age": 30
        }),  # add unique user

        ({
            "id": "gf564-3456fb",
            "method": "add",
            "name": "TestName2",
            "surname": "TestSurname2",
            "phone": "124853625",
            "age": 31
        }),  # add duplicate id

        ({
            "id": "gd235-235vf",
            "method": "add",
            "name": "TestName2",
            "surname": "TestSurname3",
            "phone": "375716653",
            "age": 32
        }),  # add duplicate name

        ({
            "id": "dfhj6-2658fh",
            "method": "add",
            "name": "TestName3",
            "surname": "TestSurname3",
            "phone": "56535656",
            "age": 33
        }),  # add duplicate surname

        ({
            "id": "gjk9fm-532jkd",
            "method": "add",
            "name": "TestName6",
            "surname": "TestSurname6",
            "phone": "8294158",
            "age": 34
        }),  # add duplicate age

        # add more cases here...
    ]


def failure_data():
    return [
        ({
             "id": "789gv-rt7840",
             "method": "add",
             "name": "TestName10",
             "surname": "TestSurname10",
             "phone": "56535656",
             "age": 34
         }, "phone is duplicated"),  # add duplicate phone

        ({
             "id": "475hdj-34jdf",
             "method": "add",
             "name": None,
             "surname": "TestSurname823",
             "phone": "3474767653",
             "age": 36
         }, "[json.exception.type_error.302] type must be string, but is null"),  # add without name

        ({
             "id": "4638fhd-fjfn",
             "method": "add",
             "name": "TestName483",
             "surname": ["TestSurname32563", "TestSurname23523"],
             "phone": "637320646965",
             "age": 20
         }, "[json.exception.type_error.302] type must be string, but is array"),  # add surname wrong type

        ({
             "id": "4632344-fjfn",
             "method": "add",
             "name": "TestName53",
             "surname": "TestSurname2573",
             "age": 20
         }, "[json.exception.out_of_range.403] key 'phone' not found"),  # add without phone

        ({
             "id": "547ghf-82jf",
             "method": "add",
             "name": "TestName398",
             "surname": "TestSurname8427",
             "phone": 358293568,
             "age": 20
         }, "[json.exception.type_error.302] type must be string, but is number"),  # add phone wrong type

        ({
             "id": "567et-egy54",
             "method": "add",
             "name": "TestName3647",
             "surnames": "TestSurname56434",
             "phone": "34543656",
             "age": 20,
         }, "[json.exception.out_of_range.403] key 'surname' not found"),  # add with wrong key

        ({
             "id": "4657gf-42g4",
             "method": "add",
             "name": "TestName976",
             "surname": "TestSurname84565",
             "phone": "473763539",
             "age": -20,
         }, "age cannot be <= 0"),  # add with negative age number

        # add more cases here...
    ]
