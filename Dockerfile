FROM python:3-onbuild
MAINTAINER Ivan Miric <imiric@gmail.com>

EXPOSE 8000

CMD ["./manage.py", "runserver"]
