### To run tests:
<code>./run.sh</code>

#### Bugs for user API add:

_________________

###### API add: No "reason" field is returned in case of duplicated "phone" value

Steps to reproduce:
1. Add a new user by sending add api request
2. Add another user with duplicated phone number

Actual result:

No "reason" field is returned: 
<code>{'id': '789gv-rt7840','method': 'add', 'status': 'failure'}</code>

Expected result:

There should be "reason" field, e.g. "phone is duplicated", by requirements

_________________

###### API add: There is no field name is returned in case of type_error

Steps to reproduce:
1. Send add api request with wrong type of any param to get type_error, e.g. with "id": 1

Actual result:

There is no field name is returned in error reason:
<code>'reason': '[json.exception.type_error.302] type must be string, but is number'</code>

Expected result:

There should be field name, like <code>'reason': "id" must be string, but is number'</code>

_________________

###### API add: A negative value of "age" param is accepted

Steps to reproduce:
1. Send add api request with a negative value of "age" param, e.g.: "age": -20

Actual result:

<code>'status': 'success'</code>

Expected result:

<code>'status': 'failure'</code>
