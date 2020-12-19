FROM  tiangolo/uwsgi-nginx:python3.6

LABEL maintainer="Alderano Fileni <afileni@hotmail.com>"

#ENTRYPOINT ["/entrypoint.sh"]

# Add demo app
ADD /site /app

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
#CMD ["/start.sh"]
