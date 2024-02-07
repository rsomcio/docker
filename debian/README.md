docker run --name test -it debian
docker start test
docker container ls
docker exec -it test /bin/bash

to connect to postgresql
su - postgres
psql

# su - postgres

$ createuser --pwprompt admin #from regular shell
$ createdb -O admin testdb

psql -d testdb -h localhost -U admin

=======

apt-get update && apt-get install lsb-release wget procps

sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

apt-get update

apt-get -y install postgresql

docker run -d --name mypostgrescontainer -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword mypostgresimage
