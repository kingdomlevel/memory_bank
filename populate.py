from subprocess import call

call('python manage.py makemigrations memoryBankApp')
call('python manage.py migrate')
call('python manage.py loaddata db.json')